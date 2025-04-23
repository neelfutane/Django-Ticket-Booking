from django.urls import path
from .views import RegisterView, LoginView  , HomeView , BookShowView , LogoutView
from .views import BookShowView, BookingHistoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',    LoginView.as_view(),    name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('book/<int:show_id>/', BookShowView.as_view(), name='book_show'),
    path('history/', BookingHistoryView.as_view(), name='booking_history'),

]
