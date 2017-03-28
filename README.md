# django-wyg

- Trumbowyg for Django

## Simply define a Admin Form

~~~py
class EntryAdminForm(ModelForm):

    class Meta:
        model = Entry
        exclude = []
        widgets = {
            'text': EditorWidget(buttons=[['bold', 'italic'], ['link']]),
        }

class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
~~~

## In templates for views

~~~html
<head>
    {{ form.media }}
</head>
...
<form ...>
    {{ form }}
</form>
~~~

## For custom settings or scripting

`auto=False`:

~~~py
class EntryForm(ModelForm):

    class Meta:
        model = Entry
        exclude = []
        widgets = {
            'text': EditorWidget(auto=False),
        }
~~~

- http://alex-d.github.io/Trumbowyg/documentation.html

~~~html
<head>
    {{ form.media.css }}
</head>
...
<form ...>
    {{ form }}
</form>
...
{{ form.media.js }}
<script>
    var param = {btns: [['bold', 'italic'], ['link']], lang: 'ja'};
    var editor_{{ form.text.name }} = $('#id_{{ form.text.name }}').trumbowyg(param);
</script>
~~~

