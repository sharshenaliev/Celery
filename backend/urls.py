from django.urls import path, include
from backend.views import *
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('establishment', EstablishmentViewSet, basename='establishment')

urlpatterns = [
    path('login/', token_obtain_pair, name='token_obtain_pair'),
    path('token/refresh/', token_refresh, name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('user/', UserView.as_view()),
    path('', include(router.urls)),
]
