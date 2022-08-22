from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, TextAreaField, ValidationError, IntegerField
from wtforms.validators import DataRequired, AnyOf, URL, Length, NumberRange, Regexp
import phonenumbers


def ValidatorChoices(choices, message = 'Invalid choice selected'):
    def _validator(field):
        choices_values = [choice[1] for choice in choices]
        if isinstance(field.data, str):
            if field.data not in choices_values:
                raise ValidationError(message)
        else:
            for value in field.data:
                if value not in choices_values:
                    raise ValidationError(message)

    return _validator

def ValidatorPhone():
    #   Ref: this code was taken from stackoverflow.
    #   https://stackoverflow.com/questions/36251149/validating-us-phone-number-in-wtforms
    #
    def _validate_phone(field):
        if len(field.data) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            try:
                input_number = phonenumbers.parse("+1"+field.data)
                if not (phonenumbers.is_valid_number(input_number)):
                    raise ValidationError('Invalid phone number.')
            except:
                raise ValidationError('Invalid phone number.')
        return None

    return _validate_phone;


state_choices=[
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]

genre_choices=[
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]


class ShowForm(Form):
    artist_id = IntegerField(
        'artist_id', validators=[DataRequired(), NumberRange(min=1, message="ID cannot be negative or string")]
    )
    venue_id = IntegerField(
        'venue_id', validators=[DataRequired(), NumberRange(min=1, message="ID cannot be negative or string")]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.now()
    )

facebook_regex = "((http|https):\/\/|)(www\.|)facebook\.com\/[a-zA-Z0-9.]{1,}"
facebook_invalid_message = "Facebook URL is Invalid"


class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired(), Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired(), ValidatorChoices(choices=state_choices, message='Invalid State')],
        choices=state_choices
    )
    address = StringField(
        'address', validators=[DataRequired(), Length(max=120)]
    )
    phone = StringField(
        'phone', validators=[ValidatorPhone()]
    )
    image_link = StringField(
        'image_link', validators=[URL(), Length(max=500)]
    )
    genres = SelectMultipleField(

        # ToDo implement enum restriction
        'genres', validators=[DataRequired(), ValidatorChoices(choices=genre_choices, message='Invalid Genre')],
        choices=genre_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(), Length(max=120), Regexp(regex=facebook_regex, message=facebook_invalid_message)]
    )
    website = StringField(
        'website', validators=[URL(), Length(max=120)]
    )
    seeking_talent = BooleanField(
        'seeking_talent'
    )
    seeking_description = TextAreaField(
        'seeking_description', validators=[Length(max=500)]
    )
    image_link = StringField(
        'image_link', validators=[URL(), Length(max=500)]
    )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired(), Length(max=120)]
    )
    state = SelectField(
        # ToDo implement validation logic for state
        'state', validators=[DataRequired(), ValidatorChoices(choices=state_choices, message='Invalid State')],
        choices=state_choices
    )
    phone = StringField(
        'phone', validators=[ValidatorPhone()]
    )
    image_link = StringField(
        'image_link', validators=[Length(max=120)]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired(), ValidatorChoices(choices=genre_choices, message='Invalid Genre')],
        choices=genre_choices
    )
    facebook_link = StringField(
        # ToDo implement enum restriction
        'facebook_link', validators=[URL(), Length(max=120), Regexp(regex=facebook_regex, message=facebook_invalid_message)]
    )
    website = StringField(
        'website', validators=[URL(), Length(max=120)]
    )
    seeking_venue = BooleanField(
        'seeking_venue'
    )
    seeking_description = TextAreaField(
        'seeking_description', validators=[Length(max=500)]
    )
    image_link = StringField(
        'image_link', validators=[URL(), Length(max=500)]
    )