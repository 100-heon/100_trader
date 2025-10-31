import os
import requests
from typing import List, Optional

UPBIT_API_BASE = os.environ.get("UPBIT_API_BASE", "https://api.upbit.com")


def get_all_krw_symbols(max_symbols: Optional[int] = None) -> List[str]:
    """Fetch all Upbit KRW market symbols (e.g., BTC, ETH, SOL ...).

    Args:
        max_symbols: optional cap to limit list size.

    Returns:
        List of symbol strings without the KRW- prefix.
    """
    url = f"{UPBIT_API_BASE}/v1/market/all"
    try:
        resp = requests.get(url, params={"isDetails": "false"}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception:
        return []

    symbols: List[str] = []
    for item in data if isinstance(data, list) else []:
        market = item.get("market", "")
        if market.startswith("KRW-"):
            symbols.append(market.split("-", 1)[1])

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for s in symbols:
        if s not in seen:
            seen.add(s)
            unique.append(s)

    if max_symbols and max_symbols > 0:
        return unique[:max_symbols]
    return unique


def get_top_krw_symbols_by_24h_value(top_n: int = 20) -> List[str]:
    """Return KRW symbols sorted by 24h traded value (descending), top N.

    Steps:
      1) Fetch all KRW markets via /v1/market/all
      2) Batch call /v1/ticker?markets=... to get 24h stats
      3) Sort by acc_trade_price_24h desc and return top_n symbols (without KRW-)
    """
    markets = [f"KRW-{s}" for s in get_all_krw_symbols()]
    if not markets:
        return []

    url = f"{UPBIT_API_BASE}/v1/ticker"
    results = []

    # Upbit supports comma-separated markets; batch to avoid URL length issues
    batch_size = 50
    for i in range(0, len(markets), batch_size):
        batch = markets[i:i+batch_size]
        try:
            resp = requests.get(url, params={"markets": ",".join(batch)}, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                results.extend(data)
        except Exception:
            continue

    # Build list of (symbol, value)
    scored: List[tuple[str, float]] = []
    for item in results:
        market = item.get("market", "")
        if not market.startswith("KRW-"):
            continue
        sym = market.split("-", 1)[1]
        value = 0.0
        try:
            value = float(item.get("acc_trade_price_24h") or 0.0)
        except Exception:
            value = 0.0
        scored.append((sym, value))

    # Deduplicate by symbol keeping max value seen
    max_by_sym = {}
    for sym, val in scored:
        if sym not in max_by_sym or val > max_by_sym[sym]:
            max_by_sym[sym] = val

    top = sorted(max_by_sym.items(), key=lambda x: x[1], reverse=True)
    return [sym for sym, _ in top[:max(0, int(top_n))]]
