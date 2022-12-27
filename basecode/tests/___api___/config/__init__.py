import os
from ....src.Helpers.LogNameSpace import log_name_space
from ....src.Helpers.ReportNameSpace import report_name_space

if "APITEST_LOGFILE" not in os.environ:
    os.environ["APITEST_LOGFILE"] = log_name_space ("api")

if "APITEST_HTML" not in os.environ:
    os.environ["APITEST_HTML"] = report_name_space ("api")
