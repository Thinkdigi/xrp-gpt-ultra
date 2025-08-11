import os, time, asyncio, signal
from dotenv import load_dotenv
from rich.console import Console
from src.kucoin_client import KucoinClient
from src.news_fetcher import NewsFetcher
from src.strategy import StrategyEngine
from src.alerts import AlertBus

console = Console()
load_dotenv()

async def run():
    kc = KucoinClient()
    news = NewsFetcher()
    alerts = AlertBus()
    strat = StrategyEngine()

    console.rule('[bold cyan]XRP-GPT Ultra (Starter)')
    while True:
        try:
            spot = kc.get_spot_price()
            fut  = kc.get_fut_price()
            sig  = strat.tick(spot_price=spot, fut_price=fut)
            if sig:
                await alerts.push(f"Signal: {sig}")
            if news.should_poll():
                headlines = await news.fetch()
                if headlines:
                    await alerts.push(f"News: {headlines[0]['title']}")
            console.print(f"Spot: {spot:.5f} | Perp: {fut:.5f}", style="green")
        except Exception as e:
            console.print(f"[red]Loop error:[/red] {e}")
        await asyncio.sleep(3)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for s in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(s, loop.stop)
        except Exception:
            pass
    loop.run_until_complete(run())
