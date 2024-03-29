from django import forms
from .models import TodoList, TodoItem


class ListCreateForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ['title', 'description']

        labels = {
            "title": "Title",
            "description": "Description",
        }


class ItemCreateForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ['itemOf', 'deadline', 'content']

        labels = {
            "itemOf": "List",
            "deadline": "Deadline (dd-mm-yyyy)",
            "content": "Description",
        }

    def __init__(self, user, *args, **kwargs):
        super(ItemCreateForm, self).__init__(*args, **kwargs)
        self.fields['itemOf'].queryset = TodoList.objects.filter(creator=user)
        self.fields['deadline'].input_formats = ['%d-%m-%Y']
