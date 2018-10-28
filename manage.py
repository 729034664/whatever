import os
from app import create_app, db
from app.models import User,Role
from flask_script import Manager, Shell
from flask_migrate import Migrate,MigrateCommand
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import Flask,render_template,session,  url_for, flash
from flask import redirect
from datetime import datetime
from flask_mail import Mail, Message
from threading import Thread
from flask_login import login_required

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
mail = Mail(app)

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    '''run the unit tests.'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

class NameForm(FlaskForm):
    name = StringField('输入姓名点击提交', validators=[Required()])
    submit = SubmitField('提交')

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject,template, **kwargs):
    msg = Message(app.config['FLASKY_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/secret')
@login_required
def secret():
    return '只允许认证用户访问'

if __name__ == '__main__':
    manager.run()