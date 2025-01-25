import requests
from dotenv import load_dotenv
import os
import logging
from .constants import GRADE_MAPPING, GRADE_POINTS

logging.basicConfig(level=logging.ERROR)
# Load environment variables from .env file
load_dotenv()

# Access API URLs from environment variables
exam_system_api = os.getenv("EXAM_SYSTEM_API")
student_web_api = os.getenv("STUDENT_WEB_API")


# Custom exception for API fetch errors
class APIDataFetchError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def fetch_exam_data():
    """Fetch exam data from the API."""
    try:
        response = requests.get(exam_system_api)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching exam data: {e}")
        raise APIDataFetchError(f"Failed to fetch exam data from API: {e}")
        # return []  # You can customize this behavior based on your needs


def calculate_average_grade(total_grade_points: float, total_exams: int) -> float:
    """Calculate the average grade from the total grade points and number of exams."""
    if total_exams > 0:
        return total_grade_points / total_exams
    else:
        logging.error("Total exams is 0, cannot calculate average grade.")
        raise ValueError("Cannot calculate average grade when total exams is 0")


def calculate_approved_credits(exam_data):
    """Calculate the total approved credits (excluding failing grades)."""
    approved_credits = 0
    for entry in exam_data:
        # Check if essential fields are present and valid
        if "STUDENTID" not in entry or "GRADE" not in entry or "CREDITS" not in entry:
            logging.warning(f"Skipping incomplete entry: {entry}")
            continue  # Skip incomplete entries

        grade_letter = GRADE_MAPPING.get(str(entry["GRADE"]), "F")
        if grade_letter != "F":  # If grade is not "F", count the credits
            try:
                credits = float(entry["CREDITS"]) if entry["CREDITS"] else 0
            except ValueError:
                logging.error(f"Invalid CREDITS value: {entry['CREDITS']} for student {entry['STUDENTID']}")
                credits = 0
            approved_credits += credits

    return approved_credits


def transform_student_data(exam_data):
    """Transform exam data for student web."""
    studentweb_data = []
    total_grade_points = 0
    total_exams = 0

    for student in exam_data:
        # Ensure required fields are present and valid
        if "STUDENTID" not in student or "FIRSTNAME" not in student or "CREDITS" not in student:
            logging.warning(f"Skipping student with missing data: {student}")
            continue

        if student["GRADE"] > 0:  # Only include students with valid grades
            # Collect last name if present
            last_name = student.get("LASTNAME", "").strip()  # Default to empty and strip whitespace
            course_name = student.get("COURSE", "").strip()  # Default to empty and strip whitespace

            # Convert grade from numeric to letter using the GRADE_MAPPING
            grade_letter = GRADE_MAPPING.get(str(student["GRADE"]), "F")  # Default to "F" if not found

            # Concatenate FIRSTNAME and LASTNAME and strip unnecessary whitespace
            full_name = f"{student['FIRSTNAME']} {last_name}".strip()

            studentweb_data.append({
                "id": student["STUDENTID"],
                "name": full_name,
                "course": course_name,
                "grade": grade_letter,
                "credits": student["CREDITS"],
            })
            total_grade_points += GRADE_POINTS.get(grade_letter, 0)
            total_exams += 1
        else:
            logging.info(f"Skipping student with invalid grade: {student}")

    return studentweb_data, total_grade_points, total_exams


def transform_data(exam_data):
    """Combine the data transformation and calculations."""
    try:
        studentweb_data, total_grade_points, total_exams = transform_student_data(exam_data)
        average_grade = calculate_average_grade(total_grade_points, total_exams)
        approved_credits = calculate_approved_credits(exam_data)

        return studentweb_data, average_grade, approved_credits

    except Exception as e:
        logging.error(f"Error in data transformation: {e}")
        raise ValueError(f"Failed to transform data: {e}")
