import csv
import sys
import calendar
from collections import defaultdict


def parse_csv(input_stream):
    expenses = defaultdict(int)
    reader = csv.DictReader(input_stream, delimiter=';')

    for row in reader:
        department = row.get('Department', '')
        year = row.get('Year', '')
        for month in range(1, 13):
            month_name = calendar.month_abbr[month]

            if month_name in row:
                expense_str = row[month_name].replace('$', '').replace(',', '').replace('(', '').replace(')', '')
                expenses[(department, year, month_name)] += int(expense_str)

    return expenses


def extract_unique_years(input_stream):
    unique_years = set()
    reader = csv.DictReader(input_stream, delimiter=';')
    for row in reader:
        year = row['Year']
        unique_years.add(year)
    return unique_years


def extract_unique_months(input_stream):
    unique_months = set()
    reader = csv.DictReader(input_stream, delimiter=';')
    for row in reader:
        for month_name in calendar.month_abbr[1:]:
            if row[month_name]:
                unique_months.add(month_name)
    return unique_months


def _is_matching_department(dept, department):
    return dept == department


def _is_matching_year(yr, year):
    return year is None or yr == year


def _calculate_quarter(period):
    return (list(calendar.month_abbr).index(period) - 1) // 3 + 1


def _is_matching_time(period, time):
    if not time:
        return True
    if time.isdigit():
        return int(time) == _calculate_quarter(period)
    return period.lower() == time.lower()


def aggregate_expenses(expenses, department, year=None, time=None):
    total = sum(value for (dept, yr, period), value in expenses.items() if
                _is_matching_department(dept, department) and _is_matching_year(yr, year) and _is_matching_time(period, time))
    return f"${total:.2f}"


def parse_input(arguments):
    if len(arguments) >= 2:
        return arguments[1], arguments[2] if len(arguments) >= 3 else None, arguments[3] if len(arguments) >= 4 else None
    else:
        return None, None, None


def print_total_expenses(total_expenses, department, year=None, time=None):
    if year:
        if time:
            if time.isdigit():
                quarter_names = ["First", "Second", "Third", "Fourth"]
                print(f"Total expenses for department '{department}' in {quarter_names[int(time)-1]} "
                      f"quarter of {year}: {total_expenses}")
            else:
                print(f"Total expenses for department '{department}' in {time} of {year}: {total_expenses}")
        else:
            print(f"Total expenses for department '{department}' in {year}: {total_expenses}")
    else:
        print(f"Total expenses for department '{department}': {total_expenses}")


if __name__ == "__main__":
    department, year, time = parse_input(sys.argv)

    if department:
        with sys.stdin as input_stream:
            expenses_data = parse_csv(input_stream)
        total_expenses = aggregate_expenses(expenses_data, department, year, time)
        print_total_expenses(total_expenses, department, year, time)
    else:
        print("Usage: cat <expense file> | python main.py <department> <year> <month/quarter>")
