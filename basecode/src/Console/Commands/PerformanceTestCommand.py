import signal
import time
from ...Helpers.SpacePerformPath import perform_path
from locust.util.timespan import parse_timespan
from subprocess import Popen, PIPE
from os import environ
from typer import Typer, echo, progressbar
from rich.console import Console

application = Typer ()

name = "test:performance"
description = "Run performance test"
loading = "Performance test is in progress"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    process = None

    try:
        process = Popen ("/usr/bin/env python3 -m locust", cwd = perform_path (), start_new_session = True, shell = True, stdin = PIPE, stdout = PIPE, stderr = PIPE)

        with progressbar (length = parse_timespan (environ["LOCUST_RUN_TIME"]), label = loading) as progress:
            while process.poll () is None:
                time.sleep (1)
                progress.update (1)

        process.wait ()

        stdout, stderr = process.communicate ()

        if process.returncode == 0:
            echo (0)
        else:
            Console (stderr = True).print (1)

        process.kill ()

    except KeyboardInterrupt:
        if process:
            process.send_signal (signal.SIGKILL)
