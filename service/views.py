from django.shortcuts import render
from datetime import date

def date_view(request):
    if request.method == "POST":
        selected_date = request.POST.get("selected_date")
        print("selected_date",selected_date)
    else:
        selected_date = date.today().strftime("%Y-%m-%d")

    return render(request, "service.html", {"selected_date": selected_date})

