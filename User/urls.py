from django.urls import path,include

from .views import(
	registration_view,

)


app_name = 'User'

urlpatterns = [
	path('register', registration_view, name="register"),
	path('product/',include('Product.urls'), name="product"),
]
