from django.contrib import admin
from django.urls import path
from main import views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', users_views.LoginAPIView.as_view()),
    path('api/v1/register/', users_views.RegisterAPIView.as_view()),
    path('api/v1/products/review/<int:id>/', views.ReviewAPIView.as_view()),
    path('api/v1/products/tag/<int:id>/', views.TagsAPIView.as_view()),
    path('api/v1/products/', views.ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', views.ProductDetailAPIView.as_view()),





    # path('api/v1/products/', views.product_list_view),
    # path('api/v1/products/<int:id>/', views.product_detail_view),
    # path('api/v1/products/review/', views.product_with_review_list_view),
    # path('api/v1/products/tag/', views.product_with_tag_list_view),
    # path('api/v1/login/', users_views.login),
    # path('api/v1/register/', users_views.register),
]
