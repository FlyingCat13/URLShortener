from django.contrib import admin

from .models import URLRedirect

class URLRedirectAdmin(admin.ModelAdmin):
    fields = ["original_URL", "created_by"]
    readonly_fields = ["short_URL_suffix", "access_count"]

admin.site.register(URLRedirect, URLRedirectAdmin)
