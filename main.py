from flask import Flask,render_template,request
from signup import signup

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        return name,email,password
    return render_template('index.html')

app.register_blueprint(signup,url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
    
