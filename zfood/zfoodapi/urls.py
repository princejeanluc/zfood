from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup_view"),
    path("auth/", views.auth_view, name="auth_view"),
    path("user/get/", views.getUserDetails, name=""),
    path("store/", views.getAllStore, name=""),
    path("product/", views.getAllProduct, name=""),
    path("productFromStore/<int:store_id>", views.getProductFromStore, name=""),

]

