from collections import deque

class StrategyEngine:
    """Hyvin kevyt signaalirunko (placeholder).
    Copilotin on helppo laajentaa tämä oikeiksi indikaattoreiksi/backtesteriksi.
    """
    def __init__(self, win=5):
        self.last = deque(maxlen=win)
    def tick(self, spot_price: float, fut_price: float):
        self.last.append(spot_price)
        if len(self.last) < self.last.maxlen:
            return None
        # Erittäin yksinkertainen: jos 5 viimeistä nousee → "LONG", jos laskee → "SHORT"
        inc = all(self.last[i] <= self.last[i+1] for i in range(len(self.last)-1))
        dec = all(self.last[i] >= self.last[i+1] for i in range(len(self.last)-1))
        if inc:  return {"side":"LONG","confidence":0.5}
        if dec:  return {"side":"SHORT","confidence":0.5}
        return None
