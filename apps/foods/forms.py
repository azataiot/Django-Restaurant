from django import forms
from cafe.models import Tamaq



class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
