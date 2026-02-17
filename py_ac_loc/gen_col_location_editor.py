"""
Generate an interactive HTML editor for adjusting column/line
locations on an Aleppo Codex page image.

Shows the full page image with a transparent overlay of two columns,
each containing 28 red line segments. The user can drag control
points to adjust column positions and line spacing.

Usage:
    python py_ac_loc/gen_col_location_editor.py 270r
"""

import json
import sys
import webbrowser
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT_DIR = BASE / ".novc"
COORD_DIR = Path(__file__).resolve().parent / "column-coordinates"

LINES_PER_COL = 28

_FALLBACK_DEFAULTS = {
    "col1": {
        "cx": 0.7242,
        "cy": 0.4535,
        "hw": 0.19,
        "hh": 0.3714,
        "topAngle": 0,
        "botAngle": 0,
    },
    "col2": {
        "cx": 0.2604,
        "cy": 0.4541,
        "hw": 0.1934,
        "hh": 0.3725,
        "topAngle": 0,
        "botAngle": 0,
    },
}


def _load_defaults(page_id):
    """Load saved column coordinates if they exist, else use fallback."""
    coord_file = COORD_DIR / f"{page_id}.json"
    if coord_file.exists():
        data = json.loads(coord_file.read_text(encoding="utf-8"))
        result = {}
        for col_key in ("col1", "col2"):
            rel = data["columns"][col_key]["rel"]
            hw = rel["w"] / 2
            hh = rel["h"] / 2
            result[col_key] = {
                "cx": round(rel["x"] + hw, 4),
                "cy": round(rel["y"] + hh, 4),
                "hw": round(hw, 4),
                "hh": round(hh, 4),
                "topAngle": rel["top_angle"],
                "botAngle": rel["bot_angle"],
            }
        return result, True
    return _FALLBACK_DEFAULTS, False


def _leaf_to_page_n(page_id):
    """Convert a leaf ID like '270r' to the archive.org 0-based page index."""
    num = int(page_id[:-1])
    side = page_id[-1]
    return (num - 1) * 2 + 2 + (0 if side == "r" else 1)


def _image_url(page_id):
    """Build archive.org direct image URL for an Aleppo Codex page."""
    n = _leaf_to_page_n(page_id)
    return (
        "https://ia601801.us.archive.org/BookReader/BookReaderImages.php"
        f"?zip=/7/items/aleppo-codex/Aleppo%20Codex_jp2.zip"
        f"&file=Aleppo%20Codex_jp2/Aleppo%20Codex_{n:04d}.jp2"
        f"&id=aleppo-codex&scale=2&rotate=0"
    )


def generate_editor(page_id):
    """Generate the HTML column-location editor for a page."""

    img_url = _image_url(page_id)
    defaults, from_file = _load_defaults(page_id)
    c1 = defaults["col1"]
    c2 = defaults["col2"]
    source_note = (
        f"column-coordinates/{page_id}.json" if from_file else "fallback defaults"
    )

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Column Location Editor \u2014 {{page_id}}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    background: #222;
    color: #eee;
    font-family: system-ui, sans-serif;
    overflow: hidden;
  }}
  #toolbar {{
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 36px;
    background: #333;
    display: flex;
    align-items: center;
    padding: 0 12px;
    gap: 12px;
    z-index: 100;
    font-size: 14px;
  }}
  #toolbar button {{
    padding: 4px 12px;
    cursor: pointer;
    border: 1px solid #666;
    background: #444;
    color: #eee;
    border-radius: 3px;
  }}
  #toolbar button:hover {{ background: #555; }}
  #toolbar .info {{ color: #aaa; margin-left: auto; }}
  #container {{
    position: absolute;
    top: 36px; left: 0; right: 0; bottom: 0;
    overflow: auto;
  }}
  #page-wrapper {{
    position: relative;
    display: block;
    margin: 0 auto;
    width: fit-content;
  }}
  #page-wrapper img {{
    display: block;
    height: calc(100vh - 36px);
    width: auto;
  }}
  #overlay {{
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
  }}
  #overlay svg {{
    width: 100%;
    height: 100%;
  }}
  /* Control points are interactive */
  .ctrl-point {{
    pointer-events: all;
    cursor: grab;
    fill: rgba(0, 200, 255, 0.6);
    stroke: #0af;
    stroke-width: 1;
  }}
  .ctrl-point:hover {{
    fill: rgba(0, 200, 255, 0.9);
  }}
  .ctrl-point.dragging {{
    cursor: grabbing;
    fill: #ff0;
  }}
  .ctrl-point.active-target {{
    animation: pulse-handle 0.8s ease-in-out infinite;
  }}
  @keyframes pulse-handle {{
    0%, 100% {{ fill-opacity: 1; stroke-width: 3; }}
    50% {{ fill-opacity: 0.3; stroke-width: 1; }}
  }}
  .skew-label-active {{
    animation: pulse-skew 0.8s ease-in-out infinite;
  }}
  @keyframes pulse-skew {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0.2; }}
  }}
