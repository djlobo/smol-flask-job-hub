```python
# Import necessary modules
from flask import jsonify
from app import db
from app.models import JobApplication

# Function to retrieve all job applications for a user
def get_all_applications(user_id):
    # Query the database for all job applications for the given user
    applications = JobApplication.query.filter_by(user_id=user_id).all()

    # Convert the result to JSON
    applications_json = jsonify([app.to_dict() for app in applications])

    return applications_json

# Function to retrieve a single job application
def get_application(application_id):
    # Query the database for the specific job application
    application = JobApplication.query.get(application_id)

    # Check if the application exists
    if application is None:
        return None

    # Convert the result to JSON
    application_json = jsonify(application.to_dict())

    return application_json
```