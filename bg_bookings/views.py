from django.shortcuts import render


# Create your views here.
def get_bookings(request):
    return render(request, 'bg_bookings/bookings.html')