</style>
</head>
<body>

<div id="toolbar">
  <span><b>Col Location</b> \u2014 {page_id}</span>
  <button id="fine-btn" onclick="toggleFine()" style="background:#070">Fine: ON</button>
  <button id="skew-btn" onclick="cycleSkew()">Skew: C1 Top</button>
  <button onclick="rotate(-1)">Rotate \u21b6</button>
  <button onclick="rotate(+1)">Rotate \u21b7</button>
  <button onclick="resetPositions()">Reset</button>
  <button onclick="exportJSON()">Export JSON</button>
  <span class="info" id="status">Drag handles to resize; buttons to skew</span>
</div>

<div id="container">
  <div id="page-wrapper">
    <img id="page-img" src="{img_url}" alt="Codex page {page_id}">
    <div id="overlay">
      <svg id="overlay-svg" viewBox="0 0 1000 1000" preserveAspectRatio="none">
      </svg>
    </div>
  </div>
</div>

<script>
const LINES = {LINES_PER_COL};
const DEG = Math.PI / 180;

// Each column is a trapezoid: centre (cx,cy), half-extents (hw,hh),
// independent top/bottom edge angles in degrees.
// Col 1 = right column, Col 2 = left column.
// Source: {source_note}
const DEFAULTS = {{
  col1: {{ cx: {c1['cx']}, cy: {c1['cy']}, hw: {c1['hw']}, hh: {c1['hh']}, topAngle: {c1['topAngle']}, botAngle: {c1['botAngle']} }},
  col2: {{ cx: {c2['cx']}, cy: {c2['cy']}, hw: {c2['hw']}, hh: {c2['hh']}, topAngle: {c2['topAngle']}, botAngle: {c2['botAngle']} }},
}};

let cols = JSON.parse(JSON.stringify(DEFAULTS));

const svg = document.getElementById('overlay-svg');
const status = document.getElementById('status');

// Fine mode: scale down mouse deltas by FINE_SCALE for precise adjustments.
let fineMode = true;
const FINE_SCALE = 0.2;  // 1/5 sensitivity

function toggleFine() {{
  fineMode = !fineMode;
  document.getElementById('fine-btn').textContent = fineMode ? 'Fine: ON' : 'Fine: OFF';
  document.getElementById('fine-btn').style.background = fineMode ? '#070' : '';
}}

// --- Geometry helpers ---

function lineEndpoints(r, t) {{
  // Returns {{ left, right }} for the line at parameter t (0=top, 1=bottom).
  // The angle interpolates linearly between topAngle and botAngle.
  const angle = r.topAngle + t * (r.botAngle - r.topAngle);
  const cos = Math.cos(angle * DEG);
  const sin = Math.sin(angle * DEG);
  const cy = r.cy - r.hh + t * 2 * r.hh;
  return {{
    left:  {{ x: r.cx - r.hw * cos, y: cy + r.hw * sin }},
    right: {{ x: r.cx + r.hw * cos, y: cy - r.hw * sin }},
  }};
}}

function corners(r) {{
  // Returns {{ tl, tr, bl, br }} from the top and bottom line endpoints.
  const top = lineEndpoints(r, 0);
  const bot = lineEndpoints(r, 1);
  return {{ tl: top.left, tr: top.right, bl: bot.left, br: bot.right }};
}}

function midpoints(r) {{
  // Returns {{ top, bottom, left, right }} midpoints of each side.
  return {{
    top:    {{ x: r.cx, y: r.cy - r.hh }},
    bottom: {{ x: r.cx, y: r.cy + r.hh }},
    left:   {{ x: r.cx - r.hw, y: r.cy }},
    right:  {{ x: r.cx + r.hw, y: r.cy }},
  }};
}}

