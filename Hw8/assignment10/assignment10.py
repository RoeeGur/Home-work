from flask import Blueprint, render_template
from interact_with_DB import interact_db
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session


assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10',
                         template_folder='templates')


# @assignment10.route('/assignment10')
# def assignment10_func():
#     return render_template('assignment10.html')

@assignment10.route('/assignment10')
def assignment10_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    LastN = request.form['LastN']
    email = request.form['email']

    query = "INSERT INTO users(name, LastN, email) VALUES ('%s' , '%s' , '%s')" % (name, LastN, email)
    interact_db(query=query, query_type='commit')

    return redirect('/assignment10')

@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users where id='%s';" %user_id
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

