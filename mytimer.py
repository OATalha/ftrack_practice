import timeit


class Timer:
    def __init__(self, name="Timer"):
        self.name = name
        self.start()
        self.num = 0

    def start(self, name=None):
        if name is not None:
            self.name = name
        self.start_time = timeit.default_timer()

    def elapsed(self):
        self.num += 1
        return timeit.default_timer() - self.start_time

    def print_elapsed(self, checkpoint=None):
        elapsed = self.elapsed()
        if checkpoint is None:
            checkpoint = "checkpoint {}".format(self.num)
        print(
            "{}: {} seconds elapsed at {}".format(
                self.name, elapsed, checkpoint
            )
        )
