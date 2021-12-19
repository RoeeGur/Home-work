from flask import Flask, redirect, url_for
from flask import render_template

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


if __name__ == '__main__':
    app2.run(debug=True)