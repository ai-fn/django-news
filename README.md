# Django News Blog

Django News Blog is a web application that allows users to read, publish, and organize news articles. 

## Features

- User registration and login
- CKEditor for easy and rich content editing
- Debug toolbar for development and debugging
- Send feedback by email with captcha security
- Categorize news articles for easy navigation
- Integration with Django cache for improved performance

## Requirements

- Python 3.x
- Django 3.x
- CKEditor
- Django Debug Toolbar
- Django Simple Captcha

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ai-fn/django-news.git
```

2. Navigate to the project directory:
```bash
cd django-news
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
- Update the database configuration in the `settings.py` file.
- Create the database migrations:
```python
python manage.py makemigrations
```
- Run the database migrations:
```python
python manage.py migrate
```

5. Start the development server:
```python
python manage.py runserver
```

6. Open your browser and visit `http://localhost:8000` to access the application.

## Usage

1. Register a new user account on the registration page.
2. Log in with your credentials on the login page.
3. Create, edit, or delete news articles using the CKEditor-powered editor.
4. Categorize news articles by assigning categories to them.
5. View and navigate news articles by category or search for specific articles.
6. Provide feedback to the site administrators using the feedback form with captcha security.
7. Monitor and debug application behavior using the debug toolbar during development.
8. Enjoy reading and sharing news articles with others.

For any questions or inquiries, please reach out to [isapsanov@list.ru](mailto:isapsanov@list.ru).

Happy blogging!
