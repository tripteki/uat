import signal
from ...Helpers.SpaceWebPath import web_path
from subprocess import call
from os import environ
from typer import Typer, echo, progressbar
from rich.console import Console

application = Typer ()

name = "test:web"
description = "Run web test cases"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    process = None

    try:
        process = call ("/usr/bin/env python3 -m pytest --html=" + environ["WEBTEST_HTML"] + " --self-contained-html", cwd = web_path (), start_new_session = True, shell = True)

    except KeyboardInterrupt:
        if process:
            process.send_signal (signal.SIGKILL)
