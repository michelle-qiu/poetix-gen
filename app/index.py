from flask_wtf import FlaskForm
from flask import render_template,flash
from datetime import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required
from .templates.Poetix_Sonnets.gen_poem_script import *
from flask import Blueprint
bp = Blueprint('index', __name__)
import re
class Poem(FlaskForm):
	theme=StringField("Choose a theme word")
	#recaptcha = RecaptchaField(u'Recaptcha')
	submit=SubmitField("generate")

@bp.route('/', methods=['GET', 'POST'])
def generate():
	search = Poem()
	if search.validate_on_submit():
		start= datetime.now()
		start = start.strftime("%H:%M:%S")
		q = search.theme.data
		poem = get_poem(q)
		poem = re.sub(r'(\([^)]*\))\n','\n',poem)
		poem = re.split(r'\n', poem)
		s1 = poem[0:4]
		s2=poem[4:9]
		s3=poem[9:13]
		s4=poem[13:15]
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		return render_template('index.html',s1=s1,s2=s2,s3=s3,s4=s4,form=search,starttime=start,time=current_time)		
	return render_template('index.html',form=search)
