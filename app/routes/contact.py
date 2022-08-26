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
        mesaj=Messages(name=name,email=email,subject=subject,message=message)
        db.session.add(mesaj)
        db.session.commit()
    return render_template('app/contact.html')


@app.route('/messages',methods=['GET','POST'])
def messages():
    from models import Messages,Users,db
    user=Users.query.all()
    if user.is_active==True:
       mesaj=Messages.query.all()
       return render_template('admin/messages.html',mesaj=mesaj)
    else:
        return redirect('/login')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    from models import Messages,db
    mesaj = Messages.query.get(id)
    if request.method == 'POST':
        mesaj.name  = request.form['name']
        mesaj.email = request.form['email']
        mesaj.subject  = request.form['subject']
        mesaj.message = request.form['message']

        db.session.add(mesaj)
        db.session.commit()

        return redirect('/messages')

    return render_template('admin/edit.html', mesaj=mesaj)


@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    from models import Messages,db
    mesaj = Messages.query.get(id)
    db.session.delete(mesaj)
    db.session.commit()
    
    return redirect('/messages')

