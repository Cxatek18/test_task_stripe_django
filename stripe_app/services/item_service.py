class ItemService:

    @staticmethod
    def get_stripe(stripe, item, unit_amount_formula, currency):
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': currency,
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(unit_amount_formula),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return session
