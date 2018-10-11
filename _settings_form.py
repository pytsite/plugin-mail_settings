"""PytSite Mail Settings Form.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang
from plugins import widget as _widget, settings as _settings


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Email(
            uid='setting_from',
            weight=10,
            label=_lang.t('mail_settings@default_sender_address'),
            required=True,
        ))

        super()._on_setup_widgets()
