from django.contrib import admin

from .models import Session, TargetCords, ZoneCords, UserCords

admin.site.register(Session)
admin.site.register(TargetCords)
admin.site.register(ZoneCords)
admin.site.register(UserCords)
