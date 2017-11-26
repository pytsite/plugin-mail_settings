"""PytSite Mail Settings Form.
"""
from pytsite import lang as _lang
from plugins import widget as _widget, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Email(
            uid='setting_from',
            weight=10,
            label=_lang.t('mail@default_sender_address'),
            required=True,
        ))

        super()._on_setup_widgets()
