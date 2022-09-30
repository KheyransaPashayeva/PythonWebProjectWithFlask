from admin.imports import *


@admin_bp.route('/')
@login_required
def admin_index():
    return render_template('admin/index.html')

@admin_bp.route('/profile')
@login_required
def admin_profile():
    return render_template('admin/profile.html')

@admin_bp.route('/message',methods=['GET','POST'])
@login_required
def admin_message():
    from run import db
    from models import Messages
    messages=Messages.query.all()
   
    return render_template('admin/contact_message.html',messages=messages)

# app indexinde olan service bolmesine yenisini elave etmek
@admin_bp.route('/service',methods=['GET','POST'])
@login_required
def admin_service_create():
    serviceForm=ServiceForm()
    from run import db
    from models import Services
    services=Services.query.all()
    if request.method=='POST':
        service=Services( service_title=serviceForm.service_title.data, service_img=serviceForm.service_img.data,
                          service_text=serviceForm.service_text.data
                        )
        db.session.add(service)
        db.session.commit()
        return redirect('/admin/service')
    return render_template('admin/service.html',serviceForm=serviceForm,services=services)

# admin de message elementlerini edit etmek
@admin_bp.route('/message/delete/<int:id>',methods=['GET','POST'])
def admin_message_delete(id):
    from run import db
    from models import Messages
    message=Messages.query.get(id)
    db.session.delete(message)
    db.session.commit()
    return redirect('/admin/message')

# admin de service elementlerini edit etmek
@admin_bp.route('/service/delete/<int:id>',methods=['GET','POST'])
def admin_service_delete(id):
    from run import db
    from models import Services
    service=Services.query.get(id)
    db.session.delete(service)
    db.session.commit()
    return redirect('/admin/service')



# APp de Navbar hissenin dinamikliyi
@admin_bp.route('/navbarlink',methods=['GET','POST'])
@login_required
def admin_navbarlink_create():
    navbarLinkForm=NavbarLinkForm()
    from run import db
    from models import NavBar
    navbarlinks=NavBar.query.all()
    if request.method=='POST':
        navbar=NavBar( navbar_name=navbarLinkForm.navbar_name.data, navbar_url=navbarLinkForm.navbar_url.data,
                       navbar_order=navbarLinkForm.navbar_order.data,is_active=navbarLinkForm.is_active.data
                     )
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

# Navbar end

# Team route start
@admin_bp.route('/team',methods=['GET','POST'])
@login_required
def admin_team_create():
    teamForm=TeamForm()
    from run import db,main
    from models import Team
    teams=Team.query.all()
    if request.method=='POST':
        file=request.form['name']
        team_folder = os.path.join(main.config['UPLOAD_FOLDER'], file)
        os.mkdir(team_folder)
        file=request.files['employee_img']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f"Employe{random.randint(1,1000)}.{extension}"
        file.save(os.path.join(team_folder,new_filename))
        team=Team( name=teamForm.name.data,employee_img=new_filename,position=teamForm.position.data,
                   info=teamForm.info.data,order=teamForm.order.data,is_active=teamForm.is_active.data
                 )
        db.session.add(team)
        db.session.commit()
        return redirect('/admin/team')
    return render_template('admin/team.html',teamForm=teamForm,teams=teams)

@admin_bp.route('/team/delete/<int:id>',methods=['GET','POST']) 
def admin_team_delete(id):
    from run import db
    from models import Team
    teams=Team.query.get(id)
    db.session.delete(teams)
    db.session.commit()
    return redirect('/admin/team')

# team end


