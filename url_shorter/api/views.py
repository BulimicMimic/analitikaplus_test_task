import os

# from dotenv import load_dotenv
from secrets import token_urlsafe

from django.shortcuts import redirect, get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.models import LinkShortener
from .serializers import ShortenLinkSerializer

# load_dotenv()

DOMAIN_NAME = os.getenv('DOMAIN_NAME')

class ShortenLink(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ShortenLinkSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        link_to_shorten = serializer.validated_data['link_to_shorten']
        link, created = LinkShortener.objects.get_or_create(
            link_to_shorten=link_to_shorten,
        )
        if created:
            random_link = token_urlsafe(16)
            while LinkShortener.objects.filter(short_link=random_link).exists():
                random_link = token_urlsafe(16)
            link.short_link = random_link
            link.save()

        short_link = 'http://localhost:8000/api/' + link.short_link
        link_data = {
            'short_link': short_link,
            'link_to_shorten': link_to_shorten,
        }
        return Response(link_data,
                        status=status.HTTP_200_OK,
                        headers=headers,
                        )


def redirect_link(request, short_link):
    link = get_object_or_404(LinkShortener, short_link=short_link)
    return redirect(link.link_to_shorten)
