import sys

# add your project directory to the sys.path
project_home = u'/home/drbaz/butterfly_survey'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from app import app
application = app.server
