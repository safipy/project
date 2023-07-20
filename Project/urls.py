from django.urls import path
from exem import views

urlpatterns = [
    path('exem/', views.ExemListCreateAPIView.as_view()),
    path('exem/<int:id_exem>/', views.ExemDeteilAPIView.as_view()),
]