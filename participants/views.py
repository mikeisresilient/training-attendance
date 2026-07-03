from django.shortcuts import render, redirect
from .forms import ParticipantForm


def register(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")

    else:
        form = ParticipantForm()

    return render(
        request,
        "participants/register.html",
        {"form": form},
    )


def success(request):
    return render(request, "participants/success.html")