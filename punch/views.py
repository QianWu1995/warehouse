from django.shortcuts import render
from punch.forms import punch_in_form
from datetime import datetime
# Create your views here.


def punch_in(request):
    if request.method == "POST":
        form = punch_in_form(data = request.POST)
        if form.is_valid():
            punch_in_record = form.save(commit=False)
            punch_in_record.user = request.user
            punch_in_record.time = datetime.now()

            punch_in_record.save()
            return render(request,'home.html')
        else:
            return render(request, 'login.html')
    else:
        form = punch_in_form()
        return render(request, 'punch.html', {'form': form})