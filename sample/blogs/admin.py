from django.contrib import admin
from django.forms import ModelForm
from .models import Entry
from wyg.widgets import EditorWidget

# Register your models here.


class EntryAdminForm(ModelForm):

    class Meta:
        model = Entry
        exclude = []
        widgets = {
            'text': EditorWidget(buttons=[['bold', 'italic'], ['link']]),
        }
        # https://alex-d.github.io/Trumbowyg/documentation.html#button-pane


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm


admin.site.register(Entry, EntryAdmin)
