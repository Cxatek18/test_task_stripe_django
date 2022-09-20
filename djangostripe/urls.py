from django.contrib import admin
from django.urls import path, include


handler404 = "stripe_app.views.handling_error_404"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stripe_app.urls'))
]
