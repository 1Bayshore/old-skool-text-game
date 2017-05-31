class Event:
    def __init__(self, timestamp, callback, payload):
        self.timestamp = timestamp
        self.callback = callback
        self.payload = payload

    def activate(self):
        self.callback(self.payload)

class EventQueue:
    def __init__(self):
        self.Q = []
    
    # TODO: make this more efficient. Right now it re-sorts every time
    def schedule(self, timestamp, callback, payload):
        ev = Event(timestamp, callback, payload)
        index = 0
        for w in self.Q:
            if w.timestamp < ev.timestamp:
                index += 1
        self.Q.insert(index, ev)

    def check_for_event(self, timestamp):
        if Q[0] <= timestamp:
            ev = Q[0]
            del Q[0]
            return ev
        else:
            return None
