from flask import Flask, render_template, request, jsonify
from main import parse_csv, aggregate_expenses, extract_unique_years, extract_unique_months
from const import data_path

app = Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate-expenses', methods=['GET'])
def calculate_expenses():
    print("Request Args:", request.args)
    department = request.args.get('department')
    year = request.args.get('year')
    month = request.args.get('month')

    print("Department:", department)
    print("Year:", year)
    print("Month:", month)

    with open(data_path, 'r') as file:
        expenses_data = parse_csv(file)

    if year == '':
        year = None
    if month == '':
        month = None

    total_expenses = aggregate_expenses(expenses_data, department, year, month)

    print("Total Expenses:", total_expenses)

    return render_template('results.html', department=department, year=year, month=month, total_expenses=total_expenses)


@app.route('/get-unique-years', methods=['GET'])
def get_unique_years():
    with open(data_path, 'r') as file:
        unique_years = extract_unique_years(file)

    return jsonify(list(unique_years))


@app.route('/get-unique-months', methods=['GET'])
def get_unique_months():
    with open(data_path, 'r') as file:
        unique_months = extract_unique_months(file)

    return jsonify(list(unique_months))


if __name__ == '__main__':
    app.run(debug=True)
