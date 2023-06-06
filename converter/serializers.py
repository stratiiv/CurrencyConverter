from rest_framework import serializers


ALLOWED_CURRENCIES = ("USD", "EUR", "GBP", "UAH")


class ConversionSerializer(serializers.Serializer):
    """Serializes conversion request"""
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)
    amount = serializers.DecimalField(max_digits=20, decimal_places=6)

    def validate(self, data):
        """Check if currency is in allowed list"""
        check_list = data["from_currency"], data["to_currency"]
        if not all(currency in ALLOWED_CURRENCIES for currency in check_list):
            raise serializers.ValidationError("Please choose currency from "
                                            f"{', '.join(ALLOWED_CURRENCIES)}")
        return data

    def validate_amount(self, value):
        """Check if currency is positive number"""
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive number")
        return value
