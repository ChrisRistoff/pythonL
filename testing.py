class SmasherJob:
    def __init__(self):
        self.workers = {
            "worker1": "Smasher",
            "worker2": "Other guy",
        }

    def force_elbow_through_nose(self):
        print(
            self.workers["worker1"]
            + " force elbow through nose of "
            + self.workers["worker2"]
        )


object = SmasherJob()
print(object.force_elbow_through_nose())
