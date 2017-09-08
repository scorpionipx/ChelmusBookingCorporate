@echo off
color d
cls
cmd /k "cd /d D:\Documents\Python\Django\ChelmusBookingCorporate\virtualenv\Scripts & activate & cd /d    D:\Documents\Python\Django\ChelmusBookingCorporate\ChelmusBooking & python manage.py createsuperuser"
pause