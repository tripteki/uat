import datetime
import os
from ....src.Helpers.SpacePerformPath import perform_path
from ....src.Helpers.LogNameSpace import log_name_space
from ....src.Helpers.ReportNameSpace import report_name_space

if "LOCUST_LOCUSTFILE" not in os.environ:
    os.environ["LOCUST_LOCUSTFILE"] = perform_path ("src")

if "LOCUST_WEB_HOST" not in os.environ:
    os.environ["LOCUST_WEB_HOST"] = "http://localhost"

if "LOCUST_WEB_PORT" not in os.environ:
    os.environ["LOCUST_WEB_PORT"] = "8001"

if "LOCUST_HOST" not in os.environ:
    os.environ["LOCUST_HOST"] = "http://localhost:80"

if "LOCUST_HEADLESS" not in os.environ:
    os.environ["LOCUST_HEADLESS"] = "1"

if "LOCUST_EXIT_CODE_ON_ERROR" not in os.environ:
    os.environ["LOCUST_EXIT_CODE_ON_ERROR"] = "1"

if "LOCUST_USERS" not in os.environ:
    os.environ["LOCUST_USERS"] = "100"

if "LOCUST_SPAWN_RATE" not in os.environ:
    os.environ["LOCUST_SPAWN_RATE"] = "10"

if "LOCUST_RUN_TIME" not in os.environ:
    os.environ["LOCUST_RUN_TIME"] = "1m"

if "LOCUST_AUTOSTART" not in os.environ:
    os.environ["LOCUST_AUTOSTART"] = "1"

if "LOCUST_AUTOQUIT" not in os.environ:
    os.environ["LOCUST_AUTOQUIT"] = "1"

if "LOCUST_LOGLEVEL" not in os.environ:
    os.environ["LOCUST_LOGLEVEL"] = "DEBUG"

if "LOCUST_LOGFILE" not in os.environ:
    os.environ["LOCUST_LOGFILE"] = log_name_space ("perform")

if "LOCUST_HTML" not in os.environ:
    os.environ["LOCUST_HTML"] = report_name_space ("perform")
