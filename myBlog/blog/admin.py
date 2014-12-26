from django.contrib import admin
from blog.models import Topics, Articles, SiteConf, Comments

# Register your models here.
admin.site.register(Topics)
admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(SiteConf)

