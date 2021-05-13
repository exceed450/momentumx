from .modelform import IdeaCommentForm, PlanCommentForm, InvestmentIdeaForm
from .models import InvestmentIdea, InvestmentPlan
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import IdeaComment, PlanComment
from inv_profiles.models import Profile


def index(request):
    ideas = None
    authenticated = False

    if request.user.is_authenticated:
        user = request.user
        authenticated = True
        ideas = InvestmentIdea.objects.filter(posted_by=user)
        plans = Profile.objects.filter(shared=True)

    return render(request, 'social/index.html',
                  {'ideas': ideas,
                   'plans': plans,
                   'authenticated': authenticated})


def add_inv_idea(request):
    success = False

    if request.POST:
        data = InvestmentIdeaForm(request.POST)
        print("From errors:")
        print(data.errors)
        user = request.user
        date = datetime.now()
        temp_idea = data.save(commit=False)
        temp_idea.posted_by = user
        temp_idea.date_added = date
        temp_idea.save()
        success = True

        return HttpResponseRedirect(reverse('social:index'))

    form = InvestmentIdeaForm()
    return render(request, 'social/add_inv_idea.html',
                  {'form': form,
                   'success': success})


def add_inv_plan(request, plan_id=0):
    authenticated = False

    if plan_id != 0:
        plan = Profile.objects.get(id=plan_id)

        if not plan.shared:
            plan.shared = True
        else:
            plan.shared = False

        plan.save()

    if request.user.is_authenticated:
        user = request.user
        authenticated = True
        user_inv_plans = Profile.objects.filter(user=user)

    return render(request, 'social/add_inv_plan.html',
                  {'user': user,
                   'authenticated': authenticated,
                   'user_inv_plans': user_inv_plans})


def view_inv_idea(request, idea_id, rec=0):
    print("rec: ")
    print(rec)
    idea_profile = InvestmentIdea.objects.get(id=idea_id)
    idea_form = IdeaCommentForm()
    date = datetime.now()
    user = request.user
    comments = IdeaComment.objects.filter(idea=idea_profile)

    if rec is not 0:
        print("User hit the recommend button")
        if rec == 1:
            idea_profile.recommendations = idea_profile.recommendations + 1
            idea_profile.save()
        else:
            idea_profile.recommendations = idea_profile.recommendations - 1
            idea_profile.save()

    if request.POST:
        form = IdeaCommentForm(request.POST)

        if form.is_valid:
            temp_comment = form.save(commit=False)
            temp_comment.date_added = date
            temp_comment.posted_by = user
            temp_comment.idea = idea_profile
            temp_comment.save()

    return render(request, 'social/view_inv_idea.html',
                  {'idea_profile': idea_profile,
                   'idea_form': idea_form,
                   'comments': comments})

