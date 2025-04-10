from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from datetime import date
from django.contrib import messages

def date_view(request):
    if request.method == "POST" and "submit_service" in request.POST:
        selected_date = request.POST.get("selected_date") or date.today().strftime("%Y-%m-%d")
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.requested_date = selected_date
            service_request.save()
            messages.success(request, "Service request created successfully!")
            return redirect("date_view")
    else:
        selected_date = date.today().strftime("%Y-%m-%d")
        form = ServiceRequestForm()

    return render(request, "service/service.html", {
        "selected_date": selected_date,
        "form": form
    })
