import os
from ....src.Helpers.LogNameSpace import log_name_space
from ....src.Helpers.ReportNameSpace import report_name_space

if "CLITEST_LOGFILE" not in os.environ:
    os.environ["CLITEST_LOGFILE"] = log_name_space ("cli")

if "CLITEST_HTML" not in os.environ:
    os.environ["CLITEST_HTML"] = report_name_space ("cli")
