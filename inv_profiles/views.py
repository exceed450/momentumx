from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .modelform import NewProfileForm, EditProfileForm
from .modelform import BrokerAnalysisForm, RevenueSourceForm
from .modelform import KeyMetricForm, RiskForm, SegmentForm
from .modelform import CompetitorForm, TransactionForm, ReportForm
from .models import Profile, BrokerAnalysis, RevenueIncomeSources
from .models import KeyMetric, Risk, Segment, Competitor, Transaction
from .models import Report
from user_management.views import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging

alpha_vantage_key = "78JXG3F5951085OL"
logging = logging.getLogger(__name__)


def profiles(request):
    """
    Landing page for inv_profiles application.
    Show all investment profiles
    """
    if request.user.is_authenticated:
        authenticated = True
        investment_profiles = Profile.objects.filter(user=request.user)
    else:
        authenticated = False
        investment_profiles = {}

    return render(request, 'inv_profiles/profiles.html',
                  {'investment_profiles': investment_profiles,
                   'authenticated': authenticated})


def add_profile(request):
    form = NewProfileForm()
    success = False
    user = request.user

    if request.POST and request.user.is_authenticated:
        form = NewProfileForm(request.POST)
        authenticated = True

        if form.is_valid:
            print("add_profile: form is valid")
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            success_created = True
            investment_profiles = Profile.objects.filter(user=user)

            return render(request, 'inv_profiles/profiles.html',
                            {'investment_profiles': investment_profiles,
                             'success_created': success_created,
                             'authenticated': authenticated})
        else:
            print("add_profile: form is NOT valid")
            print(form.errors)
    elif request.user.is_authenticated:
        authenticated = True
        return render(request, 'inv_profiles/add_profile.html',
                      {'form': form,
                       'authenticated': authenticated})

    authenticated = False
    return render(request, 'inv_profiles/add_profile.html',
                  {'form': form,
                   'authenticated': authenticated})


def view_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    # Fetch all information for the investment profile
    analysis = BrokerAnalysis.objects.all()
    revenue_sources = RevenueIncomeSources.objects.all()
    key_metrics = KeyMetric.objects.all()
    risks = Risk.objects.all()
    segments = Segment.objects.all()
    competitors = Competitor.objects.all()
    transactions = Transaction.objects.all()
    reports = Report.objects.all()

    return render(request, 'inv_profiles/view_profile.html',
                  {'analysis': analysis,
                   'key_metrics': key_metrics,
                   'risks': risks,
                   'revenue_sources': revenue_sources,
                   'segments': segments,
                   'reports': reports,
                   'competitors': competitors,
                   'transactions': transactions,
                   'profile': profile})


def edit_profile(request, profile_id, *kwargs):
    profile = Profile.objects.get(id=profile_id)

    if request.POST:
        profile = EditProfileForm(request.POST, instance=profile)
        if profile.is_valid():
            updated_profile = profile.save(commit=False)
            updated_profile.user = request.user
            updated_profile.save()
            return HttpResponseRedirect(reverse('inv_profiles:view_profile', args=([profile_id])))
        else:
            profile = EditProfileForm(request.POST)
            print(profile.errors)
            return HttpResponseRedirect(reverse('inv_profiles:edit_profile', args=([profile_id])))

    # Fetch all information for the investment profile
    analysis = BrokerAnalysis.objects.all()
    revenue_sources = RevenueIncomeSources.objects.all()
    key_metrics = KeyMetric.objects.all()
    risks = Risk.objects.all()
    segments = Segment.objects.all()
    competitors = Competitor.objects.all()
    transactions = Transaction.objects.all()
    reports = Report.objects.all()

    # Provide the form for adding new entries to 
    # each of the different subjects instead of 
    # going to a new page
    analysis_form = BrokerAnalysisForm()
    revenue_source_form = RevenueSourceForm()
    key_metric_form = KeyMetricForm()
    risk_form = RiskForm()
    segment_form = SegmentForm()
    competitor_form = CompetitorForm()
    transaction_form = TransactionForm()
    report_form = ReportForm()

    # This is the main form for editing the investment profile
    form = EditProfileForm(instance=profile)

    return render(request, 'inv_profiles/edit_profile.html',
                  {'form': form,
                   'analysis_form': analysis_form,
                   'revenue_source_form': revenue_source_form,
                   'key_metric_form': key_metric_form,
                   'risk_form': risk_form,
                   'segment_form': segment_form,
                   'competitor_form': competitor_form,
                   'report_form': report_form,
                   'transaction_form': transaction_form,
                   'analysis': analysis,
                   'key_metrics': key_metrics,
                   'risks': risks,
                   'revenue_sources': revenue_sources,
                   'segments': segments,
                   'reports': reports,
                   'competitors': competitors,
                   'transactions': transactions,
                   'profile': profile})


