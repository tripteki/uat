import os
from ....src.Helpers.LogNameSpace import log_name_space
from ....src.Helpers.ReportNameSpace import report_name_space

if "WEBTEST_LOGFILE" not in os.environ:
    os.environ["WEBTEST_LOGFILE"] = log_name_space ("web")

if "WEBTEST_HTML" not in os.environ:
    os.environ["WEBTEST_HTML"] = report_name_space ("web")
