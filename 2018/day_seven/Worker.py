import string

class Worker:

    def __init__(self, worker_number):
        self.worker = worker_number
        self.time_left = 0
        self.step = None
    
    def start_progress(self, step):
        self.step = step
        self.time_left = string.ascii_lowercase.index(step.lower()) + 61
    
    def countdown(self):
        if not self.is_free() and self.time_left > 0:
            self.time_left -= 1
            if self.time_left == 0:
                completed_step = self.step
                self.step = None
                return completed_step
        return None
    
    def is_free(self):
        return self.step == None

    def stop_work(self):
        self.step = None