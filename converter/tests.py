import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def conversion_url():
    return reverse('convert')


def test_conversion_sucessful(api_client, conversion_url):
    data = {'from': 'USD', 'to': 'UAH', 'amount': 100}
    response = api_client.get(conversion_url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['currency'] == 'UAH'
    assert 'value' in response.data
    assert 'exchange_rate' in response.data


def test_conversion_missing_parameters(api_client, conversion_url):
    data = {'from': 'USD', 'amount': '100'}
    response = api_client.get(conversion_url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_conversion_negative_amount(api_client, conversion_url):
    data = {'from': 'USD', 'to': 'UAH', 'amount': '-100'}
    response = api_client.get(conversion_url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_conversion_not_supported_currency(api_client, conversion_url):
    data = {'from': 'DKK', 'to': 'UAH', 'amount': '100'}
    response = api_client.get(conversion_url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
