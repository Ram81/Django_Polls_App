from django import forms
from dashboard.models import User

class CreateInterview(forms.Form):
	"""docstring for CreateInterview"""
	users = User.objects.all()
	Choices = []
	for o in users:
		Choices.append((o.id, o.candidate_email))
	interviewer_email = forms.MultipleChoiceField(label='Interviewer Email', widget=forms.CheckboxSelectMultiple(), choices=Choices)
	candidate_email = forms.ChoiceField(choices=Choices)
	start_time = forms.TimeField(label='Interview Start Time', widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'hh:mm format'}))
	end_time = forms.TimeField(label='Interview End Time', widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'hh:mm format'}))
	date = forms.DateField(widget=forms.SelectDateWidget(years=[y for y in range(2018, 2025)]), label='Interview Date')

	# check for start time less than end time of interview
	#def clean_end_time(self):
	#	if (self.cleaned_data['start_time']>self.cleaned_data['end_time']):
	#		raise forms.ValidationError("Start time must be before end time")
	#	return self.cleaned_data['end_time']


class EditInterview(forms.Form):
	interviewer_email = forms.EmailField(label='Interviewer Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter interviewer email'}), max_length=200)
	candidate_email = forms.EmailField(label='Candidate Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter Candidate Email'}), max_length=200)
	start_time = forms.TimeField(label='Interview Start Time', widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'hh:mm format'}))
	end_time = forms.TimeField(label='Interview End Time', widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'hh:mm format'}))
	date = forms.DateField(widget=forms.SelectDateWidget(years=[y for y in range(2018,2025)]), label='Interview Date')

    # check for start time less than end time of interview
	#def clean_end_time(self):
	#	if (self.cleaned_data['start_time']>self.cleaned_data['end_time']):
	#		raise forms.ValidationError("Start time must be before end time")
	#	return self.cleaned_data['end_time']