@admin_bp.route('/testimonials',methods=['GET','POST'])
@login_required
def admin_testimonials():
    from run import db,main
    from models import Testimonials
    testimonials=Testimonials.query.all()
    testimonialsForm=TestimonialsForm()
    if request.method=="POST":
            file=request.files['img']
            #seklin olcusunu tapmaq ucun yazdiq ve rahat olsun deye printde verdi
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            if extension=='jpg' or extension=='png': #burda da jpg ve png sonluqlu fileler daxil edilmesini temin edir.
                # ikinci bir usul ALLOWED_EXTENSIONS = {'png', 'jpg'} sekilde run.pyde yazib  route da if  extinsion in ALLOWED_EXTENSIONS yaza bilerik
                new_filename=f"Tester{random.randint(1,1000)}.{extension}"
                file.save(os.path.join(main.config["UPLOAD_FOLDER"],new_filename))
                poto_size = os.stat(main.config["UPLOAD_FOLDER"]).st_size
                print(poto_size)
                testimonial=Testimonials( name=testimonialsForm.name.data,info=testimonialsForm.info.data,
                                          img=new_filename, order=testimonialsForm.order.data,isActive=testimonialsForm.isActive.data,
                                          profession=testimonialsForm.profession.data
                                        )
                db.session.add(testimonial)
                db.session.commit()
            return redirect('/admin/testimonials')
    return render_template('admin/testimonials.html',testimonialsForm=testimonialsForm,testimonials=testimonials)

@admin_bp.route('/testimonials/delete/<int:id>',methods=['GET','POST'])
def admin_testimonial_delete(id):
    from run import db,main
    from models import Testimonials
    testimonial=db.session.execute(db.select(Testimonials.img).filter_by(id=id)).one() 
    testimonial=list(testimonial)
    testimonial_img=testimonial[0]
    os.remove(os.path.join(main.config["UPLOAD_FOLDER"], testimonial_img))
    testimonials=Testimonials.query.get(id)
    db.session.delete(testimonials)
    db.session.commit()
    return redirect('/admin/testimonials')


# app indexinde olan transport bolmesine yenisini elave etmek
@admin_bp.route('/transport',methods=['GET','POST'])
@login_required
def admin_transport_create():
    transportForm=TransportForm()
    from run import db
    from models import Transport
    transports=Transport.query.all()
    if request.method=='POST':
        transport=Transport( transport_title=transportForm.transport_title.data,
                             transport_img=transportForm.transport_img.data,
                             transport_text=transportForm.transport_text.data,
                             transport_url=transportForm.transport_url.data
                            )
        db.session.add(transport)
        db.session.commit()
        return redirect('/admin/transport')
    return render_template('admin/transport.html',transportForm=transportForm,transports=transports)


# admin de transport elementlerini delete etmek
@admin_bp.route('/transport/delete/<int:id>',methods=['GET','POST'])
def admin_transport_delete(id):
    from run import db
    from models import Transport
    transport=Transport.query.get(id)
    db.session.delete(transport)
    db.session.commit()
    return redirect('/admin/transport')


# app indexinde olan feature bolmesine yenisini elave etmek
@admin_bp.route('/feature',methods=['GET','POST'])
@login_required
def admin_feature_create():
   from run import db,main
   from models import Feature
   features=Feature.query.all()
   featureForm=FeatureForm()
   if request.method=="POST":
        file=request.files['feature_img']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f"Feature{random.randint(1,1000)}.{extension}"
        file.save(os.path.join(main.config["UPLOAD_FOLDER"],new_filename))
        feature=Feature( feature_title=featureForm.feature_title.data,feature_img=new_filename,
                         feature_text=featureForm.feature_text.data,feature_orderimg=featureForm.feature_orderimg.data,
                         feature_ordertext=featureForm.feature_ordertext.data,is_active=featureForm.is_active.data
                        )
        db.session.add(feature)
        db.session.commit()
        return redirect('/admin/feature')
   return render_template('admin/feature.html',featureForm=featureForm,features=features)



@admin_bp.route('/feature/delete/<int:id>',methods=['GET','POST'])
def admin_feature_delete(id):
    from run import db,main
    from models import Feature
    feature=db.session.execute(db.select(Feature.feature_img).filter_by(id=id)).one() 
    feature=list(feature)
    new_feature_img=feature[0]
    os.remove(os.path.join(main.config["UPLOAD_FOLDER"], new_feature_img))
    features=Feature.query.get(id)
    db.session.delete(features)
    db.session.commit()
    return redirect('/admin/feature')


