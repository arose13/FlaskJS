from flask_wtf import FlaskForm
from wtforms import StringField, validators


class RandomForm(FlaskForm):
    first_name = StringField(
        'First Name',
        [validators.InputRequired('Give me a name!'), validators.Length(min=3)]
    )

    last_name = StringField(
        'Last Name',
        [validators.InputRequired('Give me a surname!')]
    )
