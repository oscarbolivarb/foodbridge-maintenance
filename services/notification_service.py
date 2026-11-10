from config import DEFAULT_SENDER, ADMIN_ALERT_EMAIL, ENABLE_SMS


class NotificationService:
    def send_schedule_message(self, request, volunteer):
        family_name = request.get("family_name", "Client")
        driver_name = volunteer.get("name", "Driver")
        email = request.get("email")
        phone = request.get("phone")
        message = "Hello " + family_name + ", your food delivery is scheduled with " + driver_name
        print("EMAIL FROM", DEFAULT_SENDER, "TO", email, message)
        if ENABLE_SMS and phone:
            print("SMS TO", phone, message)

    def send_internal_alert(self, message):
        print("ALERT TO", ADMIN_ALERT_EMAIL, message)

    def send_low_inventory_alert(self, item_name, current_count):
        print("ALERT TO", ADMIN_ALERT_EMAIL, "Inventory low for", item_name, current_count)
