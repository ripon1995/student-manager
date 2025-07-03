# student-manager

project structure

```plaintext
student_manager/
├── manage.py
├── student_manager/
│   ├── settings.py
│   ├── urls.py
│   ├── templates/
│   │   └── base.html
│   ├── static/
│       ├── css/
│       ├── js/
├── student/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── student/
│   │       └── student_list.html
│   ├── urls.py
├── course/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── course/
│   │       └── course_list.html
│   ├── urls.py
├── payment/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── payment/
│   │       └── payment_list.html
│   ├── urls.py