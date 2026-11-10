def normalize_zip(zip_code):
    if zip_code is None:
        return ""
    return str(zip_code).strip()


def safe_int(value, default=0):
    try:
        return int(value)
    except:
        return default


def build_label(request):
    return str(request.get("id")) + "-" + request.get("family_name", "unknown")
