from rest_framework import serializers

from api.models import LinkShortener


class ShortenLinkSerializer(serializers.ModelSerializer):
    link_to_shorten = serializers.CharField()

    class Meta:
        model = LinkShortener
        fields = (
            'link_to_shorten',
        )