function lerp(a, b, t) {{
  return {{ x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t }};
}}

function clamp(v) {{ return Math.max(0, Math.min(1, v)); }}

// --- Drawing ---

function drawAll() {{
  while (svg.firstChild) svg.removeChild(svg.firstChild);

  for (const [colName, r] of Object.entries(cols)) {{
    const colNum = colName === 'col1' ? 1 : 2;
    const colour = colNum === 1 ? 'rgba(255, 60, 60, 0.7)' : 'rgba(60, 120, 255, 0.7)';
    const handleColour = colNum === 1 ? 'rgba(255, 80, 80, 0.8)' : 'rgba(80, 140, 255, 0.8)';
    const c = corners(r);

    // Draw line segments.
    for (let i = 0; i < LINES; i++) {{
      const t = LINES === 1 ? 0.5 : i / (LINES - 1);
      const ep = lineEndpoints(r, t);
      const left = ep.left;
      const right = ep.right;

      const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', left.x * 1000);
      line.setAttribute('y1', left.y * 1000);
      line.setAttribute('x2', right.x * 1000);
      line.setAttribute('y2', right.y * 1000);
      line.setAttribute('stroke', colour);
      line.setAttribute('stroke-width', '1.5');
      svg.appendChild(line);

      // Label: show line number just outside the outer edge of the column.
      const labelPt = colNum === 1 ? right : left;
      const nudgeX = colNum === 1 ? 12 : -12;
      const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      label.setAttribute('x', labelPt.x * 1000 + nudgeX);
      label.setAttribute('y', labelPt.y * 1000 + 3);
      label.setAttribute('text-anchor', colNum === 1 ? 'start' : 'end');
      label.setAttribute('font-size', '8');
      label.setAttribute('fill', colour);
      label.textContent = `${{i + 1}}`;
      svg.appendChild(label);
    }}

    // Side-midpoint handles (each adjusts only one dimension).
    const m = midpoints(r);
    const at = activeTargets();
    for (const side of ['top', 'bottom', 'left', 'right']) {{
      const pt = m[side];
      const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle.setAttribute('cx', pt.x * 1000);
      circle.setAttribute('cy', pt.y * 1000);
      circle.setAttribute('r', '8');
      let cls = 'ctrl-point';
      if (at.handle && at.handle.col === colName && at.handle.side === side) {{
        cls += ' active-target';
        circle.setAttribute('fill', '#ff0');
        circle.setAttribute('stroke', '#ff0');
      }} else {{
        circle.setAttribute('fill', handleColour);
        circle.setAttribute('stroke', handleColour);
      }}
      circle.setAttribute('class', cls);
      circle.setAttribute('data-col', colName);
      circle.setAttribute('data-side', side);
      svg.appendChild(circle);
    }}

    // Bounding outline: sides extend one line-spacing below the last line.
    const lineSpacingFrac = LINES > 1 ? 1 / (LINES - 1) : 1;
    const ext = lineEndpoints(r, 1 + lineSpacingFrac);
    const extBl = ext.left;
    const extBr = ext.right;
    const outline = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    const pts = [c.tl, c.tr, extBr, extBl]
      .map(p => `${{p.x * 1000}},${{p.y * 1000}}`)
      .join(' ');
    outline.setAttribute('points', pts);
    outline.setAttribute('fill', 'none');
    outline.setAttribute('stroke', colour);
    outline.setAttribute('stroke-width', '1');
    outline.setAttribute('stroke-dasharray', '6 3');
    svg.appendChild(outline);
  }}

  // --- Skew indicator: triangle next to the active skew target line ---
  const st = SKEW_TARGETS[skewIndex];
  const sr = cols[st.col];
  const sColNum = st.col === 'col1' ? 1 : 2;
  const sT = st.edge === 'topAngle' ? 0 : 1;
  const sEp = lineEndpoints(sr, sT);
  // Place on outer edge of the column
  const sPt = sColNum === 1 ? sEp.right : sEp.left;
  const sDir = sColNum === 1 ? 1 : -1;  // +1 = rightward, -1 = leftward
  const sx = sPt.x * 1000 + sDir * 28;
  const sy = sPt.y * 1000;
  // Draw "skew" label in column colour
  const skColour = sColNum === 1 ? '#ff4040' : '#4080ff';
  const skLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  skLabel.setAttribute('x', sx);
  skLabel.setAttribute('y', sy + 3);
  skLabel.setAttribute('text-anchor', sColNum === 1 ? 'start' : 'end');
  skLabel.setAttribute('font-size', '10');
  skLabel.setAttribute('font-weight', 'bold');
  skLabel.setAttribute('fill', skColour);
  skLabel.textContent = 'skew';
  if (activeTargets().skew) {{
    skLabel.setAttribute('class', 'skew-label-active');
  }}
  svg.appendChild(skLabel);
}}

