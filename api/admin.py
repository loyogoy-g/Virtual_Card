from django.contrib import admin

from .models import FirstQuarter, SecondQuarter, ThirdQuarter, FourthQuarter, Student

from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


class FirstInline(admin.TabularInline):
    model = FirstQuarter
    extra = 3

class SecondtInline(admin.TabularInline):
    model = SecondQuarter
    extra = 3

class ThirdInline(admin.TabularInline):
    model = ThirdQuarter
    extra = 3

class FourthInline(admin.TabularInline):
    model = FourthQuarter
    extra = 3

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("Name", "LRN", "Status")
    inlines = [FirstInline]
    list_filter = ("Status", "Section")
