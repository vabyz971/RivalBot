import os

DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    print("===== DEBUG MODE ======")
    from pathlib import Path
    from dotenv import load_dotenv
    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path=env_path)
    from settings_files.developement import *
else:
    print("===== PRODUCTION MODE ======")
    from settings_files.production import *
