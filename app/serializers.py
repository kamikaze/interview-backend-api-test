from rest_framework import serializers

from app.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    @staticmethod
    def validate_type(value):
        if value not in Event.EVENT_TYPES:
            raise serializers.ValidationError(f'Select a valid choice. {value} is not one of the available choices.')

        return value


class FilterSerializer(serializers.Serializer):
    type = serializers.CharField(required=False)

    @staticmethod
    def validate_type(value):
        if value not in Event.EVENT_TYPES:
            raise serializers.ValidationError(f'Select a valid choice. {value} is not one of the available choices.')

        return value
