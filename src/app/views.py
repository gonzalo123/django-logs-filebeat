import logging

from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class Debug(APIView):

    def get(self, request):
        logger.debug("This is debug message", extra={'extraParam': 'Gonzalo'})

        return Response(data={'debug', 'hello'})


class Error(APIView):

    def get(self, request):
        logger.error("This is error message")

        return Response(data={'error', 'hello'})


class Info(APIView):

    def get(self, request):
        logger.info("This is info message")

        return Response(data={'info', 'hello'})
