from django.urls import path
from . import views

urlpatterns = [



    # SB admin 2 urls
    path('dash/', TemplateView.as_view(template_name='dashboard.html')), 

    # API urls
    path('room_types/', views.RoomTypeView.as_view()),
    path('rooms/', views.RoomView.as_view()),
    path('guests/', views.GuestView.as_view()),
]