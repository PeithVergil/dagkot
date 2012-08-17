from wtforms import Form, SelectField, TextAreaField, TextField, validators

class AddForm(Form):
	dagkot_type = SelectField('Dagkot Type', choices=[
		('Thanks giving for', 'Thanks giving for'),
		('Happy birthday to', 'Happy birthday to'),
		('Prayer for', 'Prayer for')
	])

	dagkot_for = TextField('Dagkot For', [
		validators.required(message='The text field above is required.'),
		validators.length(max=255)
	])

	dagkot_msg = TextAreaField('Dagkot Message', [
		validators.required(message='Enter a short message or prayer.')
	])