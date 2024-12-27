from django.forms import ModelForm, Form, ChoiceField, FileInput

from .models import Thread, Post 

class PostForm (ModelForm):

    class Meta:
        model = Post
        fields = ('thread', 'content', 'post_pic')
        widgets = {'post_pic': FileInput()}

class ThreadForm (ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'topic')