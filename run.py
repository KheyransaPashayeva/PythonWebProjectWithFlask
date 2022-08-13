from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120),nullable=False)
    message = db.Column(db.String(220),nullable=False)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo',methods=['GET','POST'])
def demo():
    if request.method=='POST':
        username=name=request.form['u_name']
        conn=sqlite3.connect('project.db')
        query=f"insert into Workers(username) values ('{username}')"
        conn.execute(query)
        conn.commit()
        data=[]
        for row in conn.execute('SELECT username FROM Workers'):
            data.append(row)
        return render_template('demo.html',context=data)
        
    return render_template('demo.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']
        msj=Messages(name=name,email=email,subject=subject,message=message)
        db.session.add(msj)
        db.session.commit()
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
