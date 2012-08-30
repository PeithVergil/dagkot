from wtforms import BooleanField, Form, SelectField, TextAreaField, TextField, validators

class AddForm(Form):
	dagkot_type = SelectField('Dagkot Type', choices=[
		('Thanks giving for', 'Thanks giving for'),
		('Happy birthday to', 'Happy birthday to'),
		('Congratulations to', 'Congratulations to'),
		('In memory of', 'In memory of'),
		('Prayer for', 'Prayer for')
	])

	dagkot_for = TextField('Dagkot For', [
		validators.required(message='The text field above is required.'),
		validators.length(max=255)
	])

	dagkot_msg = TextAreaField('Dagkot Message', [
		validators.required(message='Enter a short message or prayer.')
	])

	dagkot_img = BooleanField('Upload images for this dagkot.', default=True)