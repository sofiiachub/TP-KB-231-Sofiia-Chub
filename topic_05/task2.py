import requests

value = float(input("Enter the amount of currency: "))
currency = input("Enter the currency type (EUR, USD, PLN): ").upper()

r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

eurCurr = 0

for elem in r.json():
    if elem['cc'] == currency:
        eurCurr = elem['rate']
        print(f"Result: {value} {currency} = {eurCurr*value:.2f} UAH")
        break
else:
    print(f"Exchange rate for currency {currency} not found")