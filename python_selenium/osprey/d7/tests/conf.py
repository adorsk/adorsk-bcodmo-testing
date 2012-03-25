from . import secrets
import os

conf = {
        "base_url": 'http://localhost/osprey'
        }

# Merge secrets.
conf.update(secrets.secrets)

# Override from environment variables.
env_vars = {
        "BCODMO_D7_BASE_URL": "base_url"
        }
for env_var, conf_var in env_vars.items():
    if os.getenv(env_var): conf[conf_var] = os.getenv(env_var)


