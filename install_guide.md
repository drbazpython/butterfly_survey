# Testing Dash-Plotly and pythonanywhere

[pythonanywhere](https://www.pythonanywhere.com/user/drbaz/)

[video](https://youtu.be/Qx5eFVUdDxk?si=SmICBifVHmuIYyBv)

[Dash in 20 minutes](https://dash.plotly.com/tutorial)

### Installation

Use an assets folder to store all images

Use a pages folder to store all code within web pages

pip3 install dash

pip3 install dash-tools

pip3 install pandas

**to change port use **

```python
if __name__ == '__main__':
    app.run(debug=True, port=5500)
```

### Deploy Dash-Plotly app on pythonanywhere

need to move

```python
if __name__ == '__main__':
    app.run(debug=True, port=5500)
```

into wsgi_dev.py and change to

N.B. app refers to app defined in app.py

```python
from app import app
if __name__ == '__main__':
    app.run_server(debug=True)
```

Run the wsgi_dev.py file to provide a local web server to the Dash app

```python
python3 ./wsgi_dev.py
```

Also run

```python
pip3 freeze > requirements.txt
```

Create a github repo

From CODE  - Copy url from HTTPS clone repo

don't use virtualenvs this as they take up too much space .Plotly, Dash and Pandas are part of the batteries included on pythonanywhere. No need ro run pip install either, unless there's a package that is not batteries included

[batteries included](https://www.pythonanywhere.com/batteries_included/https:/)

From pythonanywhere open bash console and run

```shell

git clone https://github.com/drbazpython/butterfly_survey.git
# mkvirtualenv butterfly_survey --python=/usr/bin/python3.10 
cd butterfly_survey
# pip3 install -r requirements.txt


```

To activate venv use workon instead of source

[continue](https://youtu.be/9TDqcPgb4c8?si=y8B_tKy6hP068E_S&t=629https:/)

Using the pythonanywhere default wsgi file, comment out the Hello Worlde code and add th code below to the bottom of the file

```python
import sys

# add your project directory to the sys.path
project_home = u'/home/drbaz/butterfly_survey'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# need to pass the flask app as "application" for WSGI to work
# for a dash app, that is at app.server
# see https://plot.ly/dash/deployment
from app3 import app
application = app.server
```
