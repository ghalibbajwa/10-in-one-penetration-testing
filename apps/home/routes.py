# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import current_app, render_template, request, url_for, redirect,jsonify
import json
from flask_login import login_required,current_user
from jinja2 import TemplateNotFound
from apps import db
from sqlalchemy.orm import class_mapper

from apps.home.forms import TestForm
from apps.home.models import Tests
from apps.configs.models import Configs
from apps.home.libs import burp,zap,nuclei,nikto,waybackcurl,cmseek,dork,cmsscan,openvas
from threading import Thread

def sql_dict(obj):
    """Converts a SQLAlchemy object to a dictionary."""
    if not obj:
        return None
    
    # Get the mapped columns and their values
    mapped_cols = class_mapper(obj.__class__).mapped_table.c
    columns = [col.name for col in mapped_cols]
    values = [getattr(obj, column) for column in columns]

    # Create a dictionary from columns and values
    return dict(zip(columns, values))




@blueprint.context_processor
def inject_user():
    return dict(current_user=current_user)

@blueprint.route('/index')
@login_required
def index():

    test_form = TestForm()
    all_tests = Tests.query.all()
    all_tools = Configs.query.all()
    return render_template('pages/dashboard.html', segment='index',form=test_form,tests=all_tests,tools=all_tools)



@blueprint.route('/nikto', methods=['POST'])
def nikto_data(test=None):
    if(test != None):
            #fetch config from db
            nikto_conf = Configs.query.filter_by(config_name='Nikto').first()
            nikto_dict=sql_dict(nikto_conf)
            test_dict=sql_dict(test)
          
            #create and start nikto scanning thread
            thread = Thread(target=nikto.run_test,args=[nikto_dict,test_dict])
            thread.start()

    if(request.method == "POST" and test==None):
        content = request.json
        test = Tests.query.get_or_404(content['test'])
        
        test.nikto_data = content
        db.session.commit()

    return "OK"

@blueprint.route('/nuclei', methods=['POST'])
def nuclei_data(test=None):
    if(test != None):
            #fetch config from db
            nuclei_conf = Configs.query.filter_by(config_name='Nuclei').first()
            nuclei_dict=sql_dict(nuclei_conf)
            test_dict=sql_dict(test)
          
            #create and start nuclei scanning thread
            thread = Thread(target=nuclei.run_test,args=[nuclei_dict,test_dict])
            thread.start()
            test.nuclei_data={'progress':0, 'status':"in progress", 'test':test['id'],'nuclei_data': ""}
            db.session.commit() 

    
    if(request.method == "POST" and test==None):
        content = request.json
        test = Tests.query.get_or_404(content['test'])
        
        test.nuclei_data = content
        db.session.commit()

    return "OK"



@blueprint.route('/zap', methods=['POST'])
def zap_data(test=None):
        if(test != None):
            #fetch config from db
            zapconf = Configs.query.filter_by(config_name='Zap').first()
            zap_dict=sql_dict(zapconf)
            test_dict=sql_dict(test)
          
            #create and start zap scanning thread
            thread = Thread(target=zap.run_test,args=[zap_dict,test_dict])
            thread.start()

        if(request.method == "POST" and test==None):
  
            content = request.json
            test = Tests.query.get_or_404(content['test'])
            test.zap_id=content['success']
            db.session.commit()        

        return "OK"



@blueprint.route('/burp', methods=['POST'])
def burp_data(test=None):

        if(test != None):
            #fetch config from db
            burpconf = Configs.query.filter_by(config_name='Burp Suite').first()
            burp_dict=sql_dict(burpconf)
            test_dict=sql_dict(test)
    
            #create and start burp scanning thread
            thread = Thread(target=burp.run_test,args=[burp_dict,test_dict])
            thread.start()

        if(request.method == "POST" and test==None):
  
            content = request.json
            test = Tests.query.get_or_404(content['test'])
            test.burp_id=content['success']
            db.session.commit()        

        return "OK"


@blueprint.route('/secretfinder', methods=['POST'])
def secretfinder_data(test=None):

        if(test != None):
            test_dict=sql_dict(test)
            #create and start secretfinder scanning thread
            thread = Thread(target=waybackcurl.start_secret_finder,args=[test_dict])
            thread.start()

        if(request.method == "POST" and test==None):
  
            content = request.json
            test = Tests.query.get_or_404(content['test'])
            test.secret_finder_data=content['secret_finder_data']
            db.session.commit()    
        return "OK"



@blueprint.route('/cmseek', methods=['POST'])
def cmseek_data(test=None):

        if(test != None):
            test_dict=sql_dict(test)
            #create and start cmseek scanning thread
            thread = Thread(target=cmseek.run_test,args=[test_dict])
            thread.start()
            test.cmseek_data=["in Progress",0,{}]
            db.session.commit() 
            

        if(request.method == "POST" and test==None):
  
            content = request.json
            test = Tests.query.get_or_404(content['test'])
            test.cmseek_data=content['cmseek_data']
            db.session.commit()    
        return "OK"

