from django.db.models import Sum


class OrderCalculator:

    @staticmethod
    def get_sum_orders(order):
        sum_price = order.items_in_order.values_list(
            'price', flat=True
        ).aggregate(Sum('price'))
        return sum_price['price__sum']
