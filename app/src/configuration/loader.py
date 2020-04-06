
import os

ENV_NAME_FLASK_DEBUG = "FLASK_DEBUG"

class _Config(object):
    def __init__(self):
        self.FLASK_DEBUG = self._load(ENV_NAME_FLASK_DEBUG)

    def _load(self, env_name):
        return os.getenv(env_name)
