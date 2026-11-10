from config import REPORT_OUTPUT


class ReportingService:
    def build_daily_summary(self, requests, volunteers, inventory):
        total = len(requests)
        scheduled = 0
        pending_inventory = 0
        pending_driver = 0
        invalid = 0
        for r in requests:
            if r.get("status") == "scheduled":
                scheduled += 1
            if r.get("status") == "pending_inventory":
                pending_inventory += 1
            if r.get("status") == "pending_driver":
                pending_driver += 1
            if r.get("status") == "invalid":
                invalid += 1

        with open(REPORT_OUTPUT, "w") as f:
            f.write("Daily Summary\n")
            f.write("Total requests: " + str(total) + "\n")
            f.write("Scheduled: " + str(scheduled) + "\n")
            f.write("Pending inventory: " + str(pending_inventory) + "\n")
            f.write("Pending driver: " + str(pending_driver) + "\n")
            f.write("Invalid: " + str(invalid) + "\n")
            f.write("Inventory remaining: " + str(inventory) + "\n")
            f.write("Volunteer count: " + str(len(volunteers)) + "\n")
