from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, PasswordField, Field, StringField, RadioField 
from wtforms.validators import DataRequired, Length, EqualTo


class ScanForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired(), Length(3, 63)])
    submit = SubmitField("Start scan")
    scan = RadioField('Scan Type', choices=[('passive','Passive scan'),('full','Full scan')])
