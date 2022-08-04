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

def Select_user(id):
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    c.execute(f"SELECT FROM Workers WHERE username = '{request.form['username']}' password = '{request.form['password']}'  id = {id}")
    conn.commit()
    conn.close()
    return render_template('demo.html')


def delete_user(id):
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    c.execute(f"DELETE FROM Workers WHERE id = {id}")
    conn.commit()
    conn.close()
    session.clear()
    session['error'] = 'User deleted'
    
    return render_template('demo.html')



def update_user(id):
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    c.execute(f"UPDATE Workers SET username = '{request.form['username']}', password = '{request.form['password']}' WHERE id = {id}")
    conn.commit()
    conn.close()
    session['is_logged_in'] = False
    session['error'] = 'User updated successfully'
    return render_template('demo.html')


if __name__ == '__main__':
    app.run(port=5000,debug=True)
