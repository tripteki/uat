from typing import Optional
from .ApplicationPath import application_path
from .NameSpace import name_space

def cli_path (path: Optional[str] = None) -> str:
    """
    :type path: Optional[str]
    :rtype: str
    """
    base = "tests/" + name_space ("cli") + "/"

    if path:
        base = base + path

    return application_path (base)
