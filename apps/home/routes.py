# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, url_for, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps import db

from apps.home.forms import TestForm
from apps.home.models import Tests

@blueprint.route('/index')
@login_required
def index():
    test_form = TestForm()
    all_tests = Tests.query.all()
    return render_template('pages/dashboard.html', segment='index',form=test_form,tests=all_tests)


@blueprint.route('/test', methods=['GET', 'POST'])
@login_required
def tests():
    test_form = TestForm(request.form)
    all_tests = Tests.query.all()
    
    print(request.form)
    if 'create_test' in request.form:
        test_name = request.form['test_name']
        test_url = request.form['test_url']
        site_username = request.form['site_username']
        site_password = request.form['site_password']


        new_test = Tests(
            test_name=test_name,
            test_url=test_url,
            site_username=site_username,
            site_password=site_password  # You should hash the password before storing it
        )

        db.session.add(new_test)
        db.session.commit()

        all_tests = Tests.query.all()

        return render_template('pages/dashboard.html', segment='index',form=test_form, succ="New Test has been added", tests=all_tests)

    if 'delete' in request.form:
    
        test_id = request.form['delete']
        test_to_delete = Tests.query.get_or_404(test_id)
        db.session.delete(test_to_delete)
        db.session.commit()
        all_tests = Tests.query.all()
        return render_template('pages/dashboard.html', segment='index',form=test_form, succ="Test has been Deleted", tests=all_tests)




    return render_template('pages/dashboard.html', segment='index',form=test_form, tests=all_tests)





@blueprint.route('/typography')
@login_required
def typography():
    return render_template('pages/typography.html')

@blueprint.route('/color')
@login_required
def color():
    return render_template('pages/color.html')

@blueprint.route('/icon-tabler')
@login_required
def icon_tabler():
    return render_template('pages/icon-tabler.html')

@blueprint.route('/sample-page')
@login_required
def sample_page():
    return render_template('pages/sample-page.html')  

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
