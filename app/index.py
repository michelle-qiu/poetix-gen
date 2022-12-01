from flask_wtf import FlaskForm
from flask import render_template,flash
from datetime import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField,SelectField
from wtforms.validators import Required
from .templates.Poetix_Sonnets.gen_poem_script import *
from flask import Blueprint
bp = Blueprint('index', __name__)
import re
class Poem(FlaskForm):
	theme=StringField("Choose a theme word")
	rhyme=BooleanField("rhyme lines", default = True)
	theme_lines=SelectField('Seed with', choices=['0', 'poem','stanza'], default="0")
	k=IntegerField("Best k samples per line",default=5)
	alliteration = IntegerField("Number of lines to alliterate per stanza",default="1")
	#recaptcha = RecaptchaField(u'Recaptcha')
	submit=SubmitField("generate")

@bp.route('/', methods=['GET', 'POST'])
def generate():
	search = Poem()
	if search.validate_on_submit():
		start= datetime.now()
		start = start.strftime("%H:%M:%S")
		theme = search.theme.data
		rhyme=search.rhyme.data
		theme_lines=search.theme_lines.data
		k=search.k.data
		alliteration=search.alliteration.data
		poem = get_poem(theme,rhyme,theme_lines,k,alliteration)
		poem = re.sub(r'(\([^)]*\))\n','\n',poem)
		poem = re.split(r'\n', poem)
		s1 = poem[0:4]
		s2=poem[4:9]
		s3=poem[9:14]
		s4=poem[13:16]
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		return render_template('index.html',s1=s1,s2=s2,s3=s3,s4=s4,form=search,starttime=start,time=current_time)		
	return render_template('index.html',form=search)
