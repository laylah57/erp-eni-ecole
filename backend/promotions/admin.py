from django.contrib import admin
from .models import (
    Promotion,
    Inscription,
    CoursPlanifie,
    Animer
)

admin.site.register(Promotion)
admin.site.register(Inscription)
admin.site.register(CoursPlanifie)
admin.site.register(Animer)