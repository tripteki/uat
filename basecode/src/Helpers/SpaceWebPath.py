from typing import Optional
from .ApplicationPath import application_path
from .NameSpace import name_space

def web_path (path: Optional[str] = None) -> str:
    """
    :type path: Optional[str]
    :rtype: str
    """
    base = "tests/" + name_space ("web") + "/"

    if path:
        base = base + path

    return application_path (base)
