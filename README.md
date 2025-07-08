# student-manager

project structure

```plaintext
student_manager/
├── manage.py
├── student_manager/
│   ├── management/
│   │   ├── __init__.py
│       ├── commands/
│       │   ├── __init__.py
│       │   ├── createinitialsuperuser.py
│   ├── settings.py
│   ├── urls.py
│   ├── static/
│       ├── css/
│       ├── js/
├── dashboard/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── base.html
│   ├── urls.py
├── course/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── student/
│   ├── models.py
│   ├── views.py
│   ├── urls.py