from django.urls import path,include

from .views import(
	registration_view,

)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'User'

urlpatterns = [
	path('register', registration_view, name="register"),
	path('login',obtain_auth_token, name="login"),
	path('product/',include('Product.urls'), name="product"),
]
