from django import forms
from .models import Question,Choices

class QuestionForm(forms.ModelForm):
    choices=forms.CharField(max_length=200,help_text='Type your choices for the poll separated by commas',
                            label='Choices')
    class Meta:
        model=Question
        fields=['question']
    def save(self, commit=True):
        question=super().save(commit=False)
        if commit:
            question.save()
            choices_text=self.cleaned_data['choices']
            choices_list=[choice.strip() for choice in choices_text.split(',')]
            for choices_text in choices_list:
                Choices.objects.create(question=question,choices=choices_text)
        return question