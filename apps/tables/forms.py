from  django import forms
from datetime import datetime
from time import time
from bootstrap_datepicker_plus import DateTimePickerInput

class TableFilterForm(forms.Form):
    rdate = forms.DateField(required=True)
    rtime = forms.TimeField(required=True)
