from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class SituationForm(FlaskForm):
    en = StringField('English', validators=[DataRequired()])
    ru = StringField('Russian', validators=[DataRequired()])
    kz = StringField('Kazakh', validators=[DataRequired()])
    animation = StringField('Animation File', validators=[DataRequired()])
    situation_id = IntegerField('Situation ID', validators=[DataRequired()])

class SentenceForm(FlaskForm):
    en = StringField('English', validators=[DataRequired()])
    kz = StringField('Kazakh', validators=[DataRequired()])
    ru = StringField('Russian', validators=[DataRequired()])
    audio = StringField('Audio File')
    situation_id = IntegerField('Situation ID', validators=[DataRequired()])
