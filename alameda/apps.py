from django.contrib.admin.apps import AdminConfig


class AlamedaAdminConfig(AdminConfig):
    default_site = 'alameda.admin.AlamedaAdminSite'
