from django.conf import settings
def is_debug(request):
    return {"DEBUG": settings.DEBUG}

def url_base(request):
    return {"URL_BASE": settings.URL_BASE}

def get_project_name(request):
    return {"PROJECT_NAME": settings.PROJECT_NAME}

