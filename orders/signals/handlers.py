from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from orders.models import PickUpOrder, DeliveryOrder


@receiver(post_save, sender=PickUpOrder)
def send_pick_up_order_info(sender, **kwargs):
    order = kwargs['instance']
    subject = render_to_string(
        'email/orders/order_letter_subject.txt', {'order': order})
    body = render_to_string(
        'email/orders/order_letter_body.txt', {'order': order})
    send_mail(
        subject,
        body,
        'test@gmail.com',
        [order.email]
    )


@receiver(post_save, sender=DeliveryOrder)
def send_delivery_order_info(sender, **kwargs):
    order = kwargs['instance']
    subject = render_to_string(
        'email/orders/order_letter_subject.txt', {'order': order})
    body = render_to_string(
        'email/orders/order_letter_body.txt', {'order': order})

    recipients = [order.email]
    if order.recipient_email != order.email:
        recipients.append(order.recipient_email)

    send_mail(
        subject,
        body,
        'test@gmail.com',
        recipients
    )
