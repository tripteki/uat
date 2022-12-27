import signal
from ...Helpers.SpaceMobilePath import mobile_path
from subprocess import call
from os import environ
from typer import Typer, echo, progressbar
from rich.console import Console

application = Typer ()

name = "test:mobile"
description = "Run mobile test cases"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    process = None

    try:
        process = call ("/usr/bin/env python3 -m pytest --html=" + environ["MOBILETEST_HTML"] + " --self-contained-html", cwd = mobile_path (), start_new_session = True, shell = True)

    except KeyboardInterrupt:
        if process:
            process.send_signal (signal.SIGKILL)
