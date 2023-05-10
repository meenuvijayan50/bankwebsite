from .import views
from django.urls import path
app_name='bank'

urlpatterns = [
    path('',views.demo,name="demo"),

    path('login', views.login, name="login"),
    path('register', views.register, name="register"),


    path('add_user', views.add_user, name='add_user'),
    # path('<int:pk>/', views.UserUpdateView.as_view(), name='person_change'),

    path('load_branches/', views.userform, name='load_branches'),
    # path('submit', views.register, name="submit"),

]