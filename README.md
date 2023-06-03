# Currency Converter

This project is a currency converter REST API that allows users to convert between different currencies.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install `pipenv` if you haven't already:
```bash
pip install pipenv
```
4. Install the project dependencies using pipenv:
```bash
pipenv install
```
5. Launch the virtual environment:
```bash
pipenv shell
```
6. Run the application using:
```bash
python manage.py runserver
```

## Usage

Send GET request by browser/postman/curl 
```shell
http://127.0.0.1:8000/convert/?from={CURRENCY}&to={CURRENCY}&amount={AMOUNT}
```
Make sure to replace with your values.

Allowed currencies are USD, EUR, GBP, UAH.

Example:
```shell
http://127.0.0.1:8000/convert/?from=USD&to=UAH&amount=50
```
```json
{
    "currency": "UAH",
    "value": 1846.9508,
    "exchange_rate": 36.939016
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)