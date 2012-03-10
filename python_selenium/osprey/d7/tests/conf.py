from . import secrets

conf = {
        "base_url": 'http://localhost/osprey'
        }

conf.update(secrets.secrets)

