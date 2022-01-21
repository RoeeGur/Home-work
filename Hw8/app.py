from flask import Flask, redirect, url_for, jsonify
from flask import render_template
from flask import request
from flask import session
from torch import res


from interact_with_DB import interact_db
import requests
import random

app2 = Flask(__name__)


@app2.route('/')
def Main_Page_fanc():
    return render_template('Main_Page.html')


@app2.route('/assignment8')
def Hobbies_func():
    # Do something with DB
    name = 'Roee'
    second_name = 'Gur'
    Hob = 'sport'

    return render_template('assignment8.html',
                           hobbies=('soccer', 'music', 'watch a movie'))


@app2.route('/assignment9', methods=['GET', 'POST'])
def Form_func():
    # FirstN = request.args['First Name']
    # LastN = request.args['Last Name']
    # Email = request.args['email']
    user = request.args.get('username')
    p = ""
    username = ""
    if user is None:
        p = Users
    elif Users.get(user, 'Not Found') != 'Not Found':
        p = Users[user]
    elif Users.get(user, 'Not Found') == 'Not Found':
        p = 'Not found in the system'

    if request.method == 'POST':
        username = request.form['username1']
        session['username'] = username
    return render_template('assignment9.html', p_user=p, username=username)


Users = {'user1': {'first_name': 'Yossi', 'last_name': 'Cohen', 'email': 'Y@gmail.com'},
         'user2': {'first_name': 'Noa', 'last_name': 'Radin', 'email': 'NoaTheQueen@gmail.com'},
         'roeeGur': {'first_name': 'Roee', 'last_name': 'Gur', 'email': 'RoeeGur@gmail.com'},
         'Pedro': {'first_name': 'Pedro', 'last_name': 'Gur', 'email': 'PedroTheDog@gmail.com'},
         'ShoshanaX': {'first_name': 'Shoshana', 'last_name': 'The Neighbor', 'email': 'Shoshi@gmail.com'}}

from assignment10.assignment10 import assignment10
app2.register_blueprint(assignment10)


# @app2.route('/assignment11/users')
# def Users_func():
#     return render_template('assignment11/users.html')

@app2.route('/assignment11/outer_source')
def Reqest_func():
    return render_template('assignment11/outer_source.html')

def get_User(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res

@app2.route('/req_backend')
def req_backend_func():
    num = int(request.args['number'])
    User = get_User(num)
    return render_template('assignment11/outer_source.html', User=User)


@app2.route('/assignment11/users')
def users_func():
    return_dict = {}
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        return_dict[f'user_{user.id}'] = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
    return jsonify(return_dict)

@app2.route('/assignment12/restapi_users', defaults={ 'USER_ID': 2})
@app2.route('/assignment12/restapi_users/<int:USER_ID>')
def get_user_db(USER_ID):
    user_query= 'SELECT * FROM users WHERE id=%s;' % USER_ID
    user =  interact_db(query=user_query, query_type='fetch')
    if len(user) == 0:
        user_dict = {
            'status': 'Failed',
            'message': 'User Not Found'
        }
    else:
        user_dict = {
            'status': 'Success',
            'id': user[0].id,
            'name': user[0].name,
            'email': user[0].email
            }
    return jsonify(user_dict)



if __name__ == '__main__':
    app2.run(debug=True)
