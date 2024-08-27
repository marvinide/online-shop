from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Hole alle Modelle der aktuellen App
app_models = apps.get_models()

# Versuche, jedes Modell zu registrieren
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass  # Modell wurde bereits registriert, überspringen
