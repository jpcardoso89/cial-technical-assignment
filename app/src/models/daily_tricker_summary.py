class DailyTickerSummary:

    def __init__(self, **kwargs):
        self._after_hours = kwargs.get("afterHours")
        self._close = kwargs.get("close")
        self._from = kwargs.get("from")
        self._high = kwargs.get("high")
        self._low = kwargs.get("low")
        self._open = kwargs.get("open")
        self._pre_market = kwargs.get("preMarket")
        self._status = kwargs.get("status")
        self._symbol = kwargs.get("symbol")
        self._volume = kwargs.get("volume")
        