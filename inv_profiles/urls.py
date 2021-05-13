from django.urls import path
from . import views

app_name = "inv_profiles"

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('/add', views.add_profile, name="add_profile"),

    # ALL THE FOLLOWING PATHS ARE RELATED TO THE "INVESTMENT PROFILES" MENU ITEM
    path('/profile/<int:profile_id>', views.view_profile, name="view_profile"),
    path('/profile/edit/<int:profile_id>', views.edit_profile, name="edit_profile"),
    path('/profile/delete/<int:profile_id>', views.delete_profile, name="delete_profile"),

    # MANAGE THE DIFFERENT ASPECTS OF A PROFILE
    path('/profile/manage/report/<int:profile_id>', views.manage_reports, name="manage_reports"),
    path('/profile/manage/analysis/<int:profile_id>', views.manage_analysis, name="manage_analysis"),
    path('/profile/manage/revenue_sources/<int:profile_id>', views.manage_revenue_sources,
         name="manage_revenue_sources"),
    path('/profile/manage/business_segments/<int:profile_id>', views.manage_business_segments,
         name="manage_business_segments"),
    path('/profile/manage/competitors/<int:profile_id>', views.manage_competitors, name="manage_competitors"),
    path('/profile/manage/metrics/<int:profile_id>', views.manage_metrics, name="manage_metrics"),
    path('/profile/manage/risks/<int:profile_id>', views.manage_risks, name="manage_risks"),
    path('/profile/manage/transactions/<int:profile_id>', views.manage_transactions, name="manage_transactions"),

    # ADD INFORMATION IN A PROFILE
    path('/profile/edit/report/<int:profile_id>', views.add_report, name="add_report"),
    path('/profile/edit/analysis/<int:profile_id>', views.add_analysis, name="add_analysis"),
    path('/profile/edit/revenue/<int:profile_id>', views.add_revenue_source, name="add_revenue_source"),
    path('/profile/edit/metric/<int:profile_id>', views.add_key_metric, name="add_key_metric"),
    path('/profile/edit/risk/<int:profile_id>', views.add_risk, name="add_risk"),
    path('/profile/edit/segment/<int:profile_id>', views.add_segment, name="add_segment"),
    path('/profile/edit/competitor/<int:profile_id>', views.add_competitor, name="add_competitor"),
    path('/profile/edit/transaction/<int:profile_id>', views.add_transaction, name="add_transaction"),

    # DELETE INFORMATION IN A PROFILE
    path('/profile/delete/report/<int:profile_id>/<int:report_id>', views.delete_report, name="delete_report"),
    path('/profile/delete/analysis/<int:profile_id>/<int:analysis_id>', views.delete_analysis, name="delete_analysis"),
    path('/profile/delete/revenue/<int:profile_id>/<int:rev_id>', views.delete_rev_sources, name="delete_rev_sources"),
    path('/profile/delete/metric/<int:profile_id>/<int:metric_id>', views.delete_metric, name="delete_metric"),
    path('/profile/delete/risk/<int:profile_id>/<int:risk_id>', views.delete_risk, name="delete_risk"),
    path('/profile/delete/segment/<int:profile_id>/<int:segment_id>',
         views.delete_business_segment, name="delete_business_segment"),
    path('/profile/delete/competitor/<int:profile_id>/<int:competitor_id>', views.delete_competitor,
         name="delete_competitor"),
    path('/profile/delete/transaction/<int:profile_id>/<int:tx_id>', views.delete_transaction,
         name="delete_transaction"),

    # MODIFY INFORMATION IN A PROFILE
    path('/profile/modify/report/<int:profile_id>/<int:report_id>', views.modify_report, name="modify_report"),
    path('/profile/modify/analysis/<int:profile_id>/<int:analysis_id>', views.modify_analysis, name="modify_analysis"),
    path('/profile/modify/revenue/<int:profile_id>/<int:rev_id>', views.modify_rev_source, name="modify_rev_source"),
    path('/profile/modify/metric/<int:profile_id>/<int:metric_id>', views.modify_metric, name="modify_metric"),
    path('/profile/modify/risk/<int:profile_id>/<int:risk_id>', views.modify_risk, name="modify_risk"),
    path('/profile/modify/segment/<int:profile_id>/<int:segment_id>', views.modify_segment, name="modify_segment"),
    path('/profile/modify/competitor/<int:profile_id>/<int:competitor_id>', views.modify_competitor,
         name="modify_competitor"),
    path('/profile/modify/transaction/<int:profile_id>/<int:tx_id>', views.modify_transaction,
         name="modify_transaction"),

    # OTHER INFORMATION RELATED TO THE PROFILE
    path('/profile/about/<int:profile_id>', views.about_company,
         name="about_company"),
    path('/profile/technicals/<int:profile_id>', views.technicals,
         name="technicals"),
    path('/profile/fundamentals/<int:profile_id>', views.fundamentals,
         name="fundamentals"),
    path('/profile/calendar/<int:profile_id>', views.calendar,
         name="calendar"),
]
