import datetime

from kfailb import ClosingHours


class TestClosingHours:
    def test_is_opened_open(self):
        now = datetime.datetime.now()
        start = now.time()
        end = (now + datetime.timedelta(minutes=5)).time()

        impl = ClosingHours(start_time=start, end_time=end)
        assert impl.is_opened() is True

    def test_is_opened_closed(self):
        now = datetime.datetime.now()
        start = (now + datetime.timedelta(minutes=5)).time()
        end = (now + datetime.timedelta(hours=5)).time()

        impl = ClosingHours(start_time=start, end_time=end)
        assert impl.is_opened() is False
