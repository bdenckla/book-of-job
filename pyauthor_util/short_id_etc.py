def short_id(record):
    cv_str = record["qr-cv"]
    chnu, vrnu = tuple(int(part) for part in cv_str.split(":"))
    cn02vn02 = f"{chnu:02d}{vrnu:02d}"
    ftv = record.get("qr-n_of_m_for_this_verse")
    ftv_str = f"-{ftv[0]}of{ftv[1]}ftv" if ftv else ""  # E.g. -1of2ftv
    return cn02vn02 + ftv_str


def lc_img(record):
    nb = record["qr-noted-by"]
    zuxlc = "-zUXLC" in nb or "-nUXLC" in nb
    ext = ".jpg" if zuxlc else ".png"
    return record.get("qr-lc-img") or f"{short_id(record)}{ext}"
