```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Load configurations from config.py
app.config.from_object('config')

# Initialize SQLAlchemy with app configuration
db = SQLAlchemy(app)

# Import routes after initializing db to avoid circular imports
from app import routes
```