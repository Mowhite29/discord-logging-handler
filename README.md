# Discord Logging Handler

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/discord-logging-handler?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/discord-logging-handler)
[![PyPI version](https://img.shields.io/pypi/v/discord-logging-handler)](https://pypi.org/project/discord-logging-handler/)
[![Python Version](https://img.shields.io/pypi/pyversions/discord-logging-handler)](https://pypi.org/project/discord-logging-handler/)
[![License](https://img.shields.io/pypi/l/discord-logging-handler)](https://github.com/yourusername/discord-logging-handler/blob/main/LICENSE)

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
