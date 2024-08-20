from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from courses.views import ProductViewSet, SubscriptionViewSet, UserBalanceViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'balances', UserBalanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