// --- Dragging (side handles, each adjusts only one dimension) ---

let dragTarget = null;
let dragCol = null;
let dragSide = null;
let dragStartMouse = null;   // mouse pos at drag start (normalised)
let dragStartRect = null;    // snapshot of rect params at drag start

// Track what arrow keys affect.
// cursorMode: 'topbot-skew' or 'side'
//   'topbot-skew': Up/Down move vertCol's vertEdge; Left/Right adjust skew.
//   'side': Left/Right move sideCol's sideEdge.
let cursorMode = 'topbot-skew';
let vertCol = 'col1';    // which column's top/bot edge Up/Down affects
let vertEdge = 'top';    // 'top' or 'bottom'
let sideCol = 'col1';    // which column's left/right edge Left/Right affects
let sideEdge = 'right';  // 'left' or 'right'

// Helper for drawAll to know what to highlight.
function activeTargets() {{
  if (cursorMode === 'topbot-skew') {{
    return {{ handle: {{ col: vertCol, side: vertEdge }}, skew: true }};
  }} else {{
    return {{ handle: {{ col: sideCol, side: sideEdge }}, skew: false }};
  }}
}}

svg.addEventListener('mousedown', (e) => {{
  if (e.target.classList.contains('ctrl-point')) {{
    dragTarget = e.target;
    dragCol = dragTarget.getAttribute('data-col');
    dragSide = dragTarget.getAttribute('data-side');
    // Clicking a top/bottom handle switches skew target to that edge.
    if (dragSide === 'top' || dragSide === 'bottom') {{
      const edge = dragSide === 'top' ? 'topAngle' : 'botAngle';
      const idx = SKEW_TARGETS.findIndex(t => t.col === dragCol && t.edge === edge);
      if (idx >= 0 && idx !== skewIndex) {{
        skewIndex = idx;
        updateSkewBtn();
      }}
    }}
    dragTarget.classList.add('dragging');
    const svgRect = svg.getBoundingClientRect();
    dragStartMouse = {{
      x: (e.clientX - svgRect.left) / svgRect.width,
      y: (e.clientY - svgRect.top) / svgRect.height,
    }};
    dragStartRect = JSON.parse(JSON.stringify(cols[dragCol]));
    e.preventDefault();
  }}
}});

window.addEventListener('mousemove', (e) => {{
  if (!dragTarget) return;
  const svgRect = svg.getBoundingClientRect();
  let mx = (e.clientX - svgRect.left) / svgRect.width;
  let my = (e.clientY - svgRect.top) / svgRect.height;

  // In fine mode, scale the delta from the drag-start position.
  if (fineMode) {{
    mx = dragStartMouse.x + (mx - dragStartMouse.x) * FINE_SCALE;
    my = dragStartMouse.y + (my - dragStartMouse.y) * FINE_SCALE;
  }}
  mx = clamp(mx);
  my = clamp(my);

  // Reset rect to drag-start state, then apply new position.
  const r0 = dragStartRect;
  const r = cols[dragCol];
  r.cx = r0.cx; r.cy = r0.cy; r.hw = r0.hw; r.hh = r0.hh;

  // Each side handle moves only its own edge; the opposite edge stays put.
  const top0  = r0.cy - r0.hh;
  const bot0  = r0.cy + r0.hh;
  const left0 = r0.cx - r0.hw;
  const right0 = r0.cx + r0.hw;

  if (dragSide === 'right') {{
    const newRight = Math.max(left0 + 0.02, mx);
    r.hw = (newRight - left0) / 2;
    r.cx = (left0 + newRight) / 2;
  }} else if (dragSide === 'left') {{
    const newLeft = Math.min(right0 - 0.02, mx);
    r.hw = (right0 - newLeft) / 2;
    r.cx = (newLeft + right0) / 2;
  }} else if (dragSide === 'bottom') {{
    const newBot = Math.max(top0 + 0.02, my);
    r.hh = (newBot - top0) / 2;
    r.cy = (top0 + newBot) / 2;
  }} else if (dragSide === 'top') {{
    const newTop = Math.min(bot0 - 0.02, my);
    r.hh = (bot0 - newTop) / 2;
    r.cy = (newTop + bot0) / 2;
  }}

  drawAll();
  updateStatus();
}});

