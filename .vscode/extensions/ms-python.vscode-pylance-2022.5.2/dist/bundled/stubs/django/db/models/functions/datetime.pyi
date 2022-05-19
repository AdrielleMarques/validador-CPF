from typing import Any, Optional

from django.db import models
from django.db.models import Func, Transform

class TimezoneMixin:
    tzinfo: Any = ...
    def get_tzname(self) -> Optional[str]: ...

class Extract(TimezoneMixin, Transform):
    lookup_name: str
    output_field: models.IntegerField
    def __init__(
        self, expression: Any, lookup_name: Optional[str] = ..., tzinfo: Optional[Any] = ..., **extra: Any
    ) -> None: ...

class ExtractYear(Extract): ...
class ExtractIsoYear(Extract): ...
class ExtractMonth(Extract): ...
class ExtractDay(Extract): ...
class ExtractWeek(Extract): ...
class ExtractWeekDay(Extract): ...
class ExtractIsoWeekDay(Extract): ...
class ExtractQuarter(Extract): ...
class ExtractHour(Extract): ...
class ExtractMinute(Extract): ...
class ExtractSecond(Extract): ...

class Now(Func):
    output_field: models.DateTimeField

class TruncBase(TimezoneMixin, Transform):
    kind: str = ...
    tzinfo: Any = ...

class Trunc(TruncBase): ...
class TruncYear(TruncBase): ...
class TruncQuarter(TruncBase): ...
class TruncMonth(TruncBase): ...
class TruncWeek(TruncBase): ...
class TruncDay(TruncBase): ...

class TruncDate(TruncBase):
    output_field: models.DateField

class TruncTime(TruncBase):
    output_field: models.TimeField

class TruncHour(TruncBase): ...
class TruncMinute(TruncBase): ...
class TruncSecond(TruncBase): ...