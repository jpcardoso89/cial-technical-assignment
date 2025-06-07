from src.domain.model.market_cap import MarketCap


class Competitor:
    def __init__(self, name: str, market_cap: MarketCap):
        self.name = name
        self.market_cap = market_cap
