from django import forms

class CreateInterview(forms.Form):
	"""docstring for CreateInterview"""
	interviewer_email = forms.EmailField(label='Interviewer Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter interviewer email'}), max_length=200)
	candidate_email = forms.EmailField(label='Candidate Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter candidate email'}), max_length=200)
	start_time = forms.TimeField(label='Interview Start Time', widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'hh:mm format'}))
	end_time = forms.TimeField(label='Interview End Time', widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'hh:mm format'}))
	date = forms.DateField(widget=forms.SelectDateWidget(years=[y for y in range(2018, 2025)]), label='Interview Date')

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

	#def clean_end_time(self):
	#	if (self.cleaned_data['start_time']>self.cleaned_data['end_time']):
	#		raise forms.ValidationError("Start time must be before end time")
	#	return self.cleaned_data['end_time']
