from . import secrets
import xmlrunner
import unittest
import os

conf = {
        "base_url": '',
        "timeout": 10,
        "selenium_jar": '',
        "test_report_dir": ''
        }

conf.update(secrets.secrets)

# Override from environment variables.
env_vars = {
        "SELENIUM_JAR": "selenium_jar",
        "TEST_REPORTS": "test_report_dir"
        }
for env_var, conf_var in env_vars.items():
    if os.getenv(env_var): conf[conf_var] = os.getenv(env_var)

xml_runner = xmlrunner.XMLTestRunner(output=conf.get('test_report_dir', '.'))
conf['default_runner'] = xml_runner
#conf['default_runner'] = unittest.TextTestRunner(verbosity=2)
