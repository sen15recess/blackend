from __future__ import unicode_literals

from account.conf import settings
from account.models import Account
from pinax_theme_bootstrap_account.conf import settings


def account(request):
    ctx = {
        "account": Account.for_request(request),
        "ACCOUNT_OPEN_SIGNUP": settings.ACCOUNT_OPEN_SIGNUP,
    }
    return ctx


def theme(request):
    ctx = {
        "THEME_ACCOUNT_ADMIN_URL": settings.THEME_ACCOUNT_ADMIN_URL,
        "THEME_ACCOUNT_CONTACT_EMAIL": settings.THEME_ACCOUNT_CONTACT_EMAIL,
    }
    return ctx