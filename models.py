from run import app,db

#contactdan geden msjlar
class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120),nullable=False)
    message = db.Column(db.String(220),nullable=False)
    