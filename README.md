# Student Management System

A Python web application for managing student records with SQL database backend.

## Features
- Add, view, update, and delete student records
- Web interface with HTML templates
- SQL database integration
- JSON data import/export capability

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mahesh0842/API-PROJECT.git
cd API-PROJECT
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
sqlite3 students.db < students.sql
```

## Usage

Run the application:
```bash
python view.py
```

Then open http://localhost:5000 in your browser.

## Project Structure

```
SQL/
├── templates/               # HTML templates
│   ├── delete_student.html
│   ├── form.html
│   ├── index.html
│   ├── update_student.html
│   └── view_students.html
├── db_connection.py         # Database connection handler
├── Fetch.py                 # Data retrieval functions
├── form_data.py             # Form handling
├── insert.py                # Data insertion functions
├── LICENSE                  # Project license
├── requirements.txt         # Python dependencies
├── show.py                  # Display functions
├── students_details.json    # Sample student data
├── students.sql             # Database schema
├── style.css                # Stylesheet
└── view.py                  # Main application entry point
```

## Dependencies

See [requirements.txt](requirements.txt) for complete list.

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.
