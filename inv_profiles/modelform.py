from django.forms import ModelForm
from .models import Profile, Report, BrokerAnalysis, RevenueIncomeSources
from .models import Risk, Competitor, Transaction, KeyMetric, Segment
from django.forms import TextInput, Select, Textarea, DateInput


class NewProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['company']
        widgets = {
            'company': TextInput(attrs={'class': 'form-control'}),
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'company': TextInput(attrs={'class': 'form-control'}),
            'exchange': Select(attrs={'class': 'form-control'}),
            'ticker': TextInput(attrs={'class': 'form-control'}),
            'rating': Select(attrs={'class': 'form-control'}),
            'investment_decision': Select(attrs={'class': 'form-control'}),
            'tech_analysis_opinion': Select(attrs={'class': 'form-control'}),
            'fundamental_analysis_opinion': Select(attrs={'class': 'form-control'}),
            'investment_type': Select(attrs={'class': 'form-control'}),
            'investment_status': Select(attrs={'class': 'form-control'}),
            'stock_momentum': Select(attrs={'class': 'form-control'}),
            'entry_strategy': TextInput(attrs={'class': 'form-control'}),
            'exit_strategy': TextInput(attrs={'class': 'form-control'}),
            'general_notes': Textarea(attrs={'class': 'form-control'}),
        }


class EditReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'


class BrokerAnalysisForm(ModelForm):
    class Meta:
        model = BrokerAnalysis
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': "form-control"}),
            'broker': TextInput(attrs={'class': "form-control"}),
            'analyst': TextInput(attrs={'class': "form-control"}),
            'summary': TextInput(attrs={'class': "form-control"}),
            'link': TextInput(attrs={'class': "form-control"}),
            'profile': Select(attrs={'class': "form-control"}),
        }


class RevenueSourceForm(ModelForm):
    class Meta:
        model = RevenueIncomeSources
        fields = '__all__'
        widgets = {
            'type_of_source': Select(attrs={'class': "form-control"}),
            'source_frequency': Select(attrs={'class': "form-control"}),
            'description': TextInput(attrs={'class': "form-control"}),
        }


class KeyMetricForm(ModelForm):
    class Meta:
        model = KeyMetric
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': "form-control"}),
            'type_of_metric': TextInput(attrs={'class': "form-control"}),
            'description': TextInput(attrs={'class': "form-control"}),
            'link': TextInput(attrs={'class': "form-control"}),
        }


class RiskForm(ModelForm):
    class Meta:
        model = Risk
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': "form-control"}),
            'rating': Select(attrs={'class': "form-control"}),
            'notes': TextInput(attrs={'class': "form-control"}),
        }


class SegmentForm(ModelForm):
    class Meta:
        model = Segment
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': "form-control"}),
            'description': TextInput(attrs={'class': "form-control"}),
            'part_of_revenue': TextInput(attrs={'class': "form-control"}),
        }


class CompetitorForm(ModelForm):
    class Meta:
        model = Competitor
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': "form-control"}),
            'competitor_impact': Select(attrs={'class': "form-control"}),
        }


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'type_of_transaction': Select(attrs={'class': "form-control"}),
            'amount': TextInput(attrs={'class': "form-control"}),
            'date_of_transaction': DateInput(attrs={'class': "form-control"}),
        }


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': "form-control"}),
            'report_type': Select(attrs={'class': "form-control"}),
            'description': TextInput(attrs={'class': "form-control"}),
            'link': TextInput(attrs={'class': "form-control"}),
            'profile': Select(attrs={'class': "form-control"}),
        }
