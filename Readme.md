# Portfolio Website

A dynamic and fully manageable **portfolio website** built using **Django** and **Bootstrap 5**.

Easily showcase your **skills**, **projects**, **work history**, and **resume**, with full control through the Django admin panel — no code changes needed to update content.

## Features

- **User Authentication**: Register(Via Admin cmd), Login, Logout, Profile Update
- **Dynamic Portfolio Sections**:
  - Skills
  - Projects
  - Work History
  - Resume (upload/download)
- **Admin-Managed Content**: Manage all portfolio data directly from the Django admin panel
- **Password Management**: Change or reset passwords
- **Responsive UI**: Built with Bootstrap 5 for mobile-first design
- **Custom Admin Interface**: Easy-to-use admin to manage all sections
- **Clean Layout**: Simple and elegant template for showcasing personal brand

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5 + HTML Templates
- **Database:** SQLite (default)
- **Other:** Django Messages Framework, Static Files

## Installation Guide for Image Gallery

### 1. Clone the repository

git clone https://github.com/Darpan-Anjanay/Portfolio.git # Download the project from GitHub
cd Portfolio # Move into the project directory

### 2. Create a virtual environment

python -m venv venv # Create a virtual environment named 'venv'

### 3. Activate the virtual environment

venv\Scripts\activate # For Windows

### 4.Install the project dependencies

pip install -r requirements.txt # Install all required packages listed in requirements.txt

### 5. Set up the database

python manage.py makemigrations # Generate migration files based on the models
python manage.py migrate # Apply the migrations to create the database schema

### 6. Create a superuser for accessing the Django admin panel

python manage.py createsuperuser # Follow the prompts (username, email, password)

### 7. Run the development server

python manage.py runserver # Start the local server

### Now, open your browser and go to: http://127.0.0.1:8000/

### To access the admin panel, visit: http://127.0.0.1:8000/admin/

## Author

- **Name:** Darpan Anjanay
- **GitHub:** https://github.com/Darpan-Anjanay/

## Screenshots

### Home Page

![Register Page](/screenshots/Darpan-Anjanay-Portfolio-09-27-2025_10_34_PM.png)
