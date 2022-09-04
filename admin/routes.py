from flask import Flask,redirect,url_for,render_template,request
from admin import admin_bp
from admin.forms import MessagesForm,ServiceForm,NavbarLinkForm

@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')

@admin_bp.route('/profile')
def admin_profile():
    return render_template('admin/profile.html')

@admin_bp.route('/message/create',methods=['GET','POST'])
def admin_message_create():
    messageForm=MessagesForm()
    from run import db
    from models import Messages
    if request.method=='POST':
        message=Messages(
            name=messagesForm.name.data,
            email=messageForm.email.data,
            subject=messageForm.subject.data,
            message=messageForm.message.data,
            message_date=messageForm.message_date.data
        )
        db.session.add(message)
        db.session.commit()
        return redirect('/message/create')
    return render_template('admin/message_create.html',messageForm=messageForm)

# app indexinde olan service bolmesine yenisini elave etmek
@admin_bp.route('/service',methods=['GET','POST'])
def admin_service_create():
    serviceForm=ServiceForm()
    from run import db
    from models import Services
    services=Services.query.all()
    if request.method=='POST':
        service_title=serviceForm.service_title.data
        service_img=serviceForm.service_img.data
        service_text=serviceForm.service_text.data
        service=Services(service_title=service_title,service_img=service_img,service_text=service_text )
        db.session.add(service)
        db.session.commit()
        return redirect('/admin/service')
    return render_template('admin/service.html',serviceForm=serviceForm,services=services)

# admin de service elementlerini edit etmek
@admin_bp.route('/service/delete/<int:id>',methods=['GET','POST'])
def admin_service_delete(id):
    from run import db
    from models import Services
    service=Services.query.get(id)
    db.session.delete(service)
    db.session.commit()
    return redirect('/admin/service')


# @admin_bp.route('/service/update/<int:id>',methods=['GET','POST'])
# def admin_service_update(id):
#     serviceForm=ServiceForm()
#     from run import db
#     from models import Services
#     service=Services.query.get(id)
#     if request.method=='POST':
#         service_title=serviceForm.service_title.data
#         service_img=serviceForm.service_img.data
#         service_text=serviceForm.service_text.data
#         db.session.add(service)
#         db.session.commit()
#         return redirect('/admin/service')
#     return render_template('admin/service.html',service=service,serviceForm=serviceForm)

# APp de Navbar hissenin dinamikliyi
@admin_bp.route('/navbarlink',methods=['GET','POST'])
def admin_navbarlink_create():
    navbarLinkForm=NavbarLinkForm()
    from run import db
    from models import NavBar
    navbarlinks=NavBar.query.all()
    if request.method=='POST':
        navbar_name=navbarLinkForm.navbar_name.data
        navbar_url=navbarLinkForm.navbar_url.data
        navbar_order=navbarLinkForm.navbar_order.data
        is_active=navbarLinkForm.is_active.data
        navbar=NavBar(navbar_name=navbar_name,navbar_url=navbar_url,navbar_order=navbar_order,is_active=is_active)
        db.session.add(navbar)
        db.session.commit()
        return redirect('/admin/navbarlink')
    return render_template('admin/navbarlink.html',navbarLinkForm=navbarLinkForm,navbarlinks=navbarlinks)


@admin_bp.route('/navbarlink/delete/<int:id>',methods=['GET','POST'])
def admin_navbarlink_delete(id):
    from run import db
    from models import NavBar
    navbarlink=NavBar.query.get(id)
    db.session.delete(navbarlink)
    db.session.commit()
    return redirect('/admin/navbarlink')