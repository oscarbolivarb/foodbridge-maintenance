from services.request_service import RequestService
from services.inventory_service import InventoryService
from services.volunteer_service import VolunteerService
from services.notification_service import NotificationService
from services.reporting_service import ReportingService


def run_daily_process():
    request_service = RequestService()
    inventory_service = InventoryService()
    volunteer_service = VolunteerService()
    notifier = NotificationService()
    reporting = ReportingService()

    requests = request_service.load_requests()
    inventory = inventory_service.load_inventory()
    volunteers = volunteer_service.load_volunteers()

    processed = []
    for request in requests:
        if request.get("status") != "new":
            continue

        if not (request.get("household_size", 0) > 0):
            request["status"] = "invalid"
            continue

        if not inventory_service.can_fulfill(request, inventory):
            request["status"] = "pending_inventory"
            notifier.send_internal_alert(
                "Insufficient inventory for request " + str(request.get("id"))
            )
            continue

        volunteer = volunteer_service.find_available_driver(
            volunteers, request.get("zip_code")
        )
        if not volunteer:
            request["status"] = "pending_driver"
            notifier.send_internal_alert(
                "No driver for request " + str(request.get("id"))
            )
            continue

        inventory_service.reserve_items(request, inventory)
        request_service.mark_scheduled(request, volunteer)
        notifier.send_schedule_message(request, volunteer)
        processed.append(request)

    request_service.save_requests(requests)
    inventory_service.save_inventory(inventory)
    reporting.build_daily_summary(requests, volunteers, inventory)
    return processed


if __name__ == "__main__":
    run_daily_process()
