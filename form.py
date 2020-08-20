from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddCupcake(FlaskForm):
    flavor = StringField("Cupcake Flavor", validators=[
                         InputRequired(message="Cupcake Flavor is Required")])
    size = SelectField("Cupcake Size", choices=[
                       ('s', 'Small'), ('m', 'Medium'), ('l', 'Large'), ('xl', 'Extra Large')])
