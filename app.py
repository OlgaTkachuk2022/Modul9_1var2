from flask import Flask, request, render_template

from rates import get_rates_data, calculate_rate


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    rates_data = get_rates_data()
    if request.method == "POST":

        currency_code = request.values['currency_code']
        amount = int(request.values['amount'])
        result = calculate_rate(rates_data, currency_code, amount)
        return render_template("rates.html", rates_data=rates_data, result=result)

    return render_template("rates.html", rates_data=rates_data)


if __name__ == '__main__':
    app.run(debug=True)
