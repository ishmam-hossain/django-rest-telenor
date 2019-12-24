from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ValuesAPIView(APIView):
    def get(self, request):
        return Response({"ok": 1}, status=status.HTTP_200_OK)
