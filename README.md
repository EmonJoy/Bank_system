# Bank_system(Using Djando)

A Django-based backend system for managing bank accounts, transactions, and users.  
This project uses **PostgreSQL** as the database and is designed to be deployed on **Railway.app** for seamless cloud hosting.

---

## Features

- User registration and authentication
- Bank account creation and management
- Transaction recording with filtering and searching
- Admin panel for easy management
- Integration with PostgreSQL database on Railway
- Ready for API extension and frontend integration

## Project Structure

```text
bank_backend/
├── bank_backend/           # Main Django project settings
│   ├── settings.py         # Database & app configurations
│   ├── urls.py             # Project URL routing
│   └── wsgi.py             
├── bank/                   # Core banking app
│   ├── migrations/         # Database migration files
│   ├── models.py           # Database models (BankAccount, Transaction, etc.)
│   ├── views.py            # Views and business logic
│   ├── admin.py            # Django admin customizations
│   └── urls.py             # App-level URLs
├── manage.py               # Django CLI entry point
└── requirements.txt        # Python dependencies
```


## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database (Railway recommended for production)
- Virtual environment tool (`venv` or `virtualenv`)

---

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/EmonJoy/Bank_system.git
   cd Bank_system/bank_backend

python -m venv env
source env/bin/activate        # On Windows use: env\Scripts\activate
## Configure the database connection:(settings.py)
'''text
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your_db_name>',
        'USER': '<your_db_user>',
        'PASSWORD': '<your_db_password>',
        'HOST': '<your_db_host>',
        'PORT': '<your_db_port>',
    }
}
'''



### Apply database migrations, Create a superuser (admin), Run the development server..




