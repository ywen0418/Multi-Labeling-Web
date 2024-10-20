from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportMixin
# Register your models here.
from .models import Question,Task
from .resources import QuestionResource

admin.site.register(Task)

class QuestionAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = QuestionResource

admin.site.register(Question,QuestionAdmin)