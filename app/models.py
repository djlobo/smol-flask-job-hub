```python
from datetime import datetime
from app import db

# Define the JobApplication model
class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Store the company name
    company_name = db.Column(db.String(100), nullable=False)
    # Store the URL if available
    url = db.Column(db.String(500))
    # Store the job title
    job_title = db.Column(db.String(100), nullable=False)
    # Store the job description
    job_description = db.Column(db.Text, nullable=False)
    # Store the resume file path
    resume = db.Column(db.String(500), nullable=False)
    # Store the generated cover letter
    generated_cover_letter = db.Column(db.Text, nullable=False)
    # Store the latest updated/modified cover letter
    updated_cover_letter = db.Column(db.Text)
    # Store the date of application
    date_of_application = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<JobApplication {self.job_title} at {self.company_name}>'
```