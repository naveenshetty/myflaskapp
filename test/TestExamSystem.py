import unittest
from unittest.mock import patch, MagicMock

from my_flask_app.app.utils import (
    fetch_exam_data,
    calculate_average_grade,
    calculate_approved_credits,
    transform_student_data,
    transform_data,
)


class TestExamSystem(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_exam_data_success(self, mock_get):
        # Simulate a successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"STUDENTID": "1", "GRADE": 5, "CREDITS": 3}]
        mock_get.return_value = mock_response

        result = fetch_exam_data()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["STUDENTID"], "1")

    def test_calculate_average_grade(self):
        # Test average grade calculation
        result = calculate_average_grade(15, 3)
        self.assertEqual(result, 5)

        # Test with total_exams as 0, expecting a ValueError
        with self.assertRaises(ValueError):
            calculate_average_grade(0, 0)

    def test_calculate_approved_credits(self):
        exam_data = [
            {"STUDENTID": "1", "GRADE": 5, "CREDITS": 3},
            {"STUDENTID": "2", "GRADE": 0, "CREDITS": 0},
            {"STUDENTID": "3", "GRADE": 4, "CREDITS": 4},
        ]
        result = calculate_approved_credits(exam_data)
        self.assertEqual(result, 7)  # Only grades "A" and "B" should count

    def test_transform_student_data(self):
        exam_data = [
            {"STUDENTID": "1", "FIRSTNAME": "John", "GRADE": 5, "CREDITS": 3},
            {"STUDENTID": "2", "FIRSTNAME": "Jane", "GRADE": 0, "CREDITS": 0},
        ]
        studentweb_data, total_grade_points, total_exams = transform_student_data(exam_data)

        self.assertEqual(len(studentweb_data), 1)  # Only one valid student
        self.assertEqual(studentweb_data[0]["name"], "John")
        self.assertEqual(total_grade_points, 5)
        self.assertEqual(total_exams, 1)

    def test_transform_data(self):
        exam_data = [
            {"STUDENTID": "1", "FIRSTNAME": "John", "GRADE": 5, "CREDITS": 3},
            {"STUDENTID": "2", "FIRSTNAME": "Jane", "GRADE": 0, "CREDITS": 0},
        ]
        studentweb_data, average_grade, approved_credits = transform_data(exam_data)

        self.assertEqual(len(studentweb_data), 1)  # Only one valid student
        self.assertEqual(average_grade, 5)
        self.assertEqual(approved_credits, 3)


if __name__ == "__main__":
    unittest.main()
