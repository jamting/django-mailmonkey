"""Admin for mailmonkey"""
from django.contrib import admin
from django.conf import settings

from mailmonkey.models import Link
from mailmonkey.models import Contact
from mailmonkey.models import WorkGroup
from mailmonkey.models import SMTPServer
from mailmonkey.models import Newsletter
from mailmonkey.models import MailingList
from mailmonkey.models import ContactMailingStatus

from mailmonkey.settings import USE_WORKGROUPS
from mailmonkey.admin.contact import ContactAdmin
from mailmonkey.admin.workgroup import WorkGroupAdmin
from mailmonkey.admin.newsletter import NewsletterAdmin
from mailmonkey.admin.smtpserver import SMTPServerAdmin
from mailmonkey.admin.mailinglist import MailingListAdmin


admin.site.register(Contact, ContactAdmin)
admin.site.register(SMTPServer, SMTPServerAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(MailingList, MailingListAdmin)

if USE_WORKGROUPS:
    admin.site.register(WorkGroup, WorkGroupAdmin)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation_date')

if settings.DEBUG:
    admin.site.register(Link, LinkAdmin)
    admin.site.register(ContactMailingStatus)

