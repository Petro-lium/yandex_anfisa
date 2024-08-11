from django.contrib import admin
from .models import City, Friend


#admin.site.register(City)
#admin.site.register(Friend)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city__name')