window.addEventListener('mouseup', () => {{
  if (dragTarget) {{
    if (dragSide === 'top' || dragSide === 'bottom') {{
      cursorMode = 'topbot-skew';
      vertCol = dragCol;
      vertEdge = dragSide;
    }} else {{
      cursorMode = 'side';
      sideCol = dragCol;
      sideEdge = dragSide;
    }}
    dragTarget.classList.remove('dragging');
    dragTarget = null;
    drawAll();
  }}
}});

// --- Skew selector ---

const SKEW_TARGETS = [
  {{ col: 'col1', edge: 'topAngle', label: 'C1 Top' }},
  {{ col: 'col1', edge: 'botAngle', label: 'C1 Bot' }},
  {{ col: 'col2', edge: 'topAngle', label: 'C2 Top' }},
  {{ col: 'col2', edge: 'botAngle', label: 'C2 Bot' }},
];
let skewIndex = 0;

function updateSkewBtn() {{
  const btn = document.getElementById('skew-btn');
  const t = SKEW_TARGETS[skewIndex];
  btn.textContent = 'Skew: ' + t.label;
  btn.style.color = t.col === 'col1' ? '#ff4040' : '#4080ff';
}}

function cycleSkew() {{
  skewIndex = (skewIndex + 1) % SKEW_TARGETS.length;
  updateSkewBtn();
  drawAll();
  updateStatus();
}}

// --- Rotation (applies to selected skew target) ---

function rotate(degrees) {{
  const d = fineMode ? degrees * FINE_SCALE : degrees;
  const target = SKEW_TARGETS[skewIndex];
  cols[target.col][target.edge] += d;
  cursorMode = 'topbot-skew';
  drawAll();
  updateStatus();
}}

// --- Arrow keys ---
// topbot-skew mode: Up/Down move top/bot edge, Left/Right adjust skew.
// side mode: Left/Right move a side edge.

const ARROW_STEP = 0.001;  // ~1px at typical image sizes

function nudgeEdge(col, side, delta) {{
  const r = cols[col];
  const top0  = r.cy - r.hh;
  const bot0  = r.cy + r.hh;
  const left0 = r.cx - r.hw;
  const right0 = r.cx + r.hw;
  if (side === 'top') {{
    const newTop = Math.min(bot0 - 0.02, top0 + delta);
    r.hh = (bot0 - newTop) / 2;
    r.cy = (newTop + bot0) / 2;
  }} else if (side === 'bottom') {{
    const newBot = Math.max(top0 + 0.02, bot0 + delta);
    r.hh = (newBot - top0) / 2;
    r.cy = (top0 + newBot) / 2;
  }} else if (side === 'left') {{
    const newLeft = Math.min(right0 - 0.02, left0 + delta);
    r.hw = (right0 - newLeft) / 2;
    r.cx = (newLeft + right0) / 2;
  }} else if (side === 'right') {{
    const newRight = Math.max(left0 + 0.02, right0 + delta);
    r.hw = (newRight - left0) / 2;
    r.cx = (left0 + newRight) / 2;
  }}
}}

