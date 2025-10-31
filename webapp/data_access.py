import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
AGENT_DATA_DIR = REPO_ROOT / "data" / "agent_data"


def list_signatures() -> List[str]:
    if not AGENT_DATA_DIR.exists():
        return []
    return sorted(
        name
        for name in (p.name for p in AGENT_DATA_DIR.iterdir() if p.is_dir())
        if name.strip()
    )


def _position_file(signature: str) -> Path:
    return AGENT_DATA_DIR / signature / "position" / "position.jsonl"


def read_positions(signature: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
    file_path = _position_file(signature)
    if not file_path.exists():
        return []

    records: List[Dict[str, Any]] = []
    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if limit is not None and limit > 0:
        return records[-limit:]
    return records


def latest_position(signature: str) -> Optional[Dict[str, Any]]:
    records = read_positions(signature, limit=1)
    return records[-1] if records else None


def read_metrics(signature: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
    metrics_path = AGENT_DATA_DIR / signature / "metrics" / "metrics.jsonl"
    if not metrics_path.exists():
        return []

    rows: List[Dict[str, Any]] = []
    with metrics_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if limit is not None and limit > 0:
        return rows[-limit:]
    return rows


def latest_metrics(signature: str) -> Optional[Dict[str, Any]]:
    rows = read_metrics(signature, limit=1)
    return rows[-1] if rows else None


def repo_summary() -> Dict[str, Any]:
    signatures = list_signatures()
    totals: List[Tuple[str, Optional[float]]] = []
    for sig in signatures:
        latest = latest_position(sig)
        if not latest:
            totals.append((sig, None))
            continue
        cash = latest.get("positions", {}).get("CASH")
        totals.append((sig, cash if isinstance(cash, (int, float)) else None))

    return {
        "signatures": signatures,
        "cash_balances": [
            {"signature": sig, "cash": cash}
            for sig, cash in totals
        ],
    }
