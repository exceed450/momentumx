from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, URLInput
from .models import InvestmentIdea, IdeaComment, PlanComment


class InvestmentIdeaForm(ModelForm):
    class Meta:
        model = InvestmentIdea
        fields = ['title', 'picture_or_video_URL', 'description']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'picture_or_video_URL':URLInput(attrs={'class': 'form-control'}),
        }


class IdeaCommentForm(ModelForm):
    class Meta:
        model = IdeaComment
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={'class': 'form-control',
                                       'rows': 5}),
        }


class PlanCommentForm(ModelForm):
    pass
