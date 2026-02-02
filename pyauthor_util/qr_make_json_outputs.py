"""Generate JSON file with quirkrec field usage statistics."""

from collections import Counter
from pycmn.file_io import json_dump_to_file_path


def write_qr_field_stats_json(quirkrecs, out_path):
    """
    Write a JSON file containing counts of all fields used in quirkrecs.

    Args:
        quirkrecs: List of quirkrec dicts (after processing, including nbd)
        out_path: Path to write the JSON file
    """
    field_counter = Counter()
    for qr in quirkrecs:
        for key in qr:
            field_counter[key] += 1

    # Sort by count descending, then by field name
    sorted_fields = sorted(
        field_counter.items(),
        key=lambda x: (-x[1], x[0])
    )

    output = {
        "description": "Count of fields used in quirkrecs",
        "total_quirkrecs": len(quirkrecs),
        "fields": [
            {"field": field, "count": count}
            for field, count in sorted_fields
        ]
    }

    json_dump_to_file_path(output, out_path)


def write_quirkrecs_json(quirkrecs, out_path):
    """
    Write a JSON file containing all quirkrecs data.

    Args:
        quirkrecs: List of quirkrec dicts (after processing, including nbd)
        out_path: Path to write the JSON file
    """
    json_dump_to_file_path(quirkrecs, out_path)
