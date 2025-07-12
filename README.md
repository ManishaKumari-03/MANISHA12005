# MANISHA_LMS — Learning Management System 🧠

A Django-based Learning Management System (LMS) designed and developed by **Manisha** to streamline educational workflows, manage users, and facilitate digital learning experiences. This project demonstrates the core principles of Django development, including MVC/MVT architecture, user authentication, database interaction, and modular app design.

---

## 📌 Project Overview

**MANISHA_LMS** is a full-stack web application built with Django and SQLite, intended as a robust foundation for managing courses, users, and digital content in an educational environment. It is suitable for educational institutions, trainers, or anyone looking to set up a scalable LMS solution.

---

## 🚀 Features

- ✅ User authentication and registration
- 🛠️ Admin dashboard for managing users and data
- 📚 Course and content management (extendable)
- 📦 SQLite3 database (lightweight and easy to use)
- 🧱 Modular Django app structure
- 🔐 Secure with Django’s built-in security features
- 🔗 Easily extendable to REST APIs using Django REST Framework (DRF)

---

## 👨‍💻 Developed By

**Manisha**  
Aspiring full-stack developer with a strong foundation in Python and Django. This project reflects hands-on experience with backend development and architectural design in web apps.

---

## 🧰 Tech Stack

- **Framework**: Django (Python)
- **Database**: SQLite 3
- **Frontend**: HTML/CSS (Django templates)
- **Deployment**: Localhost (can be extended to Heroku, Render, etc.)

---

## ⚙️ Installation Guide

Follow these steps to set up the project locally:

```bash
# Clone the repository
git clone h[ttps://github.com/yourusername/MANISHA_LMS.git](https://github.com/ManishaKumari-03/MANISHA12005.git)
cd MANISHA_LMS

# (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the development server
python manage.py runserver
