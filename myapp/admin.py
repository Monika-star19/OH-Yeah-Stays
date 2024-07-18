from django.contrib import admin
from .models import Contact_us, Booking,  PartnerInquiry

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('date',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'check_in', 'check_out', 'adults', 'children', 'phone_no', 'villa_name')
    search_fields = ('name', 'phone_no', 'villa_name')
    list_filter = ('check_in', 'check_out',)

class PartnerInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_no', 'location')
    search_fields = ('name', 'email', 'phone_no', 'location')








admin.site.register(Contact_us,ContactUsAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(PartnerInquiry, PartnerInquiryAdmin)