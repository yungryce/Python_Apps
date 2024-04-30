from django.contrib import admin
from .models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']
    list_per_page = 10

admin.site.register(Candidate, CandidateAdmin)

# Register your models here.
