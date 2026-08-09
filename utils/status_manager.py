class STATUS:
    BAD = 0
    GOOD = 1

class StatusManager:
    def __init__(self):
        self._status = STATUS.GOOD

    def get_status(self):
        return self._status
    
    def force_good_state(self):
        self._status = STATUS.GOOD

    def throwE(self, expectation):
        print(expectation)
        self._status = STATUS.BAD
        raise Exception(expectation)