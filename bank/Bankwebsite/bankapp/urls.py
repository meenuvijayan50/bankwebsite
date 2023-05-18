from .import views
from django.urls import path

app_name='bankapp'

urlpatterns = [
    path('',views.demo,name="demo"),
    path('log', views.log, name="log"),
    path('register', views.register, name="register"),
    path('person_create_view', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='load_cities'),  # AJAX
 ]
