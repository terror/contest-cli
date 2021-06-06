"utility related logic"

from datetime import datetime


class Utils:
  """all utility methods"""

  @staticmethod
  def convert_date(date) -> str:
    """converts an ISO 8601 date to readable format"""
    return datetime.fromisoformat(date).strftime("%B %d, %Y")

  @staticmethod
  def duration(time) -> str:
    """convert seconds to hours and return the appropriate message"""
    time //= 3600
    return f"{int(time)} hours" if time > 1 else f"{int(time)} hour"

  @staticmethod
  def url(url: str) -> str:
    """return the last part of a url"""
    return url.rsplit("/", 1)[-1]
