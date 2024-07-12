from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'feature_image', 'demo_link', 'source_link', 'tags']
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),  # Use CheckboxSelectMultiple for tags
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})  # Add "input" class to all fields

        # Optional enhancements:

        # Add placeholder text to specific fields
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter Project Title'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Describe Your Project'})

        # Make specific fields required (if needed)
        self.fields['title'].required = True
        self.fields['description'].required = True
