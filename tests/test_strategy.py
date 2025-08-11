from src.strategy import StrategyEngine

def test_direction_detector():
    s = StrategyEngine(win=5)
    for v in [1,2,3,4,5]:
        sig = s.tick(v, v)
    assert sig and sig['side']=='LONG'
