from django import template

from basic_app.models import Order

register = template.Library()


@register.simple_tag()
def order_total(pk):
    order = Order.objects.get(id=pk)
    print(order.orderedBy.username)
    total = order.quantity * 2 + 3
    return total