from django.urls import path

from accounts.views import CurrentUserView

urlpatterns = [path("me/", CurrentUserView.as_view())]
