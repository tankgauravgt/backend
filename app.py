"""
Grafana Dashboard API
=================================================
This file provides the entry point for the Grafana Dashboard API.

Dependencies:
--------------------------
- Blueprint: Main View
- Blueprint: Flight List View
- Blueprint: Flight Detail View
"""

from flask import Blueprint, Flask
from flask_cors import CORS

# ==============================================
# Application Setup
# ==============================================

# Create Flask app instance
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing
CORS(app)

# ==============================================
# Blueprint Setup
# ==============================================

# Root Blueprint for dashboard-related modules
dashboard_bp = Blueprint('dashboard', __name__)

# ==============================================
# Import and Register Blueprints
# ==============================================

# Import individual dashboard blueprints
from dashboards.main import main_bp  #: Main dashboard blueprint
from dashboards.flightlist import flightlist_bp  #: Flight list dashboard blueprint

# Register individual blueprints with the dashboard root blueprint
dashboard_bp.register_blueprint(main_bp, url_prefix='/main')
dashboard_bp.register_blueprint(flightlist_bp, url_prefix='/flightlist')

# Register the dashboard root blueprint with the Flask app
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

# ==============================================
# List Registered Endpoints
# ==============================================

# Print all registered routes and their endpoints
for rule in app.url_map.iter_rules():
    print('ENDPOINT:', rule)

# ==============================================
# Application Entry Point
# ==============================================
if __name__ == "__main__":
    app.run(debug=True, port=5001)
