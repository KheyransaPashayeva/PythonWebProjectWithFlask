from flask import Flask,redirect,url_for,render_template,request
from run import app

@app.route('/contact',methods=['GET','POST'])
def contact():
    from models import Messages,db
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']
        msj=Messages(name=name,email=email,subject=subject,message=message)
        db.session.add(msj)
        db.session.commit()
    return render_template('contact.html')


@app.route('/messages',methods=['GET','POST'])
def messages():
    from models import Messages,db
    msj=Messages.query.all()
    return render_template('messages.html',msj=msj)


@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    from models import Messages,db
    msj = Messages.query.get(id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msj.name = name
        msj.email = email
        msj.message = message

        db.session.add(msj)
        db.session.commit()

        return redirect('/messages')

    return render_template('edit.html', msj=msj)


@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    from models import Messages,db
    mesaj = Messages.query.get(id)
    db.session.delete(mesaj)
    db.session.commit()
    
    return redirect('/messages')
