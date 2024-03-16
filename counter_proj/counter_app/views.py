from django.shortcuts import render
from .models import Digit

# increase , decrease and reset counter:
def counter(request):
    digit = Digit.objects.first()
    

    if request.method == 'POST':

        if "decreasment" in request.POST:
            digit.decreasment()

        if "reset" in request.POST:
            digit.reset()

        if "increasment" in request.POST:
            digit.increasment()

    return render (request , 'counter_app/counter_page.html', context={'num' : digit})

