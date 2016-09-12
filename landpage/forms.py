from django.forms import ModelForm
from landpage.models import Comments

class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ['comments_text']