from rest_framework import serializers


class ConversionSerializer(serializers.Serializer):
    """Serializes conversion request"""
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)
    value = serializers.DecimalField(max_digits=20, decimal_places=10)

    