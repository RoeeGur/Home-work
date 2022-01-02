from flask import Blueprint, render_template

assignment10 = Blueprint ('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')

@assignment10.route('/assignment10')
def assignment10_func():
    return render_template('assignment10.html')
