"""PytSite Mail Settings Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_wsgi():
    from pytsite import router, reg
    from plugins import settings
    from . import _settings_form

    settings.define('mail', _settings_form.Form, 'mail_settings@mail', 'fa fa-envelope', 'dev')

    if not reg.get('mail.from'):
        reg.put('mail.from', 'info@' + router.server_name())
