from . import views
from django.urls import path

urlpatterns = [
    path('', views.WhiskeyList.as_view(), name='home'),
    path('edit/<int:id>', views.EditWhiskey, name='edit'),
]
