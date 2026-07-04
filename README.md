# Training Attendance Management System

A full-stack web application built with **Django** that enables organizations to digitally register participants for training sessions and manage attendance records through an organizer dashboard.

This project was developed as a real-world solution for **VONMUE QUALISAFE CONSULTING LIMITED** to manage participant registration for corporate training programs.

---

## Live Demo

🔗 https://training-attendance.onrender.com/

---

## Features

### Participant Registration
- Register participants through an intuitive online form
- Required fields:
  - Full Name
  - Designation
  - Department
  - Phone Number
  - Email Address
- Confirmation checkbox before submission
- Personalized success page after registration

### Organizer Dashboard
- Secure login for organizers
- View all registered participants
- Search participants by name
- Pagination for easy navigation
- Registration statistics

### Data Export
- Export attendance records to:
  - CSV
  - Microsoft Excel (.xlsx)

### Print Support
- Print-friendly attendance sheet
- Suitable for physical attendance verification during training

### Responsive Design
- Mobile-friendly interface
- Built with Bootstrap for a clean user experience

---

## Tech Stack

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- SQLite
- Git
- GitHub
- Render (Deployment)
- WhiteNoise (Static Files)

---

## Project Structure

```
training-attendance/
│
├── config/
├── participants/
├── static/
│   ├── css/
│   ├── img/
│   └── js/
├── templates/
├── manage.py
├── requirements.txt
└── build.sh
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/mikeisresilient/training-attendance.git
```

Navigate into the project

```bash
cd training-attendance
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Create an admin account

```bash
python manage.py createsuperuser
```

Start the development server

```bash
python manage.py runserver
```

Open your browser and visit

```
http://127.0.0.1:8000/
```

---

## Current Features

- ✅ Participant Registration
- ✅ Form Validation
- ✅ Organizer Dashboard
- ✅ Search Functionality
- ✅ Pagination
- ✅ CSV Export
- ✅ Excel Export
- ✅ Print Attendance Sheet
- ✅ Responsive Design
- ✅ Render Deployment

---

## Future Improvements

- PDF attendance reports
- Certificate generation
- Email confirmation after registration
- QR code generation from the dashboard
- Dashboard analytics
- Department-based filtering
- Custom domain integration

---

## Author

**Michael Uchechukwu Ege**

Full-Stack Web & Blockchain Developer

- GitHub: https://github.com/mikeisresilient
- X: https://x.com/mikeisresilient
---

## License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

This project was developed as a practical solution for managing participant registration and attendance during corporate training sessions conducted by **VONMUE QUALISAFE CONSULTING LIMITED**.

If you found this project helpful, consider giving it a ⭐ on GitHub.
