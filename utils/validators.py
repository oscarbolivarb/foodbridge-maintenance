def validate_request(request):
    errors = []
    if not request.get("family_name"):
        errors.append("family_name missing")
    if not request.get("zip_code"):
        errors.append("zip_code missing")
    if request.get("household_size", 0) <= 0:
        errors.append("household_size invalid")
    return errors
