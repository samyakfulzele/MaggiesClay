from flask import *
from controls.user import user

app = Flask(__name__)
app.secret_key = 'maggies_clay'

userObj = user()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/product')
def product():
    return render_template("product.html")

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        gender = request.form['gender']
        email = request.form['email']
        conf_pass = request.form['password']
        password = request.form['confirmPassword']
        if conf_pass == password:
            registerStatus = userObj.register(first_name,last_name,gender,email,password)
            if registerStatus == 1:
                register_success = True
                return render_template("index.html",register_success=register_success)
            else:
                register_fail = True
                return render_template("index.html",register_fail=register_fail)
        else:
            password_fail = True
            return render_template("index.html",password_fail=password_fail)
    else:
        return redirect(url_for('home'))

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        loginStatus = userObj.login(email,password)
        if loginStatus == 1:
            return redirect(url_for('home'))
        else:
            login_fail = True
            return render_template("index.html",login_fail=login_fail)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug = True) 