@blueprint.route('/cmsscan', methods=['POST'])
def cmsscan_data(test=None):

        if(test != None):
            test_dict=sql_dict(test)
            #create and start cmseek scanning thread
            thread = Thread(target=cmsscan.run_test,args=[test_dict])
            thread.start()
            test.cmsscan_data=["in Progress",0,{}]
            db.session.commit() 
            

        if(request.method == "POST" and test==None):
  
            content = request.json
            test = Tests.query.get_or_404(content['test'])
            test.cmsscan_data=content['cmsscan_data']
            db.session.commit()    
        return "OK"



@blueprint.route('/dork', methods=['POST'])
def dork_data(test=None):

        if(test != None):
            test_dict=sql_dict(test)
       
           
            #create and start dork scanning thread
            thread = Thread(target=dork.start_dork,args=[test_dict])
            thread.start()
            test.dork_data=["in Progress",0,{}]
        
            db.session.commit() 

        if(request.method == "POST" and test==None):

            content = request.json
            test = Tests.query.get_or_404(content['test'])
            test.dork_data=content['dork_data']
            db.session.commit() 
  
             
        return "OK"


@blueprint.route('/openvas', methods=['POST'])
def openvas_data(test=None):
    if(test != None):
            test_dict=sql_dict(test)
            #create and start openvas scanning thread
            openvas_conf = Configs.query.filter_by(config_name='Openvas').first()
            openvas_conf=sql_dict(openvas_conf)
           
            thread = Thread(target=openvas.run_test,args=[openvas_conf['config_endpoint'],test_dict])
            thread.start()
            test.openvas_data=["in Progress",0,{}]
            db.session.commit() 

    if(request.method == "POST" and test==None):

        content = request.json
        test = Tests.query.get_or_404(content['test'])
        test.openvas_data=content['openvas_data']
        test.openvas_id=str(content['report_id'])
        
        db.session.commit()    
    return "OK"

def check_progress(test):
    test_dict=sql_dict(test)


    #check burp_progress
    burpconf = Configs.query.filter_by(config_name='Burp Suite').first()
    burp_dict=sql_dict(burpconf)
    burp_progress = burp.check_status(burp_dict,test_dict)
    
    if(burp_progress.get("error") is not None):
        burp_progress=test.burp_data
    else:
        test.burp_data=burp_progress
        db.session.commit()


    #check zap progress
    zapconf = Configs.query.filter_by(config_name='Zap').first()
    zap_dict=sql_dict(zapconf)
    zap_progress = zap.check_status(zap_dict,test_dict)
    
   
    if(zap_progress.get("error") is not None or 'does_not_exist' in zap_progress['success']):
      
        zap_progress =  test.zap_data
       
    else:

        test.zap_data=zap_progress
        db.session.commit()

    
    #check nuclei progress
    nuclei_progress = test.nuclei_data

    if(nuclei_progress is None):
        nuclei_progress = {'progress':0, 'status':"In Progress", 'test':test.id,'nuclei_data':None}

    
    #check nikto progress
    nikto_progress = test.nikto_data

    if(nikto_progress is None):
            nikto_progress = {'progress':0, 'status':"In Progress", 'test':test.id,'nikto_data':None}



    #check secretfinder progress
    secretfinder_progress = test.secret_finder_data

    if(secretfinder_progress is None):
            secretfinder_progress = {'progress':0, 'status':"In Progress", 'test':test.id,'secretfinder_data':None}
    else:
            secretfinder_progress = {'progress':secretfinder_progress[1], 'status':secretfinder_progress[0], 'test':test.id,'secretfinder_data':secretfinder_progress[2]}


    #check cmsseek progress
    cmseek_progress = test.cmseek_data
    if(cmseek_progress is None):
            cmseek_progress = {'progress':0, 'status':"In Progress", 'test':test.id,'cmseek_data':None}
    else:
            cmseek_progress = {'progress':cmseek_progress[1], 'status':cmseek_progress[0], 'test':test.id,'cmseek_data':cmseek_progress[2]}



    #check cmsscan progress
    cmsscan_progress = test.cmsscan_data
    if(cmsscan_progress is None):
            cmsscan_progress = {'progress':0, 'status':"In Progress", 'test':test.id,'cmsscan_data':None}
    else:
            cmsscan_progress = {'progress':cmsscan_progress[1], 'status':cmsscan_progress[0], 'test':test.id,'cmsscan_data':json.loads(cmsscan_progress[2])}

    
     #check dork progress
    dork_progress = test.dork_data
    if(dork_progress is None):
            dork_progress = {'progress':0, 'status':"In Progress", 'test':test.id,'dork_data':None}
    else:
            dork_progress = {'progress':dork_progress[1], 'status':dork_progress[0], 'test':test.id,'dork_data':dork_progress[2]}


    openvas_progress = test.openvas_data
    if(openvas_progress is None):
            openvas_conf = Configs.query.filter_by(config_name='Openvas').first()
            openvas_conf=sql_dict(openvas_conf)
            openvas_data = openvas.check_progress(openvas_conf['config_endpoint'],test.openvas_id)
            openvas_progress = {'progress':0, 'status':"In Progress", 'test':test.id,'openvas_data':openvas_data}
            test.openvas_data = openvas_data
            db.session.commit()
    else:
            openvas_progress = {'progress':100, 'status':"Succeeded", 'test':test.id,'openvas_data':openvas_progress}
        
    
    return burp_progress,zap_progress,nuclei_progress,nikto_progress,secretfinder_progress,cmseek_progress,dork_progress,cmsscan_progress,openvas_progress


    

        

    


