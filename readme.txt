QUICK START — Axis & Arbor Online Store

1. Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Add .env File

Create a .env in the project root with:

DEBUG=True
SECRET_KEY=your_secret_key_here

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email_here
EMAIL_HOST_PASSWORD=your_email_password_here

4. Apply Migrations
python manage.py migrate

5. Create Admin User (Optional)
python manage.py createsuperuser

6. Run the Server
python manage.py runserver


Then visit:
http://127.0.0.1:8000

7. Features

User accounts & authentication

Product browsing & cart system

Contact form with email

Blog with comments

Custom woodworking & 3D printing pages