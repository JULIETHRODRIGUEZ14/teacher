from django import forms
#permite que una clse se extienda para despues convertirse en un formulario html


class CreateNewTask(forms.Form):
    titles = forms.CharField(label ="Titulo de tarea", max_length=200)
    description = forms.Textarea()