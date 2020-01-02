from django.urls import path
import Product.views

from.views import ProductDetail,ProductList,CarttList,CarttDetail

urlpatterns=[
    path('<int:pk>/', ProductDetail.as_view()),
    path('', ProductList.as_view()),
]
