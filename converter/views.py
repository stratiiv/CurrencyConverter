from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .serializers import ConversionSerializer
from .services import check_query_params, convert_currency 


class CurrencyConversionView(APIView):
    def get(self, request):
        from_currency = request.query_params.get("from")
        to_currency = request.query_params.get("to")
        amount = request.query_params.get("amount")
        if not check_query_params(from_currency, to_currency, amount):
            raise serializers.ValidationError("Required parameters "
                                               "are missing.")
        data = {
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount
        }
        serializer = ConversionSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        from_currency = serializer.validated_data['from_currency']
        to_currency = serializer.validated_data['to_currency']
        amount = serializer.validated_data['amount']
        converted_amount, exchange_rate = convert_currency(from_currency,
                                                           to_currency,
                                                           amount)
        return Response({"to_currency": to_currency,
                         "value": converted_amount,
                         "exchange_rate": exchange_rate})
        