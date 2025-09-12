# Discord Logging Handler

A Python logging handler that sends log messages to Discord via webhook with colour coded levels.

## Installation

```bash
pip install discord-logging-handler
```

## Usage

### Django Example

settings.py

```bash
DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')

LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/app.log'),
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'discord': {
            'level': 'INFO',
            'class': 'discord_logging_handler.handler.DiscordWebHookHandler',
            'webhook_url': DISCORD_WEBHOOK_URL
        }
    },
    'root': {
        'handlers': ['console', 'file', 'discord'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'CRITICAL',
            'propagate': True,
        },
        'vaultapi': {
            'handlers': ['console', 'file', 'discord'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
```

### Environment Variable

DISCORD_WEBHOOK_URL - Your Discord webhook URL
