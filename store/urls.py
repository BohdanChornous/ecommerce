from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
    path('priduct/<slug:slug>/', views.SingleProductView.as_view(), name='product-info'),
    path('search/<slug:slug>', views.CategoriesView.as_view(), name='search-info'),
]
