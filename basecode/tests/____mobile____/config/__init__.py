import os
from ....src.Helpers.LogNameSpace import log_name_space
from ....src.Helpers.ReportNameSpace import report_name_space

if "MOBILETEST_REMOTE_ADDRESS" not in os.environ:
    os.environ["MOBILETEST_REMOTE_ADDRESS"] = "http://localhost:4723/wd/hub"



if "MOBILETEST_PLATFORM_ANDROID_ID" not in os.environ:
    os.environ["MOBILETEST_PLATFORM_ANDROID_ID"] = "emulator-5554"

if "MOBILETEST_PLATFORM_ANDROID_NAME" not in os.environ:
    os.environ["MOBILETEST_PLATFORM_ANDROID_NAME"] = "Pixel_5_API_33"

if "MOBILETEST_PLATFORM_ANDROID_VERSION" not in os.environ:
    os.environ["MOBILETEST_PLATFORM_ANDROID_VERSION"] = "13"



if "MOBILETEST_PLATFORM_IOS_ID" not in os.environ:
    os.environ["MOBILETEST_PLATFORM_IOS_ID"] = "A374D6AA-769E-451F-AD4A-AFC804368B42"

if "MOBILETEST_PLATFORM_IOS_NAME" not in os.environ:
    os.environ["MOBILETEST_PLATFORM_IOS_NAME"] = "iPhone 14 Pro Max"

if "MOBILETEST_PLATFORM_IOS_VERSION" not in os.environ:
    os.environ["MOBILETEST_PLATFORM_IOS_VERSION"] = "16.0"



if "MOBILETEST_APPLICATION_ANDROID_PATH" not in os.environ:
    os.environ["MOBILETEST_APPLICATION_ANDROID_PATH"] = "pathto.apk"

if "MOBILETEST_APPLICATION_IOS_PATH" not in os.environ:
    os.environ["MOBILETEST_APPLICATION_IOS_PATH"] = "pathto.ipa"



if "MOBILETEST_LOGFILE" not in os.environ:
    os.environ["MOBILETEST_LOGFILE"] = log_name_space ("mobile")

if "MOBILETEST_HTML" not in os.environ:
    os.environ["MOBILETEST_HTML"] = report_name_space ("mobile")
