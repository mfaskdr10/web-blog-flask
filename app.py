from flask import Flask, render_template, session, redirect, url_for, request
from config import Database
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route("/")
def index():
  email = session.get("email")
  return render_template("index.html", email=email)

@app.route('/login', methods=['POST', 'GET'])
def login_form():
  if request.method ==  'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    db = Database
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
      session['email'] = email
      return redirect(url_for('index'))
    else:
      return "Login failed. Please check your credentials."
    
  return render_template("login.html")

@app.route('/signup', methods=['POST', 'GET'])
def signup_form():
  if request.method ==  'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    db = Database
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (email, password) VALUES (%s, %s)", (email, password))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/login')

  return render_template("signup.html")

@app.route('/logout')
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))

@app.route('/posts') 
def posts_list():
  if "email" in session:
    db = Database
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('posts.html', email = session['email'], posts=posts)
  else:
    return redirect(url_for('login_form'))

@app.route("/posts/blogs/<int:id>", methods=['GET'])
def blog_page(id):
   if "email" in session:
    db = Database
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog WHERE id = %s", (id,))
    results = cursor.fetchone()

    return render_template("blogs.html", email = session['email'], data=results)
   else:
     return redirect(url_for('login_form'))

@app.route("/create", methods=['POST', 'GET'])
def create_page():
  if "email" in session:
    if request.method == 'POST':
      title = request.form.get('title')
      description = request.form.get('description')
      content = request.form.get('content')
      db = Database
      conn = db.connect_to_database()
      cursor = conn.cursor()
      cursor.execute("INSERT INTO blog (title, description, content) VALUES (%s, %s, %s)", (title, description, content))
      conn.commit()

      cursor.close()
      conn.close()

      return redirect(url_for('index'))
    return render_template('create.html', email = session['email'])
  else:
    return redirect(url_for('login_form'))


if __name__ == '__main__':
  app.run(debug=True)