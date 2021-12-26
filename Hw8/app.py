from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session

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
    elif Users.get(user,'Not Found') != 'Not Found':
        p = Users[user]
    elif Users.get(user,'Not Found') == 'Not Found':
        p = 'Not found in the system'

    if request.method == 'POST':
        username = request.form['username1']
        session['username'] = username
    return render_template('assignment9.html', p_user=p, username=username)

Users = {'user1': {'first_name': 'Yossi', 'last_name': 'Cohen', 'email': 'Y@gmail.com'},
         'user2':{'first_name': 'Noa', 'last_name': 'Radin', 'email': 'NoaTheQueen@gmail.com'},
         'roeeGur':{'first_name': 'Roee', 'last_name': 'Gur', 'email': 'RoeeGur@gmail.com'},
         'Pedro':{'first_name': 'Pedro', 'last_name': 'Gur', 'email': 'PedroTheDog@gmail.com'},
         'ShoshanaX':{'first_name': 'Shoshana', 'last_name': 'The Neighbor', 'email': 'Shoshi@gmail.com'}}

if __name__ == '__main__':
    app2.run(debug=True)
