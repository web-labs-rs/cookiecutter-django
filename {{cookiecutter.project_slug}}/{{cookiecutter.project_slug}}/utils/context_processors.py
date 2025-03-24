import os

from {{ cookiecutter.project_slug }} import PROJECT_VERSION


def export_vars(request) -> dict:
    """Expose some variable in templates."""
    return {
        "PROJECT_VERSION": PROJECT_VERSION,
        "ENV": os.environ["DJANGO_SETTINGS_MODULE"].replace("config.settings.", ""),
    }
