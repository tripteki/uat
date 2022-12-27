import signal
from ...Helpers.SpaceApiPath import api_path
from subprocess import call
from os import environ
from typer import Typer, echo, progressbar
from rich.console import Console

application = Typer ()

name = "test:api"
description = "Run api test cases"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    process = None

    try:
        process = call ("/usr/bin/env python3 -m pytest --html=" + environ["APITEST_HTML"] + " --self-contained-html", cwd = api_path (), start_new_session = True, shell = True)

    except KeyboardInterrupt:
        if process:
            process.send_signal (signal.SIGKILL)
