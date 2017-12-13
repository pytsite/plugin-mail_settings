"""PytSite Mail Settings Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from pytsite import lang, router, reg
    from plugins import permissions, settings
    from . import _settings_form

    lang.register_package(__name__)

    permissions.define_permission('mail_settings@manage_settings', 'mail_settings@manage_mail_settings', 'app')
    settings.define('mail', _settings_form.Form, 'mail_settings@mail', 'fa fa-envelope',
                    'mail_settings@manage_settings')

    if not reg.get('mail.from'):
        reg.put('mail.from', 'info@' + router.server_name())
