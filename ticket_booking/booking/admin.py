from django.contrib import admin
from .models import Show, Seat, Booking

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display   = ('title', 'date_time', 'total_seats', 'price')
    search_fields  = ('title',)
    ordering       = ('-date_time',)
    list_filter    = ('date_time',)
    fieldsets      = (
        (None, {
            'fields': ('title', 'date_time', 'total_seats', 'price')
        }),
    )

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display  = ('show', 'seat_number', 'is_booked')
    list_filter   = ('show', 'is_booked')
    search_fields = ('seat_number',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display     = ('user', 'show', 'booking_time', 'seat_list')
    list_filter      = ('show', 'user')
    search_fields    = ('user__username', 'show__title')
    filter_horizontal = ('seats',)

    def seat_list(self, obj):
        return ", ".join(seat.seat_number for seat in obj.seats.all())
    seat_list.short_description = 'Seats'
