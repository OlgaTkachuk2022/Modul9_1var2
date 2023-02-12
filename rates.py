import requests

SEPARATOR = ';'


def create_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()

    rates: list[dict] = data[0]['rates']

    col_names = ['currency', 'code', 'bid', 'ask']

    csv_result = SEPARATOR.join(col_names) + '\n'
    for rate in rates:
        csv_result += SEPARATOR.join([str(value) for value in rate.values()]) + '\n'

    with open('result.csv', 'w') as f:
        f.write(csv_result)


def get_rates_data():
    with open('result.csv', 'r') as f:
        data = f.readlines()
    data = data[1:]  # skip column names
    result = []
    for row in data:
        row_values = row.split(SEPARATOR)
        result.append({
            'currency': row_values[0],
            'code': row_values[1],
            'bid': row_values[2],
            'ask': row_values[3],
        })
    return result

def calculate_rate(currency_data, code, amount):
    required_currency = list(filter(lambda item: item['code'] == code, currency_data))[0]
    return float(required_currency['bid']) * amount


if __name__ == '__main__':
    create_rates()
