import os, sys, time
from flask import Flask
from flask import render_template
from jinja2 import FileSystemLoader

app_root_dir = os.path.join(os.path.dirname(__file__), '../../')
views_dir = os.path.join(app_root_dir,  'views/')

print(os.path.abspath(views_dir))
app = Flask(__name__, static_folder=os.path.join(app_root_dir, 'lib'))
app.jinja_loader = FileSystemLoader(views_dir)
print(app.static_folder)
app.static_folder = os.path.join(app_root_dir, 'lib')
print(os.path.abspath(app.static_folder))


@app.route("/")
def hello():
    return render_template('main.html')

if __name__ == "__main__":
    sys.stdout.flush()
    app.run(host='127.0.0.1', port=5000, debug=True)
