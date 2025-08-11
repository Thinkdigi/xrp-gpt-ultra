# XRP-GPT Ultra — Copilot Starter PR

Tämä PR tuo minimiin supistetun **XRP-analyysiagentin** rungon. Se toimii sellaisenaan (paper/simulaatio), ja Copilot voi jatkaa tästä automaattisesti.

## Käyttö

```bash
cp .env.example .env   # täytä KuCoin READ-ONLY -avaimet
docker compose up --build -d
docker logs -f xrp-gpt-ultra
```

## Mitä mukana
- KuCoin-client (spot/fut tickerit, perus REST)
- Uutisskanneri (NewsNow XRP)
- Yksinkertainen strategiarunko (EMA + volyymisignaali, simuloitu)
- Telegram-hälytykset (valinnainen)
- CLI/looppi `main.py` — tulostaa Richillä tilannetiedot

## Mitä Copilotille pyydetään seuraavaksi (esimerkkitiketit)
- ATR/SR oikeasta kline-datasta
- Backtesteri
- Orderbook-whale analytiikka
- FastAPI + Dashboard
