from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {'content': '내용'}

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['content'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "내용을 입력하세요.",
            'rows': 3
        }