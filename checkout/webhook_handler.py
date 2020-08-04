from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f"Webhook recived: {event['type']}",
            status=200
        )

    def handle_payment_event_succeeded(self, event):
        """
        Handle a payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f"Webhook recived: {event['type']}",
            status=200
        )

    def handle_payment_event_failed(self, event):
        """
        Handle a payment_intent.failed webhook from Stripe
        """
        return HttpResponse(
            content=f"Webhook recived: {event['type']}",
            status=200
        )