##########################################
# MANAGE INFORMATION FOR A PROFILE           #
##########################################


def manage_reports(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    report_form = ReportForm()
    all_reports = Report.objects.filter(profile=profile)
    paginator = Paginator(all_reports, 5)
    page = request.GET.get('page', 1)

    try:
        all_elements = paginator.page(page)
    except PageNotAnInteger:
        all_elements = paginator.page(1)
    except EmptyPage:
        all_elements = paginator.page(paginator.num_pages)

    return render(request, 'inv_profiles/manage/manage_reports.html',
                  {'profile': profile,
                   'form': report_form,
                   'all_elements': all_elements})


def manage_analysis(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    analysis_form = BrokerAnalysisForm()
    all_elements = BrokerAnalysis.objects.filter(profile=profile)

    return render(request, 'inv_profiles/manage/manage_analysis.html',
                  {'profile': profile,
                   'form': analysis_form,
                   'all_elements': all_elements})


def manage_revenue_sources(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    revenue_source_form = RevenueSourceForm()
    all_rev_sources = RevenueIncomeSources.objects.filter(profile=profile)

    return render(request, 'inv_profiles/manage/manage_revenue_sources.html',
                  {'profile': profile,
                   'form': revenue_source_form,
                   'all_elements': all_rev_sources})


def manage_business_segments(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    business_segment_form = SegmentForm()
    all_elements = Segment.objects.filter(profile=profile)

    return render(request, 'inv_profiles/manage/manage_segments.html',
                  {'profile': profile,
                   'form': business_segment_form,
                   'all_elements': all_elements})


def manage_competitors(request, profile_id):
    logging.info("manage_competitors: function running...")
    profile = Profile.objects.get(id=profile_id)
    competitor_form = CompetitorForm()
    all_elements = Competitor.objects.filter(profile=profile)

    logging.info("sending http response...")
    return render(request, 'inv_profiles/manage/manage_competitors.html',
                  {'profile': profile,
                   'form': competitor_form,
                   'all_elements': all_elements})


def manage_metrics(request, profile_id):
    logging.info("manage_metrics: function running...")
    profile = Profile.objects.get(id=profile_id)
    metric_form = KeyMetricForm()
    all_elements = KeyMetric.objects.filter(profile=profile)
    logging.info("manage_metrics: fetched all objects, sending http response...")

    return render(request, 'inv_profiles/manage/manage_metrics.html',
                  {'profile': profile,
                   'form': metric_form,
                   'all_elements': all_elements})


def manage_risks(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    risk_form = RiskForm()
    all_elements = Risk.objects.filter(profile=profile)

    return render(request, 'inv_profiles/manage/manage_risks.html',
                  {'profile': profile,
                   'form': risk_form,
                   'all_elements': all_elements})


def manage_transactions(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    tx_form = TransactionForm()
    all_elements = Transaction.objects.filter(profile=profile)

    return render(request, 'inv_profiles/manage/manage_transactions.html',
                  {'profile': profile,
                   'form': tx_form,
                   'all_elements': all_elements})


##########################################
# DELETE INFORMATION TO A PROFILE           #
##########################################


def delete_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    success_deleted = False
    if profile.delete():
        success_deleted = True

    investment_profiles = Profile.objects.all()
    return render(request, 'inv_profiles/profiles.html',
                  {'investment_profiles': investment_profiles,
                   'success_deleted': success_deleted})


def delete_report(request, profile_id, report_id):
    Report.objects.get(id=report_id).delete()
    return HttpResponseRedirect(reverse('inv_profiles:manage_reports', kwargs={'profile_id': profile_id}))


def delete_analysis(request, profile_id, analysis_id):
    BrokerAnalysis.objects.get(id=analysis_id).delete()
    return HttpResponseRedirect(reverse('inv_profiles:manage_analysis', kwargs={'profile_id': profile_id}))


def delete_rev_sources(request, profile_id, rev_id):
    RevenueIncomeSources.objects.get(id=rev_id).delete()
    return HttpResponseRedirect(reverse('inv_profiles:manage_revenue_sources', kwargs={'profile_id': profile_id}))


def delete_business_segment(request, profile_id, segment_id):
    Segment.objects.get(id=segment_id).delete()
    return HttpResponseRedirect(reverse('inv_profiles:manage_business_segments', kwargs={'profile_id': profile_id}))


def delete_competitor(request, profile_id, competitor_id):
    Competitor.objects.get(id=competitor_id).delete()
    return HttpResponseRedirect(reverse('inv_profiles:manage_competitors', kwargs={'profile_id': profile_id}))


def delete_transaction(request, profile_id, tx_id):
    TransactionForm.objects.get(id=tx_id).delete()
    return HttpResponseRedirect(reverse('inv_profiles:manage_transactions', kwargs={'profile_id': profile_id}))


def delete_metric(request, profile_id, metric_id):
    KeyMetric.objects.get(id=metric_id).delete()
    return HttpResponseRedirect(reverse('inv_profiles:manage_metrics', kwargs={'profile_id': profile_id}))


def delete_risk(request, profile_id, risk_id):
    Risk.objects.get(id=risk_id).delete()
    return HttpResponseRedirect(reverse('inv_profiles:manage_risks', kwargs={'profile_id': profile_id}))


##########################################
# MODIFY INFORMATION TO A PROFILE           #
##########################################


def modify_report(request, profile_id, report_id):
    context = modify_element(request, ReportForm, Report, report_id, profile_id, request.POST)
    return render(request, 'inv_profiles/manage/manage_reports.html', context)


def modify_analysis(request, profile_id, analysis_id):
    context = modify_element(request, BrokerAnalysisForm, BrokerAnalysis, analysis_id, profile_id, request.POST)
    return render(request, 'inv_profiles/manage/manage_analysis.html', context)


def modify_rev_source(request, profile_id, rev_id):
    context = modify_element(request, RevenueSourceForm, RevenueIncomeSources, rev_id, profile_id, request.POST)
    return render(request, 'inv_profiles/manage/manage_revenue_sources.html', context)


def modify_segment(request, profile_id, segment_id):
    context = modify_element(request, SegmentForm, Segment, segment_id, profile_id, request.POST)
    return render(request, 'inv_profiles/manage/manage_segments.html', context)


def modify_competitor(request, profile_id, competitor_id):
    context = modify_element(request, CompetitorForm, Competitor, competitor_id, profile_id, request.POST)
    return render(request, 'inv_profiles/manage/manage_competitors.html', context)


def modify_metric(request, profile_id, metric_id):
    context = modify_element(request, KeyMetricForm, KeyMetric, metric_id, profile_id, request.POST)
    return render(request, 'inv_profiles/manage/manage_metrics.html', context)


def modify_risk(request, profile_id, risk_id):
    context = modify_element(request, RiskForm, Risk, risk_id, profile_id, request.POST)
    return render(request, 'inv_profiles/manage/manage_risks.html', context)


def modify_transaction(request, profile_id, tx_id):
    context = modify_element(request, TransactionForm, Transaction, tx_id, profile_id, request.POST)
    return render(request, 'inv_profiles/manage/manage_transactions.html', context)


##########################################
# ADD INFORMATION TO A PROFILE           #
##########################################


def add_report(request, profile_id):
    add_element(profile_id, ReportForm, request.POST)
    return HttpResponseRedirect(reverse('inv_profiles:manage_reports', kwargs={'profile_id': profile_id}))


def add_analysis(request, profile_id):
    add_element(profile_id, BrokerAnalysisForm, request.POST)
    return HttpResponseRedirect(reverse('inv_profiles:manage_analysis', kwargs={'profile_id': profile_id}))


def add_revenue_source(request, profile_id):
    add_element(profile_id, RevenueSourceForm, request.POST)
    return HttpResponseRedirect(reverse('inv_profiles:manage_revenue_sources', kwargs={'profile_id': profile_id}))


def add_key_metric(request, profile_id):
    add_element(profile_id, KeyMetricForm, request.POST)
    return HttpResponseRedirect(reverse('inv_profiles:manage_metrics', kwargs={'profile_id': profile_id}))


def add_risk(request, profile_id):
    add_element(profile_id, RiskForm, request.POST)
    return HttpResponseRedirect(reverse('inv_profiles:manage_risks', kwargs={'profile_id': profile_id}))


def add_segment(request, profile_id):
    add_element(profile_id, SegmentForm, request.POST)
    return HttpResponseRedirect(reverse('inv_profiles:manage_business_segments', kwargs={'profile_id': profile_id}))


def add_competitor(request, profile_id):
    add_element(profile_id, CompetitorForm, request.POST)
    return HttpResponseRedirect(reverse('inv_profiles:manage_competitors', kwargs={'profile_id': profile_id}))


def add_transaction(request, profile_id):
    add_element(profile_id, TransactionForm, request.POST)
    return HttpResponseRedirect(reverse('inv_profiles:manage_transactions', kwargs={'profile_id': profile_id}))


##########################################
#                                        #
# OTHER INFORMATION RELATED TO A PROFILE #
#                                        #
##########################################
def about_company(request):
    pass


def technicals(request):
    pass


def fundamentals(request):
    pass


def calendar(request):
    pass


##########################################
# HELPER FUNCTIONS                       #
##########################################
def add_element(profile_id, form_class, post_data):
    if post_data:
        profile = get_profile(profile_id)
        form = form_class(post_data)
        print("form errors:")
        print(form.errors)
        element_obj = form.save(commit=False)
        element_obj.profile = profile
        element_obj.save()


def modify_element(request, form_class, model_class, element_id, profile_id, post_data):
    profile = get_profile(profile_id)
    modify_form, empty_form = get_forms(element_id, model_class, form_class)
    all_elements = get_objects(model_class, profile_id)
    context = {'form': empty_form,
               'modify_form': modify_form,
               'element_id': element_id,
               'all_elements': all_elements,
               'profile': profile}

    if post_data:
        profile = get_profile(profile_id)
        element = model_class.objects.get(id=element_id)
        element_form = form_class(post_data, instance=element)

        if element_form.errors:
            print(element_form.errors)

        updated_element = element_form.save(commit=False)
        updated_element.profile = profile
        updated_element.save()
        del context['element_id']
        return context
    else:
        return context


def get_elements(profile, model_class):
    all_elements = model_class.objects.filter(profile=profile)
    return all_elements


def get_current_element(model_class, id):
    current_investment_object = model_class.objects.get(id=id)
    return current_investment_object


def get_profile(profile_id):
    """ Get the investment profile object """
    profile = Profile.objects.get(id=profile_id)
    return profile


def get_forms(id, model_class, form_class):
    """ Get an empty form and a form containing an instance of an object that can be edited """
    current_investment_object = get_current_element(model_class, id)
    empty_form = form_class()
    modify_form = form_class(instance=current_investment_object)

    return modify_form, empty_form


def handle_post_data(post_data, form_class, element_id, model_class, profile_id):
    current_element = get_current_element(model_class, element_id)
    profile = get_profile(profile_id)
    form_post = form_class(post_data, instance=current_element)
    new_element = form_post.save(commit=False)
    new_element.profile = profile
    new_element.save()


def get_objects(model, profile):
    all_objects = model.objects.filter(profile=profile)

    return all_objects
