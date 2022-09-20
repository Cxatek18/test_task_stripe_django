from django.urls import path
from .views import (
    ItemCreateCheckoutSessionView,
    ItemBuyView,
    OrderView,
    OrderCreateCheckoutSessionView,
    HomeView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path(
        'buy/<int:pk>/', ItemCreateCheckoutSessionView.as_view(),
        name='create_session_item'
    ),
    path('item/<int:session_id>/', ItemBuyView.as_view(), name='get_item'),
    path(
        'buy-order/<int:pk>/', OrderCreateCheckoutSessionView.as_view(),
        name='create_session_order'
    ),
    path('order/<int:order_id>/', OrderView.as_view(), name='get_order'),
]
