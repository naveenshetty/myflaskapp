# README

## Exam System Integration and Student Web Processing

This project implements an integration between the Exam System and the Student Web to retrieve exam results and calculate key metrics such as the average grade and total approved credits. The project includes a backend API built with Flask, processing utilities, and testing mechanisms to ensure correctness and reliability.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies and Frameworks](#technologies-and-frameworks)
- [Libraries Used](#libraries-used)
- [Installation and Setup](#installation-and-setup)
- [File Structure](#file-structure)
- [How to Run](#how-to-run)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)

---

## Project Overview

### Problem Statement:
Ole, a student, needs his exam results integrated into the Student Web. Additionally, the system should calculate his average grade and the total approved credits (only for exams passed with a grade better than F). This project achieves this through data integration, processing, and providing a web interface to display the results.

### Features:
1. Fetch exam data from the Exam System API.
2. Transform and process the fetched data to meet the requirements of the Student Web.
3. Calculate average grade and approved credits.
4. Render results on a web frontend using Flask.
5. Includes robust error handling and testing.

---

## Technologies and Frameworks

### Flask:
- **Why Used**: Flask was chosen for its lightweight nature and simplicity, ideal for creating small-to-medium web applications with flexible extensions.

### dotenv:
- **Why Used**: Used for environment variable management, ensuring sensitive information like API URLs is stored securely in a `.env` file.

### requests:
- **Why Used**: Simplifies HTTP requests and interactions with external APIs (GET and POST operations).

### unittest:
- **Why Used**: For testing utility functions and verifying the correctness of the application's core logic.

---

## Libraries Used

| **Library** | **Purpose** | **Justification** |
|-------------|-------------|--------------------|
| `Flask` | Web framework | Provides the core framework for defining routes and rendering templates. |
| `dotenv` | Environment management | Ensures secure storage and access to sensitive API URLs. |
| `requests` | HTTP requests | Simplifies integration with the Exam System and Student Web APIs. |
| `unittest` | Testing framework | Ensures utility functions and data transformations are tested thoroughly. |
| `logging` | Error tracking and debugging | Enables efficient error handling and logging during runtime. |

---

## Installation and Setup

### Prerequisites:
- Python 3.7 or higher
- pip (Python package manager)
- .env file containing the following keys:
  ```env
  EXAM_SYSTEM_API=<Exam System API URL>
  STUDENT_WEB_API=<Student Web API URL>
  ```

### Steps:
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python run.py
   ```

---

## File Structure

```plaintext
my_flask_app/
  app/
    templates/
      index.html        # HTML file for rendering the results
    __init__.py         # Initializes the Flask app
    routes.py           # Flask routes handling HTTP requests
    utils.py            # Contains core utility functions for data processing
  test/
    TestExamSystem.py   # Unit tests for utility functions
  run.py                # Entry point for running the Flask app
  .env                  # Environment variables (not included in version control)
  requirements.txt      # List of project dependencies
```

---

## How to Run

1. Start the Flask application using the `run.py` file:
   ```bash
   python run.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
3. The homepage will display the student data, including average grade and approved credits.

---

## API Documentation

### Exam System API (GET):
- **Endpoint**: Defined in `EXAM_SYSTEM_API` environment variable
- **Response Example**:
  ```json
  [
    {
      "COURSE": "TMA4105",
      "CREDITS": "7.5",
      "FIRSTNAME": "BRYNJAR",
      "GRADE": "5",
      "LASTNAME": "ENGELSEN",
      "ROOOM": "A1-201",
      "STUDENTID": 1337
    }
  ]
  ```

### Student Web API (POST):
- **Endpoint**: Defined in `STUDENT_WEB_API` environment variable
- **Payload Example**:
  ```json
  [
    {
      "id": 1337,
      "name": "BRYNJAR ENGELSEN",
      "grade": "A",
      "course": "TMA4105",
      "credits": "7.5"
    }
  ]
  ```

---

## Testing

Run unit tests to validate the application logic:
```bash
python -m unittest discover -s test
```

### Test Cases:
- Test API fetching and error handling.
- Validate calculations for average grade.
- Verify transformation logic and data consistency.
- Ensure approved credits are correctly calculated.

---

## Future Enhancements
1. **Error Reporting**: Improve logging and error tracking with tools like Sentry.
2. **Frontend**: Enhance the UI with modern frameworks like React or Vue.js.
3. **Deployment**: Deploy the application to cloud platforms like AWS, Azure, or Google Cloud.
4. **Data Validation**: Add stricter validation for incoming API data.

---


