from django.urls import path
from . import views

app_name = "social"

urlpatterns = [
    path('', views.index, name="index"),
    path('/add/idea', views.add_inv_idea, name="add_inv_idea"),
    path('/add/plan/', views.add_inv_plan, name="add_inv_plan"),
    path('/add/plan/<int:plan_id>', views.add_inv_plan, name="add_inv_plan"),
    path('/view/idea/<int:idea_id>', views.view_inv_idea, name="view_inv_idea"),
    path('/view/idea/<int:idea_id>/<int:rec>', views.view_inv_idea, name="view_inv_idea"),
]
