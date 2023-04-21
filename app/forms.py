from django import forms

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=30)


class WebpageForm(forms.Form):
    topic_name=forms.CharField(max_length=30)
    NAME=forms.CharField(max_length=30)
    email=forms.EmailField()