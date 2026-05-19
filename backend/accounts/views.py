from rest_framework.permissions import IsAuthenticated
from rest_framework.response import (
    Response,
)  # Similar to Django's HttpResponse. Can return Python data like

# dictionaries/lists, and DRF turns it into JSON.
from rest_framework.views import APIView

from accounts.serializers import UserSerializer


class CurrentUserView(APIView):
    permission_classes = [
        IsAuthenticated
    ]  # IsAuthenticated = only authenticated users can access the view (in our
    # case, a valid JWT token is included in the request. It is used before get() runs. Used by the APIView class
    # under the hood so we don't have to do conditional logic.

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
