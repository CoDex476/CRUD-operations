from django.contrib import admin

from .models import Employee, Position


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "position", "emp_code", "phone")
    list_display_links = ("id", "full_name")
    list_filter = ("full_name",)


class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
