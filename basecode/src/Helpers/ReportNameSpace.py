import os
import datetime
from .BasePath import base_path
from .NameSpace import name_space

def report_name_space (space: str) -> str:
    """
    :type space: str
    :rtype: str
    """
    space = name_space (space)

    if os.environ.get ("PYTHON_ENV", "production") == "production":
        return space + datetime.datetime.now ().strftime ("%d%m%Y%H%M%S") + ".html"
    else:
        return base_path ("logs/reports/" + space + datetime.datetime.now ().strftime ("%d%m%Y%H%M%S") + ".html")