@blueprint.route('/test', methods=['GET', 'POST'])
@login_required
def tests():

    #get page data
    test_form = TestForm(request.form)
    all_tests = Tests.query.all()
    all_tools = Configs.query.all()

    if 'create_test' in request.form:

        #create a new db entry for test
        test_name = request.form['test_name']
        test_url = request.form['test_url']
        site_username = request.form['site_username']
        site_password = request.form['site_password']


        new_test = Tests(
            test_name=test_name,
            test_url=test_url,
            site_username=site_username,
            site_password=site_password  
        )

        db.session.add(new_test)
        db.session.commit()
       
        if('Burp' in request.form):
            #start burpsuite test   
            burp_data(new_test)
            
        if('Nessus' in request.form):
            print('Nessus')

        if('Nuclei' in request.form):
            #start nuclei test
            nuclei_data(new_test)

        if('Zap' in request.form):
            #start zap test
            zap_data(new_test)
            
        if('Nikto' in request.form):
            #start nikto test
            nikto_data(new_test)

        if('Secret' in request.form):
            #start secret finder test
            secretfinder_data(new_test)

        if('CMSSeek' in request.form):
           cmseek_data(new_test)
        
        if('CMSScan' in request.form):
            cmsscan_data(new_test)
        
        if('Google' in request.form):
            dork_data(new_test)

        if('Openvas' in request.form):
            openvas_data(new_test)
        


        all_tools = Configs.query.all()
        all_tests = Tests.query.all()



        
    if 'delete' in request.form:
    
        test_id = request.form['delete']
        test_to_delete = Tests.query.get_or_404(test_id)
        db.session.delete(test_to_delete)
        db.session.commit()
        all_tests = Tests.query.all()
        return render_template('pages/dashboard.html', segment='index',form=test_form, succ="Test has been Deleted", tests=all_tests,tools=all_tools)
    


    if 'details' in request.form:
        test_id = request.form['details']
        test = Tests.query.get_or_404(test_id)


        burp_progress=""
        zap_progress=""
        nikto_progress=""
        nuclei_progress=""
        nessus_progress=""
        secretfinder_progress=""
        cmseek_progress=""
        cmsscan_progress=""
        openvas_progress=""

        burp_progress,zap_progress,nuclei_progress,nikto_progress,secretfinder_progress,cmseek_progress,dork_progress,cmsscan_progress,openvas_progress = check_progress(test)

        all_tools = Configs.query.all()

        return render_template('pages/detail.html',  test=test,tools=all_tools,progress=burp_progress,zap_progress=zap_progress,nuclei_progress=nuclei_progress,nikto_progress=nikto_progress,secretfinder_progress=secretfinder_progress,cmseek_progress=cmseek_progress,dork_progress=dork_progress,cmsscan_progress=cmsscan_progress,openvas_progress=openvas_progress)



    return render_template('pages/dashboard.html', segment='index',form=test_form, tests=all_tests, tools=all_tools)







# @blueprint.route('/typography')
# @login_required
# def typography():
#     return render_template('pages/typography.html')

# @blueprint.route('/color')
# @login_required
# def color():
#     return render_template('pages/color.html')

# @blueprint.route('/icon-tabler')
# @login_required
# def icon_tabler():
#     return render_template('pages/icon-tabler.html')

# @blueprint.route('/sample-page')
# @login_required
# def sample_page():
#     return render_template('pages/sample-page.html')  

@blueprint.route('/accounts/password-reset/')
def password_reset():
    return render_template('accounts/password_reset.html')

@blueprint.route('/accounts/password-reset-done/')
def password_reset_done():
    return render_template('accounts/password_reset_done.html')

@blueprint.route('/accounts/password-reset-confirm/')
def password_reset_confirm():
    return render_template('accounts/password_reset_confirm.html')

@blueprint.route('/accounts/password-reset-complete/')
def password_reset_complete():
    return render_template('accounts/password_reset_complete.html')

@blueprint.route('/accounts/password-change/')
def password_change():
    return render_template('accounts/password_change.html')

@blueprint.route('/accounts/password-change-done/')
def password_change_done():
    return render_template('accounts/password_change_done.html')

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
