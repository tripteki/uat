def name_space (space: str) -> str:
    """
    :type space: str
    :rtype: str
    :raises Exception:
    """
    if space == "perform":
        return "_perform_"
    elif space == "cli":
        return "__cli__"
    elif space == "api":
        return "___api___"
    elif space == "web":
        return "____web____"
    elif space == "mobile":
        return "____mobile____"
    else:
        raise Exception ("Not the type of spaces")
