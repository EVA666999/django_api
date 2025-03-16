from django.urls import re_path

from .consumers import OrderConsumer, CategoryConsumer, ProductConsumer

websocket_urlpatterns = [
    re_path(r"ws/orders/$", OrderConsumer.as_asgi()),
    re_path(r'ws/categories/$', CategoryConsumer.as_asgi()),  # Добавь этот маршрут
    re_path(r'ws/products/$', ProductConsumer.as_asgi()),  # Добавь этот маршрут
]
