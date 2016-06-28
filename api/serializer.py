from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class FacebookSerializer(serializers.Serializer):
    class Meta:
        model = Facebook
        fields = ('name', 'start_time', 'place', 'source')

    def create(self, validated_data):
        return Facebook.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instace.start_time = validated_data.get('start_time', instance.start_time)
        instace.place = validated_data.get('place', instance.place)
        instace.source = validated_data.get('source', instance.source)
        instance.save()
        return instance
