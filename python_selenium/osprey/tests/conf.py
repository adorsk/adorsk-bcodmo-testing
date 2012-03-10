from . import secrets
import xmlrunner
import unittest

conf = {
        "base_url": '',
        "output_dir": 'test-output'
        }

xml_runner = xmlrunner.XMLTestRunner(output=conf.get('output_dir', '.'))
#conf['default_runner'] = xml_runner
conf['default_runner'] = unittest.TextTestRunner(verbosity=2)

conf.update(secrets.secrets)
