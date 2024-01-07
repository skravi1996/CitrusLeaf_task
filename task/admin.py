from django.contrib import admin
from .models import Task
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    pass
#admin.site.register(Task)