window.addEventListener('keydown', (e) => {{
  if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].indexOf(e.key) < 0) return;
  e.preventDefault();

  const step = fineMode ? ARROW_STEP * FINE_SCALE : ARROW_STEP;

  if (cursorMode === 'topbot-skew') {{
    if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {{
      const dy = e.key === 'ArrowUp' ? -step : step;
      nudgeEdge(vertCol, vertEdge, dy);
    }} else {{
      // Left/Right adjust skew
      if (e.key === 'ArrowLeft') rotate(-1);
      else if (e.key === 'ArrowRight') rotate(1);
      return;  // rotate already redraws
    }}
  }} else {{
    // side mode
    if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {{
      const dx = e.key === 'ArrowLeft' ? -step : step;
      nudgeEdge(sideCol, sideEdge, dx);
    }}
    // Up/Down in side mode: move the last vert target if set
    if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {{
      const dy = e.key === 'ArrowUp' ? -step : step;
      nudgeEdge(vertCol, vertEdge, dy);
    }}
  }}

  drawAll();
  updateStatus();
}});

// --- Status ---

function updateStatus() {{
  const target = SKEW_TARGETS[skewIndex];
  const val = cols[target.col][target.edge].toFixed(2);
  const c1t = cols.col1.topAngle.toFixed(2);
  const c1b = cols.col1.botAngle.toFixed(2);
  const c2t = cols.col2.topAngle.toFixed(2);
  const c2b = cols.col2.botAngle.toFixed(2);
  status.textContent =
    `[${{target.label}}: ${{val}}\u00b0]  ` +
    `C1: ${{c1t}}\u00b0/${{c1b}}\u00b0  C2: ${{c2t}}\u00b0/${{c2b}}\u00b0`;
}}

function f(pt) {{ return `${{(pt.x * 100).toFixed(1)}}%,${{(pt.y * 100).toFixed(1)}}%`; }}

// --- Reset ---

function resetPositions() {{
  cols = JSON.parse(JSON.stringify(DEFAULTS));
  drawAll();
  updateStatus();
}}

// --- Export ---

function exportJSON() {{
  const img = document.getElementById('page-img');
  const W = img.naturalWidth;
  const H = img.naturalHeight;

  const colData = {{}};
  for (const [colName, r] of Object.entries(cols)) {{
    const colNum = colName === 'col1' ? 1 : 2;
    const c = corners(r);
    const w = 2 * r.hw;
    const h = 2 * r.hh;
    const lineSpacing = LINES > 1 ? h / (LINES - 1) : h;
    colData[`col${{colNum}}`] = {{
      rel: {{
        x: round4(c.tl.x), y: round4(c.tl.y),
        w: round4(w), h: round4(h),
        top_angle: round4(r.topAngle),
        bot_angle: round4(r.botAngle),
        line_spacing: round4(lineSpacing),
      }},
      px: {{
        x: Math.round(c.tl.x * W), y: Math.round(c.tl.y * H),
        w: Math.round(w * W), h: Math.round(h * H),
        top_angle: round4(r.topAngle),
        bot_angle: round4(r.botAngle),
        line_spacing: Math.round(lineSpacing * H),
      }},
    }};
  }}
  const json = JSON.stringify({{
    page: "{page_id}",
    image_size: {{ width: W, height: H }},
    lines_per_col: LINES,
    columns: colData,
  }}, null, 2);
  navigator.clipboard.writeText(json).then(() => {{
    status.textContent = 'JSON copied to clipboard!';
    setTimeout(updateStatus, 2000);
  }});
}}

function round4(v) {{ return Math.round(v * 10000) / 10000; }}

// --- Init ---

updateSkewBtn();
drawAll();
updateStatus();

// Scroll to show col1 (right column) when the image is wider than viewport.
document.getElementById('page-img').addEventListener('load', () => {{
  const container = document.getElementById('container');
  const col1 = cols.col1;
  // Scroll so that col1's center is visible, biased toward the right edge.
  const imgEl = document.getElementById('page-img');
  const renderedW = imgEl.clientWidth;
  const targetX = col1.cx * renderedW;
  const scrollX = targetX - container.clientWidth / 2;
  if (scrollX > 0) container.scrollLeft = scrollX;
}});
</script>
</body>
</html>
"""

    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / f"col_editor_{page_id}.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Editor written to {out_path}")
    webbrowser.open(out_path.as_uri())


def main():
    if len(sys.argv) < 2:
        print("Usage: python py_ac_loc/gen_col_location_editor.py <page_id>")
        print("  e.g. python py_ac_loc/gen_col_location_editor.py 270r")
        sys.exit(1)
    page_id = sys.argv[1]
    generate_editor(page_id)


if __name__ == "__main__":
    main()
