from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('product-list/', views.showAll, name='product-list'),
    path('product-detail/<int:id>', views.viewProduct, name='product-detail'),
    path('product-create/', views.createProduct, name='product-create'),
    path('product-update/<int:id>', views.updateProduct, name='product-update'),
    path('product-delete/<int:id>', views.deleteProduct, name='product-delete'),

]