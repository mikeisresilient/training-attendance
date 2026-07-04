from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("success/", views.success, name="success"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("export/csv/", views.export_csv, name="export_csv"),
    path("export/excel/", views.export_excel, name="export_excel"),
    path("print/", views.print_attendance, name="print_attendance"),
    path(
    "success/<int:participant_id>/",
    views.success,
    name="success",
),
]