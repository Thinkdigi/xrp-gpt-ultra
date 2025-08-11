import os, asyncio, httpx
from typing import Optional

TG_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TG_CHAT  = os.getenv('TELEGRAM_CHAT_ID')

class AlertBus:
    def __init__(self):
        self.enabled = bool(TG_TOKEN and TG_CHAT)
    async def push(self, msg: str):
        print(f'[ALERT] {msg}')
        if not self.enabled: return
        async with httpx.AsyncClient(timeout=10) as c:
            url = f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
            await c.post(url, data={'chat_id': TG_CHAT, 'text': msg})
