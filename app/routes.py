```python
from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.forms import JobApplicationForm
from app.models import JobApplication
from app.utils.cover_letter_generator import generate_cover_letter
from app.utils.file_upload import upload_file
from app.utils.data_retrieval import get_application_data

@app.route('/')
@app.route('/dashboard')
def dashboard():
    # Fetch all job applications from the database
    applications = get_application_data()
    return render_template('dashboard.html', applications=applications)

@app.route('/new_application', methods=['GET', 'POST'])
def new_application():
    form = JobApplicationForm()
    if form.validate_on_submit():
        # Upload the resume file
        filename = upload_file(form.resume.data)
        if not filename:
            flash('file-upload-error')
            return redirect(request.url)

        # Generate the cover letter
        cover_letter = generate_cover_letter(form.job_description.data)

        # Create a new job application
        application = JobApplication(
            company_name=form.company_name.data,
            job_url=form.job_url.data,
            job_title=form.job_title.data,
            job_description=form.job_description.data,
            resume=filename,
            cover_letter=cover_letter
        )
        db.session.add(application)
        db.session.commit()
        flash('application-save-success')
        return redirect(url_for('dashboard'))

    return render_template('new_application.html', form=form)

@app.route('/edit_application/<int:id>', methods=['GET', 'POST'])
def edit_application(id):
    application = JobApplication.query.get_or_404(id)
    form = JobApplicationForm(obj=application)
    if form.validate_on_submit():
        # Update the job application details
        form.populate_obj(application)
        db.session.commit()
        flash('application-save-success')
        return redirect(url_for('dashboard'))

    return render_template('edit_application.html', form=form)

@app.route('/view_application/<int:id>', methods=['GET'])
def view_application(id):
    application = JobApplication.query.get_or_404(id)
    return render_template('view_application.html', application=application)
```