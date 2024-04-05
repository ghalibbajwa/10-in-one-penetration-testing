

from apps.configs import blueprint
from flask import render_template, request, url_for, redirect
from flask_login import login_required,current_user
from jinja2 import TemplateNotFound
from apps import db

from apps.configs.models import Configs
from apps.configs.forms import BurpForm,NessusForm,ZapForm,NucleiForm,ConfigForm








@blueprint.route('/configs', methods=['GET', 'POST'])
@login_required
def index():

  


    burp = Configs.query.filter_by(config_name='Burp Suite').first()
    if not burp:
        burp = Configs(
                    config_name='Burp Suite',
                    config_endpoint='http://127.0.0.1:1337',
                    config_api_key="Ouddp3chhxLVtyNNAwYIqoqFdE1JZaEn"
                )

        db.session.add(burp)
        db.session.commit()
    

    nessus = Configs.query.filter_by(config_name='Nessus').first()
    if not nessus:
        nessus = Configs(
                    config_name='Nessus',
                    config_endpoint='https://localhost:8834',
                    config_username="admin",
                    config_password = "admin"
                )

        db.session.add(nessus)
        db.session.commit()

    nuclei = Configs.query.filter_by(config_name='Nuclei').first()
    if not nuclei:
        nuclei = Configs(
                    config_name='Nuclei',
                    config_path="C:/nuclei_3.1.10_windows_amd64"
                )

        db.session.add(nuclei)
        db.session.commit()

    
    nikto = Configs.query.filter_by(config_name='Nikto').first()
    if not nikto:
        nikto = Configs(
                    config_name='Nikto',
                    config_path="C:/nikto-master/program/nikto.pl"
                )

        db.session.add(nikto)
        db.session.commit()

    sfinder = Configs.query.filter_by(config_name='Secret Finder').first()
    if not sfinder:
        sfinder = Configs(
                    config_name='Secret Finder'
                )

        db.session.add(sfinder)
        db.session.commit()

    
    gdorks = Configs.query.filter_by(config_name='Google Dorks').first()
    if not gdorks:
        gdorks = Configs(
                    config_name='Google Dorks'
                )

        db.session.add(gdorks)
        db.session.commit()

    cmsseek = Configs.query.filter_by(config_name='CMSSeek').first()
    if not cmsseek:
        cmsseek = Configs(
                    config_name='CMSSeek'
                )

        db.session.add(cmsseek)
        db.session.commit()
    

    cmsscan = Configs.query.filter_by(config_name='CMSScan').first()
    if not cmsscan:
        cmsscan = Configs(
                    config_name='CMSScan'
                )

        db.session.add(cmsscan)
        db.session.commit()


    zap = Configs.query.filter_by(config_name='Zap').first()
    if not zap:
        zap = Configs(
                    config_name='Zap',
                    config_endpoint='http://127.0.0.1:8080',
                    config_api_key="sauhu8602obv3fr8oh58dhrh4s"
                )

        db.session.add(zap)
        db.session.commit()




 
    

   
    form=ConfigForm()


    print(request.form)
    if 'save_config' in request.form:
        config = Configs.query.filter_by(config_name=request.form['config_name']).first()

        if 'config_endpoint' in request.form:
            config.config_endpoint=request.form['config_endpoint']
        if 'config_api_key' in request.form:
            config.config_api_key=request.form['config_api_key']
        if 'config_path' in request.form:
            config.config_path=request.form['config_path']
        if 'config_username' in request.form:
            config.config_username=request.form['config_username']
        if 'config_password' in request.form:
            config.config_password=request.form['config_password']
        
        db.session.commit()
        all_configs = Configs.query.all()
        return render_template('pages/config.html',configs=all_configs,form=form,succ=[request.form['config_name'],"Configuration Updated"])

      
    all_configs = Configs.query.all()
    
    return render_template('pages/config.html',configs=all_configs,form=form)

