def short_id(record):
    cv_str = record["cv"]
    chnu, vrnu = tuple(int(part) for part in cv_str.split(":"))
    cn02vn02 = f"{chnu:02d}{vrnu:02d}"
    ftv = record.get("n_of_m_for_this_verse")
    ftv_str = f"-{ftv[0]}of{ftv[1]}ftv" if ftv else ""  # E.g. -1of2ftv
    return cn02vn02 + ftv_str


def lc_img(record):
    return record.get("lc-img") or f"{short_id(record)}.png"
