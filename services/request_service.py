import json


class RequestService:
    def load_requests(self):
        with open("data/requests.json", "r") as f:
            return json.load(f)

    def save_requests(self, requests):
        with open("data/requests.json", "w") as f:
            json.dump(requests, f, indent=2)

    def mark_scheduled(self, request, volunteer):
        request["status"] = "scheduled"
        request["assigned_driver"] = volunteer.get("name")
        request["scheduled_window"] = "9am-1pm"

    def find_request_by_family(self, requests, family_name):
        found = None
        for r in requests:
            if r.get("family_name") == family_name:
                found = r
        return found

    def build_request_message(self, request):
        msg = "Request #" + str(request.get("id")) + " for " + request.get("family_name", "Unknown")
        msg += " in zip " + str(request.get("zip_code"))
        msg += " household size=" + str(request.get("household_size"))
        return msg
