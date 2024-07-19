from django.shortcuts import render, redirect
from .models import Contact_us, Booking, PartnerInquiry
from datetime import datetime



# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        check_in = request.POST.get('Check-In')
        check_out = request.POST.get('Check-Out')
        adults = request.POST.get('Adults')
        children = request.POST.get('Children')
        phone_no = request.POST.get('Phone No.')
        villa_name = request.POST.get('Villa Name')

        try:
            check_in = datetime.strptime(check_in, '%Y-%m-%d').date()
            check_out = datetime.strptime(check_out, '%Y-%m-%d').date()
        except ValueError:
            # Handle invalid date format
            return render(request, 'index.html', {'error': 'Invalid date format. Please use YYYY-MM-DD.'})

        booking = Booking(
            name=name,
            check_in=check_in,
            check_out=check_out,
            adults=adults,
            children=children,
            phone_no=phone_no,
            villa_name=villa_name,
        )

        booking.save()
        return redirect('villas')


    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')
def partnerwithus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        location = request.POST.get('location')

        # Debugging print statements to check form data
        print(name, email, phone_no, location)

        partnerwithus = PartnerInquiry(
            name=name,
            email=email,
            phone_no=phone_no,
            location=location
        )
        partnerwithus.save()
        return redirect('/')

    return render(request, 'partnerwithus.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,)

        contact.save()
        return redirect('contact')


    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def villas(request):
    return render(request,'villas.html')

def header(request):
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

def single(request):
    return render(request,'single.html')

def gallery(request):
    return render(request,'gallery.html')





