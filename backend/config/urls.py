from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import EmailTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", EmailTokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/accounts/", include("accounts.urls")),
    path("api/", include("promotions.urls")),
]
