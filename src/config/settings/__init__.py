from .base import BASE_DIR, env

if env.bool('DEBUG'):
    from .dev import *
else:
    from .prod import *
