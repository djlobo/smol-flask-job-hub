```python
# Import the Flask class from the flask module
from flask import Flask

# Import the configuration data
from config import Config

# Import the application instance
from app import create_app, db

# Import the models module to create the database tables
from app.models import JobApplication

# Create the Flask application object
app = create_app(Config)

# Create a context for the application
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'JobApplication': JobApplication}

# Main driver function
if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```