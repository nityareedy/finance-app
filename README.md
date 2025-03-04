# Finance Management App

A modern web application for managing personal finances. Track your income and expenses, categorize transactions, and monitor your financial health.

## Features

- User authentication (register/login)
- Add, edit, and delete transactions
- Categorize transactions (income/expense)
- View financial summary (total income, expenses, and balance)
- Recent transactions list
- Responsive design
- Modern UI with Bootstrap 5

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd finance-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Running the Application

1. Set the Flask environment variables:
```bash
export FLASK_APP=finance_app
export FLASK_ENV=development
```

2. Run the application:
```bash
flask run
```

3. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Register a new account or login with existing credentials
2. Add transactions (income or expenses) with descriptions and categories
3. View your financial summary on the dashboard
4. Edit or delete transactions as needed
5. Monitor your spending patterns and financial health

## Security Notes

- Change the `SECRET_KEY` in `config.py` before deploying to production
- Use environment variables for sensitive information
- Implement proper password hashing (already included)
- Use HTTPS in production

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 