from django.shortcuts import render, redirect
from django.views import View 
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Show , Seat , Booking

class RegisterView(View):
    def get(self, request):
        return render(request, 'booking/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            return render(request, 'booking/register.html', {'error': 'Passwords do not match'})
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')  
    
class LoginView(View):
    def get(self, request):
        next_url = request.GET.get('next')
        return render(request, 'booking/login.html', {'next': next_url})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect(request.POST.get('next') or 'home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'booking/login.html')

class HomeView(View):
    def get(self, request):
        shows = Show.objects.filter(date_time__gte=timezone.now()).order_by('date_time')
        return render(request, 'booking/home.html', {'shows': shows})

@method_decorator(login_required, name='dispatch')
class BookShowView(View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        seats = show.seats.filter(is_booked=False).order_by('seat_number')
        return render(request, 'booking/book_show.html', {'show': show, 'seats': seats})

    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        selected = request.POST.getlist('seats')  

        if not selected:
            return render(request, 'booking/book_show.html', {
                'show': show,
                'seats': show.seats.filter(is_booked=False),
                'error': 'Please select at least one seat.'
            })

        booking = Booking.objects.create(user=request.user, show=show)

        available_seats = show.seats.filter(id__in=selected, is_booked=False)
        if len(available_seats) != len(selected):
            return render(request, 'booking/book_show.html', {
                'show': show,
                'seats': show.seats.filter(is_booked=False),
                'error': 'One or more selected seats are no longer available. Please try again.'
            })

        for seat in available_seats:
            booking.seats.add(seat)
            seat.is_booked = True

        Seat.objects.bulk_update(available_seats, ['is_booked'])        
        booking.save()
        
        return redirect('booking_history')

@method_decorator(login_required, name='dispatch')
class BookingHistoryView(View):
    def get(self, request):
        bookings = request.user.bookings.select_related('show').prefetch_related('seats').order_by('-booking_time')
        return render(request, 'booking/history.html', {'bookings': bookings})
    
class LogoutView(View):
    def get(self, request):
        logout(request)  
        return redirect('home')  