from flask import Flask,redirect,url_for,render_template,request
import sqlite3


app=Flask(__name__)
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

if __name__ == '__main__':
    app.run(port=5000,debug=True)
