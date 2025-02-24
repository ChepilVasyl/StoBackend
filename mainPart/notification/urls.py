from .views import Main
from django.urls import path

urlpatterns = [
    path('created/',Main.as_view()),
    path('all_items/',Main.as_view()),
    path('delete/',Main.as_view()),
    path('update/',Main.as_view())
]