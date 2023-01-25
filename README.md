## Django Backend With HTMX
***An SPA simple alternative to ReactJS and Vue based on HTML principles***

This Library HTMX at https://htmx.org is useful for creating responsive frontend SPAs like ReactJS that can possibly power a SaaS app. Awesome!
Follow HTMX vs ReactJS argument here at Hackernews https://news.ycombinator.com/item?id=33218439

AM currently building an enterprise level web app to test out this Library.
This is a hobbydev Contact List App to see how it works

git clone 'https://github.com/exceptionalvic/Django-plus-HTMX.git'

1. Create a virtual env and activate
2. Install the requirements using pip install -r requirements.txt
3. Run migrations with python manage.py makemigrations and python manage.py migrate
4. start django development server using python manage.py runserver
5. navigate to http://127.0.0.1:8000/contacts/ and add new contacts, delete contacts and see HTMX awesomeness