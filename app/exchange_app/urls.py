from django.urls import path
from . import views
from .views import exchange

urlpatterns = [
    path('', exchange),
    path('journal/', views.journal, name = "journal.html"),
]