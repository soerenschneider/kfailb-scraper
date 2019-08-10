import datetime


class ClosingHours:
    """
    ClosingHours takes into account that the website is 'closed' during
    the night. Shooting requests at the target only wastes bandwidth and
    increases the chances of giving us away.
    """
    def __init__(self, start_time=None, end_time=None):
        if start_time is None:
            start_time = datetime.time(5,00)

        if end_time is None:
            end_time = datetime.time(1,0)

        self.start_time = start_time
        self.end_time = end_time

    def is_opened(self):
        """
        Determines whether the website is 'open' right now or not.
        :return: Returns True when the website is updating is considered open as of now,
        otherwise False.
        """
        now = datetime.datetime.now().time()
        if self.start_time < self.end_time:
            return self.start_time <= now <= self.end_time

        return now >= self.start_time or now <= self.end_time


class ClosingHoursDummy:
    def __init__(self, open=False):
        self.opened = open

    def is_opened(self):
        return self.opened
