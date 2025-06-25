from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LanguagePreference
from .serializers import LanguagePreferenceSerializer

class SetLanguageAPIView(APIView):
    def post(self, request):
        session_id = request.data.get('session_id')
        language = request.data.get('language')

        if not session_id or not language:
            return Response({"error": "session_id and language required"}, status=400)

        obj, created = LanguagePreference.objects.update_or_create(
            session_id=session_id,
            defaults={'language': language}
        )
        return Response({"message": "Language set", "language": obj.language})

    def get(self, request):
        session_id = request.query_params.get('session_id')
        if not session_id:
            return Response({"error": "session_id required"}, status=400)

        try:
            obj = LanguagePreference.objects.get(session_id=session_id)
            return Response({"language": obj.language})
        except LanguagePreference.DoesNotExist:
            return Response({"language": "ru"})