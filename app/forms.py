```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, URL, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired

# Define the form for creating a new job application
class JobApplicationForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    job_url = StringField('Job URL', validators=[URL(), Optional()])
    job_description = TextAreaField('Job Description', validators=[DataRequired()])
    resume = FileField('Resume', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'doc'], 'PDF or DOC files only!')
    ])

# Define the form for editing an existing job application
class EditJobApplicationForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    job_url = StringField('Job URL', validators=[URL(), Optional()])
    job_description = TextAreaField('Job Description', validators=[DataRequired()])
    cover_letter = TextAreaField('Cover Letter', validators=[DataRequired()])
    resume = FileField('Resume', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'doc'], 'PDF or DOC files only!')
    ])
```