import logging
import requests
import json
from datetime import datetime

class DiscordWebHookHandler(logging.Handler):
    colour_map = {
        "DEBUG": 8421504,
        "INFO": 3447003,
        "WARNING": 16776960,
        "ERROR": 16711680,
        "CRITICAL": 10038562
    }

    def __init__(self, webhook_url, level=logging.ERROR, **kwargs):
        super().__init__(level)
        if not webhook_url:
            raise ValueError("webhook_url must be provided")
        self.webhook_url = webhook_url

    def emit(self, record):
        if self.formatter:
            log_entry = self.format(record)
        else:
            log_entry = record.getMessage()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if record.exc_info:
            import traceback
            log_entry += "\n" + "".join(traceback.format_exception(*record.exc_info))

        colour = self.colour_map.get(record.levelname, 0)
        payload = {
            "embeds": [{
                "title": f"Log ({record.levelname})",
                "description": f"```{log_entry}\n[{timestamp}]```",
                "color": colour
            }]
        }
        try:
            requests.post(
                self.webhook_url,
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
                timeout=5
            )
        
        except Exception:
            pass