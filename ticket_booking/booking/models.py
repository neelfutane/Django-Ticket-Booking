from django.db import models
from django.contrib.auth.models import User

class Show(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.date_time.strftime('%Y-%m-%d %H:%M')})"

class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.show.title} – Seat {self.seat_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='bookings')
    seats = models.ManyToManyField(Seat)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        seat_list = ','.join(s.seat_number for s in self.seats.all())
        return f"{self.user.username}: {self.show.title} [{seat_list}]"

