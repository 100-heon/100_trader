from __future__ import annotations

from datetime import datetime, timedelta, timezone
import time


# KST (UTC+9)
KST = timezone(timedelta(hours=9))


def get_kst_now() -> datetime:
    return datetime.now(tz=KST)


def get_kst_today_str() -> str:
    return get_kst_now().date().isoformat()


def is_weekend(date_str: str) -> bool:
    dt = datetime.strptime(date_str, "%Y-%m-%d").date()
    return dt.weekday() >= 5  # 5=Sat, 6=Sun


def previous_business_day(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d").date()
    while dt.weekday() >= 5:
        dt = dt - timedelta(days=1)
    return dt.isoformat()


def latest_trading_date_kst(include_today: bool = True) -> str:
    today = get_kst_today_str()
    if include_today and not is_weekend(today):
        return today
    return previous_business_day(today)


def seconds_until_next_bar_kst(minutes: int) -> int:
    """Seconds until the next bar boundary in KST.

    For example, minutes=60 aligns to the next HH:00; minutes=10 aligns to next HH:MM where MM%10==0.
    """
    now = get_kst_now()
    m = max(1, int(minutes))
    # Next minute boundary that is a multiple of m
    next_minute_block = (now.minute // m + 1) * m
    carry_hours = next_minute_block // 60
    target_minute = next_minute_block % 60
    target_hour = (now.hour + carry_hours) % 24
    target_day = now.date()
    if now.minute >= target_minute and carry_hours == 0:
        # Should not happen due to calculation, but guard anyway
        carry_hours = 1
    if carry_hours:
        # may roll to next day; datetime handles overflow if we rebuild using replace + timedelta
        target = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=carry_hours)
    else:
        target = now.replace(minute=target_minute, second=0, microsecond=0)
    delta = target - now
    return max(1, int(delta.total_seconds()))


def sleep_until_next_bar_kst(minutes: int) -> None:
    secs = seconds_until_next_bar_kst(minutes)
    time.sleep(secs)