# app indexinde olan faq bolmesine yenisini elave etmek
@admin_bp.route('/faq',methods=['GET','POST'])
@login_required
def admin_faq_create():
    faqsForm=FaqsForm()
    from run import db
    from models import Faqs
    faqs=Faqs.query.all()
    if request.method=='POST':
        faq=Faqs( faq_question=faqsForm.faq_question.data,faq_answer=faqsForm.faq_answer.data)
        db.session.add(faq)
        db.session.commit()
        return redirect('/admin/faq')
    return render_template('admin/faq.html',faqsForm=faqsForm,faqs=faqs)

# admin de faq elementlerini delete etmek
@admin_bp.route('/faq/delete/<int:id>',methods=['GET','POST'])
def admin_faq_delete(id):
    from run import db
    from models import Faqs
    faq=Faqs.query.get(id)
    db.session.delete(faq)
    db.session.commit()
    return redirect('/admin/faq')

# app indexinde olan Stat bolmesine yenisini elave etmek
@admin_bp.route('/stat',methods=['GET','POST'])
@login_required
def admin_stat_create():
    statsForm=StatsForm()
    from run import db
    from models import Stats
    stats=Stats.query.all()
    if request.method=='POST':
        stat=Stats( name=statsForm.name.data,value=statsForm.value.data)
        db.session.add(stat)
        db.session.commit()
        return redirect('/admin/stat')
    return render_template('admin/stat.html',statsForm=statsForm,stats=stats)

@admin_bp.route('/stat/delete/<int:id>',methods=['GET','POST'])
def admin_stat_delete(id):
    from run import db
    from models import Stats
    stat=Stats.query.get(id)
    db.session.delete(stat)
    db.session.commit()
    return redirect('/admin/stat')

# app indexinde olan social_media bolmesine yenisini elave etmek
@admin_bp.route('/social_media',methods=['GET','POST'])
@login_required
def admin_social_media_create():
    socialmedia=SocialMediaForm()
    from run import db
    from models import SocialMedia
    socialmedias=SocialMedia.query.all()
    if request.method=='POST':
        socialmedia=SocialMedia( social_name=socialmediaForm.social_name.data,social_icon=socialmediaForm.social_icon.data,
                                social_url=socialmediaForm.social_url.data
                                )
        db.session.add(socialmedia)
        db.session.commit()
        return redirect('/admin/social_media')
    return render_template('admin/social_media.html',socialmediaForm=socialmediaForm,socialmedias=socialmedias)

@admin_bp.route('/social_media/delete/<int:id>',methods=['GET','POST'])
def admin_social_media_delete(id):
    from run import db
    from models import SocialMedia
    socialmedia=SocialMedia.query.get(id)
    db.session.delete(socialmedia)
    db.session.commit()
    return redirect('/admin/social_media')

# app indexinde olan team social_media bolmesine yenisini elave etmek
@admin_bp.route('/team_social',methods=['GET','POST'])
@login_required
def admin_team_social_create():
    teamsocialForm=TeamSocialForm()
    from run import db
    from models import TeamSocial
    teamsocials=TeamSocial.query.all()
    if request.method=='POST':
        teamsocial=TeamSocial( social_name=teamsocialForm.social_name.data,social_icon=teamsocialForm.social_icon.data,
                                social_url=teamsocialForm.social_url.data
                                )
        db.session.add(teamsocial)
        db.session.commit()
        return redirect('/admin/team_social')
    return render_template('admin/team_social.html',teamsocialForm=teamsocialForm,teamsocials=teamsocials)

@admin_bp.route('/team_social/delete/<int:id>',methods=['GET','POST'])
def admin_team_social_delete(id):
    from run import db
    from models import TeamSocial
    teamsocials=TeamSocial.query.get(id)
    db.session.delete(teamsocials)
    db.session.commit()
    return redirect('/admin/team_social')