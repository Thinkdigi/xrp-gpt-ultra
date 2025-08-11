import os, time, asyncio, httpx
from bs4 import BeautifulSoup

NEWS_URL = os.getenv('NEWSNOW_URL','https://www.newsnow.co.uk/h/Business+&+Finance/Cryptocurrencies/XRP?type=ln')

class NewsFetcher:
    def __init__(self):
        self._last = 0
    def should_poll(self)->bool:
        return time.time()-self._last > 60
    async def fetch(self):
        self._last = time.time()
        try:
            async with httpx.AsyncClient(timeout=15) as c:
                r = await c.get(NEWS_URL, headers={'User-Agent':'Mozilla/5.0'})
                soup = BeautifulSoup(r.text, 'lxml')
                items = []
                for a in soup.select('a.newsfeed__title-link')[:10]:
                    items.append({'title': a.get_text(strip=True), 'url': a.get('href')})
                return items
        except Exception:
            return []
