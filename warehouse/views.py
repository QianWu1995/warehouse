from django.shortcuts import redirect



def home_page_redirect(request):
    return redirect('/home')