import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR,'data')

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", False)


BOT_PREFIX = "!"

# MongoDB Configuration

MONGODB_HOST=os.getenv("MONGODB_HOST")
MONGODB_DATABASE=os.getenv("MONGODB_DATABASE")
MONGODB_USER=os.getenv("MONGODB_USER")
MONGODB_PASSWORD=os.getenv("MONGODB_PASSWORD")