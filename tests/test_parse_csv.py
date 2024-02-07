import pytest
import io
import main


@pytest.mark.parametrize("input_stream,expected_result", [
    (
        [
            'Department;Year;Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec',
            'Sales;2022;$1000;$2000;$3000;$4000;$5000;$6000;$7000;$8000;$9000;$10000;$11000;$12000',
            'Sales;2023;$1500;$2500;$3500;$4500;$5500;$6500;$7500;$8500;$9500;$10500;$11500;$12500',
            'Marketing;2022;$1200;$2200;$3200;$4200;$5200;$6200;$7200;$8200;$9200;$10200;$11200;$12200',
            'Marketing;2023;$1700;$2700;$3700;$4700;$5700;$6700;$7700;$8700;$9700;$10700;$11700;$12700'
        ],
        {
            ('Sales', '2022', 'Jan'): 1000, ('Sales', '2022', 'Feb'): 2000, ('Sales', '2022', 'Mar'): 3000,
            ('Sales', '2022', 'Apr'): 4000, ('Sales', '2022', 'May'): 5000, ('Sales', '2022', 'Jun'): 6000,
            ('Sales', '2022', 'Jul'): 7000, ('Sales', '2022', 'Aug'): 8000, ('Sales', '2022', 'Sep'): 9000,
            ('Sales', '2022', 'Oct'): 10000, ('Sales', '2022', 'Nov'): 11000, ('Sales', '2022', 'Dec'): 12000,
            ('Sales', '2023', 'Jan'): 1500, ('Sales', '2023', 'Feb'): 2500, ('Sales', '2023', 'Mar'): 3500,
            ('Sales', '2023', 'Apr'): 4500, ('Sales', '2023', 'May'): 5500, ('Sales', '2023', 'Jun'): 6500,
            ('Sales', '2023', 'Jul'): 7500, ('Sales', '2023', 'Aug'): 8500, ('Sales', '2023', 'Sep'): 9500,
            ('Sales', '2023', 'Oct'): 10500, ('Sales', '2023', 'Nov'): 11500, ('Sales', '2023', 'Dec'): 12500,
            ('Marketing', '2022', 'Jan'): 1200, ('Marketing', '2022', 'Feb'): 2200, ('Marketing', '2022', 'Mar'): 3200,
            ('Marketing', '2022', 'Apr'): 4200, ('Marketing', '2022', 'May'): 5200, ('Marketing', '2022', 'Jun'): 6200,
            ('Marketing', '2022', 'Jul'): 7200, ('Marketing', '2022', 'Aug'): 8200, ('Marketing', '2022', 'Sep'): 9200,
            ('Marketing', '2022', 'Oct'): 10200, ('Marketing', '2022', 'Nov'): 11200, ('Marketing', '2022', 'Dec'): 12200,
            ('Marketing', '2023', 'Jan'): 1700, ('Marketing', '2023', 'Feb'): 2700, ('Marketing', '2023', 'Mar'): 3700,
            ('Marketing', '2023', 'Apr'): 4700, ('Marketing', '2023', 'May'): 5700, ('Marketing', '2023', 'Jun'): 6700,
            ('Marketing', '2023', 'Jul'): 7700, ('Marketing', '2023', 'Aug'): 8700, ('Marketing', '2023', 'Sep'): 9700,
            ('Marketing', '2023', 'Oct'): 10700, ('Marketing', '2023', 'Nov'): 11700, ('Marketing', '2023', 'Dec'): 12700
        }
    ),
])
def test_parse_csv_good_input(input_stream, expected_result):
    input_file = io.StringIO('\n'.join(input_stream))

    result = main.parse_csv(input_file)

    assert result == expected_result


def test_parse_csv_with_missing_month_header():
    input_stream = [
        'Department;Year;Jan;Feb;Mar;',
        'Sales;2022;$1000;$2000;$3000;$4000;'
    ]

    expected_result = {
        ('Sales', '2022', 'Jan'): 1000,
        ('Sales', '2022', 'Feb'): 2000,
        ('Sales', '2022', 'Mar'): 3000,
    }

    input_file = io.StringIO('\n'.join(input_stream))

    result = main.parse_csv(input_file)

    assert result == expected_result
