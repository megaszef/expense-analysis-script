# Expense Analysis Script

This Python script is designed to analyze expense data stored in a CSV file. It allows users to aggregate expenses based on department, year, and month/quarter.

## Prerequisites

- Python 3.9
- `requirements.txt`

## Setup

To use the script, follow these steps:

1. Clone the repository to your local machine:
```
git clone https://github.com/megaszef/expense-analysis-script.git
cd expense-analysis-script
```

2. Create venv and install prerequisites:
``` 
python -m venv venv
python -m pip install -r requirements.txt
```

3. Prepare your expense data in a CSV file with the following format:
``` 
Department;Expense Type;Year;Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec
```

## Usage Cli

Run the script using the following command:

- *Note:* Year and Month/Quarter is optional. You can use that to specify you search
```
cat <expense-file>.csv | python main.py <department> <year> <month/quarter>
```

## Usage Web

Run the web server using following commands:

1. Start the app:
``` 
python api\api.py
```

2. Go to the specified ip address.
*Default:* [127.0.0.1:5000](http://127.0.0.1:5000/)
