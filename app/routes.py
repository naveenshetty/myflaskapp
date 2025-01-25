from flask import render_template, Blueprint
from app import app

from .utils import fetch_exam_data, transform_data

# Define a blueprint for your routes
main = Blueprint('main', __name__)


@app.route("/")
def home():
    # Fetch and process the data
    exam_data = fetch_exam_data()
    studentweb_data, average_grade, approved_credits = transform_data(exam_data)

    return render_template("index.html",
                           studentweb_data=studentweb_data,
                           average_grade=average_grade,
                           approved_credits=approved_credits)

