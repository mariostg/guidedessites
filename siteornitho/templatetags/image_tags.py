import os
from django import template

register = template.Library()


@register.simple_tag
def get_file_name(image_path_name):
    """
    Returns image file name given fullpath.
    """
    return os.path.basename(image_path_name)
