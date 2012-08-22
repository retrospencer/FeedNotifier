# Helper Functions
def load_revision():
    try:
        with open('revision.txt', 'r') as file:
            return int(file.read().strip())
    except Exception:
        return -1
        
# Popup Settings
POPUP_DURATION = 5
POPUP_AUTO_PLAY = True
POPUP_WAIT_ON_HOVER = True
POPUP_THEME = 'default'
POPUP_WIDTH = 400
POPUP_POSITION = (1, 1)
POPUP_TRANSPARENCY = 230
POPUP_TITLE_LENGTH = 120
POPUP_BODY_LENGTH = 400
POPUP_DISPLAY = 0
POPUP_STAY_ON_TOP = True
POPUP_BORDER_SIZE = 3
POPUP_BORDER_COLOR = (0, 0, 0)

# Cache age limit. This is used as a maximum to determine when cached entries age off the cache list. 
# This is NOT the pop up cache, the is the internal cache that is used to determine if an entry is new or not
# TBD: expose this in UI
CACHE_AGE_LIMIT = 40 #in days

# Application Settings
APP_ID = 'FeedNotifier'
APP_NAME = 'Feed Notifier'
APP_VERSION = '2.5'
APP_URL = 'http://www.feednotifier.com/'
USER_AGENT = '%s/%s +%s' % (APP_ID, APP_VERSION, APP_URL)
DEFAULT_POLLING_INTERVAL = 60 * 15
USER_IDLE_TIMEOUT = 60
DISABLE_WHEN_IDLE = False
ITEM_CACHE_AGE = 60 * 60 * 24 * 1
MAX_WORKER_THREADS = 10
PLAY_SOUND = True
SOUND_PATH = 'sounds/notification.wav'
SOCKET_TIMEOUT = 15

# Initial Setup
DEFAULT_FEED_URLS = [
    'http://www.feednotifier.com/welcome.xml',
]

# Proxy Settings
USE_PROXY = False
PROXY_URL = ''

# Updater Settings
LOCAL_REVISION = load_revision()
REVISION_URL = 'http://www.feednotifier.com/update/revision.txt'
INSTALLER_URL = 'http://www.feednotifier.com/update/installer.exe'
CHECK_FOR_UPDATES = True
UPDATE_INTERVAL = 60 * 60 * 24 * 1
UPDATE_TIMESTAMP = 0

del load_revision
