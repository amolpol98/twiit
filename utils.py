from datetime import date, datetime, timedelta
from decimal import Decimal
from django.utils import timezone
from json import JSONEncoder

default_tzone = timezone.get_default_timezone()


class APIJSONEncoder(JSONEncoder):
    """
    Extension to default json serializer
    Supports datetime, date and Decimal
    """

    def default(self, o):
        _cls = o.__class__
        if _cls == date:
            return o.isoformat()
        elif _cls == datetime:
            o = o.replace(microsecond=0)
            if o.tzinfo:
                o = o.astimezone(default_tzone)
            return o.isoformat()
        elif _cls == Decimal:
            int_val = int(o)
            return int_val if (int_val == o) else float(o)
        return JSONEncoder.default(self, o)
