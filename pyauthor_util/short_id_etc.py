def short_id(quirkrec):
    cv_str = quirkrec["qr-cv"]
    chnu, vrnu = tuple(int(part) for part in cv_str.split(":"))
    cn02vn02 = f"{chnu:02d}{vrnu:02d}"
    ftv = quirkrec.get("qr-n_of_m_for_this_verse")
    ftv_str = f"-{ftv[0]}of{ftv[1]}ftv" if ftv else ""  # E.g. -1of2ftv
    return cn02vn02 + ftv_str
