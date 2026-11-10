import json


class VolunteerService:
    def load_volunteers(self):
        with open("data/volunteers.json", "r") as f:
            return json.load(f)

    def save_volunteers(self, volunteers):
        with open("data/volunteers.json", "w") as f:
            json.dump(volunteers, f, indent=2)

    def find_available_driver(self, volunteers, zip_code):
        selected = None
        for v in volunteers:
            if v.get("active") == True:
                if v.get("role") == "driver":
                    if zip_code in v.get("coverage", []):
                        if v.get("assigned_today", 0) < 3:
                            selected = v
                            v["assigned_today"] = v.get("assigned_today", 0) + 1
                            break
        return selected

    def volunteer_summary(self, volunteers):
        result = []
        for v in volunteers:
            result.append(v.get("name") + ":" + v.get("role", "unknown"))
        return result
