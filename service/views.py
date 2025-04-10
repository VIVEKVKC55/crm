# app/views.py
from django.shortcuts import render
from datetime import datetime

def calendar_view(request):
    return render(request, 'calendar.html')  # HTML file name

def date_view(request, selected_date):
    try:
        date_obj = datetime.strptime(selected_date, "%Y-%m-%d").date()
    except ValueError:
        date_obj = None
    return render(request, 'calendar_day_view.html', {'selected_date': date_obj})
