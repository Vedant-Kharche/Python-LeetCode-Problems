class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)

        while t - self.q[0] > 3000:
            self.q.popleft()
            
        return len(self.q)