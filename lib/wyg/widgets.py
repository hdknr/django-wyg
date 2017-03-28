# coding=utf-8
'''
https://alex-d.github.io/Trumbowyg/documentation.html
'''

from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.utils import translation
from django.conf import settings
from django.utils.six.moves.urllib.parse import urljoin
from json import dumps


def _S(path):
    return urljoin(getattr(settings, 'STATIC_URL', ''), path)


class EditorWidget(Textarea):

    class Media:
        css = {
            'all': (
                _S('bootstrap/dist/css/bootstrap.min.css'),
                _S('trumbowyg/dist/ui/trumbowyg.css'),
            )
        }

        js = (
            _S('jquery/dist/jquery.min.js'),
            _S('bootstrap/dist/js/bootstrap.min.js'),
            _S('trumbowyg/dist/trumbowyg.min.js'),
        )

    def __init__(self, attrs=None, buttons=None, auto=True):
        super(EditorWidget, self).__init__(attrs=None)
        self.editor = {}
        self.auto = auto
        if buttons:
            self.editor['btns'] = buttons
        lang = translation.get_language()
        if lang:
            self.editor['lang'] = lang
            js = _S('trumbowyg/dist/langs/%s.min.js' % lang)
            if js not in self.Media.js:
                self.Media.js += (js, )

    def render(self, name, value, attrs=None):
        output = super(EditorWidget, self).render(name, value, attrs)
        if self.auto:
            script = u'''
                <script>var editor_{name} = $('#id_{name}').trumbowyg({param});
                </script>
            '''.format(name=name, param=dumps(self.editor))
            output += mark_safe(script)
        return output
