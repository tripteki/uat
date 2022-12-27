from .Version import Version
from .Console.Commands.VersionCommand import application as VersionCommand, name as VersionCommandName, description as VersionCommandDescription
from .Console.Commands.PerformanceTestCommand import application as PerformanceTestCommand, name as PerformanceTestCommandName, description as PerformanceTestCommandDescription
from .Console.Commands.CliTestCommand import application as CliTestCommand, name as CliTestCommandName, description as CliTestCommandDescription
from .Console.Commands.ApiTestCommand import application as ApiTestCommand, name as ApiTestCommandName, description as ApiTestCommandDescription
from .Console.Commands.WebTestCommand import application as WebTestCommand, name as WebTestCommandName, description as WebTestCommandDescription
from .Console.Commands.MobileTestCommand import application as MobileTestCommand, name as MobileTestCommandName, description as MobileTestCommandDescription
from dotenv import load_dotenv
from os import environ
from typer import Typer

load_dotenv ()
from ..tests._perform_ import config
from ..tests.__cli__ import config
from ..tests.___api___ import config
from ..tests.____web____ import config
from ..tests.____mobile____ import config

application = Typer (help = environ.get ("PYTHON_NAME", "User Acceptance Test Command Line Tool"))

application.add_typer (VersionCommand, name = VersionCommandName, help = VersionCommandDescription)
application.add_typer (PerformanceTestCommand, name = PerformanceTestCommandName, help = PerformanceTestCommandDescription)
application.add_typer (CliTestCommand, name = CliTestCommandName, help = CliTestCommandDescription)
application.add_typer (ApiTestCommand, name = ApiTestCommandName, help = ApiTestCommandDescription)
application.add_typer (WebTestCommand, name = WebTestCommandName, help = WebTestCommandDescription)
application.add_typer (MobileTestCommand, name = MobileTestCommandName, help = MobileTestCommandDescription)

if __name__ == "__main__":

    application ()
