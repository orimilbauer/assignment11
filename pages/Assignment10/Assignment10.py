import flask
from flask import Blueprint, render_template,request,redirect
from interact_with_DB import interact_db

# about blueprint definition
assignment10 = Blueprint('assignment10', __name__,
                  static_folder='static',
                  #maybe
                  static_url_path='/assignment10',
                  template_folder='templates')

# Routes
@assignment10.route('/assignment10')
def index():
    query='select * from users;'
    users=interact_db(query=query,query_type='fetch')
    return render_template('assignment10.html',users=users)

@assignment10.route ('/insert_user',methods=['post'])
def insert_user_func():
        #get the date
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        #inster
        query="insert into users(name,email,password) values ('%s','%s','%s');" %(name,email,password)
        interact_db(query=query,query_type='commit')
        flask.flash('insert success')
        return redirect('/assignment10')

@assignment10.route ('/delete_user',methods=['POST'])
def delete_user_func():
        #get the date
        user_id=request.form['id']
        query="DELETE FROM users Where id='%s';"%user_id
        interact_db(query=query,query_type='commit')
        flask.flash('delete success')
        return redirect('/assignment10')

@assignment10.route ('/update_user',methods=['POST'])
def update_user_func():
        #get the date
        user_id=request.form['id']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        query="UPDATE users SET name='%s',email='%s',password='%s' Where id='%s' ;"%(name,email,password,user_id)
        interact_db(query=query,query_type='commit')
        flask.flash('if id in the table, update success')
        return redirect('/assignment10')

