import os

if os.environ["app"] == "prod":
    from config.prod import prodConfig as Config
else:
    from config.dev import devConfig as Config