class OrderService:

    @staticmethod
    def get_order_stripe(stripe, unit_amount_formula):
        session = stripe.checkout.Session.create(
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Список покупок',
                        },
                        'unit_amount': unit_amount_formula,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='https://example.com/success',
                cancel_url='https://example.com/cancel',
            )
        return session
