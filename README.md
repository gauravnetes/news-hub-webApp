# Django Project Setup

This guide provides step-by-step instructions to set up the Django project on your local machine.

## Prerequisites

Make sure you have the following installed:
- Python (>= 3.8)
- Git
- Virtual environment (venv)

---

## 1️⃣ Clone the Repository

```bash
# Clone the repo from GitHub
git clone https://github.com/yourusername/your-django-project.git

# Navigate into the project directory
cd your-django-project
```

---

## 2️⃣ Create & Activate Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (MacOS/Linux)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
If `requirements.txt` is not available, install dependencies manually:
```bash
pip install django python-dotenv
```

---

## 4️⃣ Set Up Environment Variables

1. Create a `.env` file in the project root.
2. Add the required environment variables:
   ```ini
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   ````

---

## 5️⃣ Run Migrations & Create Superuser

```bash
# Apply database migrations
python manage.py migrate

# Create an admin superuser (optional)
python manage.py createsuperuser
```

---

## 6️⃣ Run the Django Server

```bash
python manage.py runserver
```
Now, open your browser and visit:
```
http://127.0.0.1:8000/
```

---

## 7️⃣ (Optional) Collect Static Files

```bash
python manage.py collectstatic
```

---

## 8️⃣ Deactivate Virtual Environment (When Done)

```bash
deactivate
```

---

## 🚀 Deployment
For deploying on **PythonAnywhere**, follow the [PythonAnywhere Deployment Guide](https://www.pythonanywhere.com/).

---

## 🤝 Contributing
Feel free to contribute! Open an issue or submit a pull request.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

Happy Coding! 🚀

