import stripe

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.generic import View, TemplateView
from .models import Item, Order
from .services.order_сalculator import OrderCalculator
from .services.item_service import ItemService
from .services.order_service import OrderService


def handling_error_404(request, exception):
    """
    Кастомная страница для ошибки 404
    """
    return render(request, 'error_templates/404_page.html', status=404)


class ItemCreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        item = Item.objects.get(pk=self.kwargs['pk'])
        if item.currency == 'USD':
            formula = item.price*100
            session = ItemService.get_stripe(stripe, item,  formula, 'usd')
            return JsonResponse({'session_id': session.id})
        elif item.currency == 'AUD':
            formula = item.price*100
            session = ItemService.get_stripe(stripe, item,  formula, 'aud')
            return JsonResponse({'session_id': session.id})


class ItemBuyView(View):
    def get(self, request, *args, **kwargs):
        get_item = Item.objects.get(pk=self.kwargs['session_id'])
        context = {
            'item': get_item,
        }
        return render(request, 'item.html', context)


class OrderCreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        order = Order.objects.get(pk=self.kwargs['pk'])
        if (order.order_tax and order.order_discount) is not None:
            tax = order.order_tax.tax
            discount = order.order_discount.discount
            session = OrderService.get_order_stripe(
                stripe, (
                    OrderCalculator.get_sum_orders(order)*100
                )+(tax*100)-(discount*100)
            )
            return JsonResponse({'session_id': session.id})
        elif order.order_tax is not None:
            tax = order.order_tax.tax
            session = OrderService.get_order_stripe(
                stripe, (OrderCalculator.get_sum_orders(order)*100)+(tax*100)
            )
            return JsonResponse({'session_id': session.id})
        elif order.order_discount is not None:
            discount = order.order_discount.discount
            session = OrderService.get_order_stripe(
                stripe, (OrderCalculator.get_sum_orders(order)*100)-(discount*100)
            )
            return JsonResponse({'session_id': session.id})
        else:
            session = OrderService.get_order_stripe(
                stripe, OrderCalculator.get_sum_orders(order)*100
            )
            return JsonResponse({'session_id': session.id})


class OrderView(View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(pk=self.kwargs['order_id'])
        context = {
            'order': order,
            'full_sum': OrderCalculator.get_sum_orders(order),
        }
        return render(request, 'order.html', context)


class HomeView(TemplateView):
    """
    ***Примечание***
    Главная страница сделана для удобства.
    В задании не указан этот пункт.
    """
    template_name = 'index.html'
    extra_context = {'title_head': 'Главная'}
