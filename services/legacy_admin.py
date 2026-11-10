# legacy admin helper utilities
# TODO: clean this up later

from services.request_service import RequestService
from services.inventory_service import InventoryService
from services.volunteer_service import VolunteerService


class LegacyAdminTools:
    def __init__(self):
        self.request_service = RequestService()
        self.inventory_service = InventoryService()
        self.volunteer_service = VolunteerService()

    def emergency_reset_all_statuses(self):
        requests = self.request_service.load_requests()
        for r in requests:
            r["status"] = "new"
            if "assigned_driver" in r:
                del r["assigned_driver"]
        self.request_service.save_requests(requests)

    def print_everything(self):
        requests = self.request_service.load_requests()
        inventory = self.inventory_service.load_inventory()
        volunteers = self.volunteer_service.load_volunteers()
        print(requests)
        print(inventory)
        print(volunteers)
