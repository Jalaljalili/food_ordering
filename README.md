# Food Ordering Website

This is a simple food ordering website built with Django. The application allows an admin to import menus of weekly food from Saturday to Wednesday, and clients can select their food for each day. The admin can then export the order list to an Excel file.

## Features

- Admin can create usernames and passwords for clients.
- Clients can select one food item for each day and cannot change it once selected.
- Admin can export the orders to an Excel file.

## Requirements

- Python 3.6+
- Django 3.2+
- Openpyxl (for exporting to Excel)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Jalaljalili/food_ordering.git
    cd food-ordering-website
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup the database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    - Admin panel: `http://127.0.0.1:8000/admin`
    - Client ordering: `http://127.0.0.1:8000/order`

## Usage

### Admin

1. **Login to the admin panel**.
2. **Create Menu items** for each day of the week.
3. **Create user accounts** for clients.
4. **Export orders** to an Excel file by visiting `http://127.0.0.1:8000/export_orders`.

### Client

1. **Login** with the credentials provided by the admin.
2. **Select food items** for each day from Saturday to Wednesday.
3. **Submit** the order.

## Project Structure
```
food-ordering-website/
│
├── FoodOrderingProject/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── foodorder/
│ ├── migrations/
│ ├── templates/
│ │ ├── order_food.html
│ │ └── order_success.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
│
├── manage.py
└── requirements.txt
```

## Dependencies

- Django
- Openpyxl

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


