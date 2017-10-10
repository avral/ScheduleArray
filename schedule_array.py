class ScheduleArray:
    """
    Returns items with the specified delay.
    Items need to be list or tuples [(item: delay)], delay can be 0

    delay should be in seconds
    """

    def __init__(self, items=None):
        self.items = [
            (i[0], self._delay(i[1]))
            for i in items
        ] if items else []

    def __iter__(self):
        return self

    def _delay(self, seconds):
        return datetime.now() + timedelta(seconds=seconds)

    def append(self, item, delay):
        ready_time = self._delay(delay)

        self.items.append((item, ready_time))

    def __next__(self):
        while self.items:
            try:
                item = next(i for i in self.items if i[1] <= datetime.now())
                self.items.remove(item)

                return item[0]
            except StopIteration:
                time.sleep(0.1)

        raise StopIteration
