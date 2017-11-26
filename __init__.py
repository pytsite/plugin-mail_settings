"""PytSite Mail Settings Plugin
"""
from . import _settings_form

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, router
    from plugins import permissions, settings

    lang.register_package(__name__)

    permissions.define_permission('mail_settings@manage_settings', 'mail_settings@manage_mail_settings', 'app')
    settings.define('mail', _settings_form.Form, 'mail_settings@mail', 'fa fa-envelope', 'mail_settings@manage_settings')

    if not settings.get('mail.from'):
        settings.put('mail.from', 'info@' + router.server_name())


_init()
