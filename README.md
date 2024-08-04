# Hospital Information Management System

## Overview

This project is a Hospital Information Management System (HIMS) developed using Python and MySQL, with a web interface built using Streamlit. The system is designed to manage various hospital operations, including patient records, doctor information, room assignments, tests, and guardian details.

## Features

- **Doctor Management**: Manage doctor details, including their degrees and specializations.
- **Patient Management**: Keep track of patient information and their treatments.
- **Room Assignments**: Assign and manage patient rooms.
- **Test Records**: Record and manage tests conducted on patients.
- **Guardian Information**: Maintain details of patients' guardians.

## Technology Stack

- **Backend**: Python
- **Database**: MySQL
- **Web Interface**: Streamlit

## Installation

### Prerequisites

- Python 3.8+
- MySQL Server
- Streamlit

### Step-by-Step Guide

1. **Set Up the MySQL Database**:
    - Create a database in MySQL.
    - Run the SQL script `schema.sql` to create the necessary tables.
    - Update the database configuration in the `config.py` file with your MySQL credentials.

2. **Install Python Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Streamlit Application**:
    ```sh
    streamlit run app.py
    ```

 Usage

1. Launching the App:
    - Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

2. Navigating the Interface:
    - Use the sidebar to navigate between different sections: Doctors, Patients, Room Assignments, Tests, and Guardians.
    - Fill out forms and submit to add or update records.

 Project Structure

```plaintext
hospital-information-management-system/
│
├── app.py                # Main Streamlit application file
├── config.py             # Database configuration
├── requirements.txt      # List of Python dependencies
├── schema.sql            # SQL script to create database tables
├── README.md             # Project readme file
└── ...                   # Additional files and directories
```

 Database Schema

 Tables

- Doctor: Stores doctor details.
- Doctor_degree: Stores degrees and specializations of doctors.
- treat_patient: Links doctors with patients they are treating.
- assign_room: Manages room assignments for patients.
- Test: Stores test details and results.
- record: Stores medical records of patients.
- Has_Guardian: Stores details of patients' guardians.

---

Feel free to reach out with any questions or feedback!

---
Happy Coding!
