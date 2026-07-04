from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ParticipantForm
from .models import Participant
from django.contrib.auth.decorators import login_required
import csv
from openpyxl import Workbook
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


def register(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)

        if form.is_valid():
            participant = form.save()
            return redirect("success", participant_id=participant.id)

    else:
        form = ParticipantForm()

    return render(
        request,
        "participants/register.html",
        {"form": form},
    )


def success(request, participant_id):

    participant = get_object_or_404(
        Participant,
        id=participant_id
    )

    return render(
        request,
        "participants/success.html",
        {
            "participant": participant
        }
    )

@login_required

def dashboard(request):
    from django.utils import timezone

    search = request.GET.get("search", "")

    participants = Participant.objects.all().order_by("-id")

    if search:
        participants = participants.filter(
            full_name__icontains=search
        )

    paginator = Paginator(participants, 10)

    page_number = request.GET.get("page")

    participants = paginator.get_page(page_number)

    context = {
        "participants": participants,
        "total": Participant.objects.count(),
        "search": search,
        "today": timezone.now(),
    }

    return render(
        request,
        "participants/dashboard.html",
        context,
    )

@login_required
def export_csv(request):

    response = HttpResponse(content_type="text/csv")

    response["Content-Disposition"] = (
        'attachment; filename="participants.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        "Full Name",
        "Designation",
        "Department",
        "Phone Number",
        "Email Address",
    ])

    participants = Participant.objects.all().order_by("full_name")

    for participant in participants:

        writer.writerow([
            participant.full_name,
            participant.designation,
            participant.department,
            participant.phone_number,
            participant.email,
        ])

    return response

@login_required
def export_excel(request):

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Participants"

    sheet.append([
        "S/N",
        "Full Name",
        "Designation",
        "Department",
        "Phone Number",
        "Email",
        "Registered",
    ])

    participants = Participant.objects.all().order_by("full_name")

    for index, participant in enumerate(participants, start=1):

        sheet.append([
            index,
            participant.full_name,
            participant.designation,
            participant.department,
            participant.phone_number,
            participant.email,
            participant.date_registered.strftime("%d %b %Y %H:%M"),
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response[
        "Content-Disposition"
    ] = 'attachment; filename="participants.xlsx"'

    workbook.save(response)

    return response

@login_required
def print_attendance(request):

    participants = Participant.objects.all().order_by("full_name")

    context = {
        "participants": participants,
    }

    return render(
        request,
        "participants/print_attendance.html",
        context,
    )