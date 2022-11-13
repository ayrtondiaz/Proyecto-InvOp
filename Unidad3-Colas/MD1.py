import random
import queue

class Customer(object):
    def __init__(self, cid, arrival_time):
        self.cid = cid
        self.arrival_time = arrival_time
        self.departure_time = None
        
    def get_wait(self):
        if self.departure_time is None:
            return None
        else:
            return self.departure_time - self.arrival_time
        
    def __str__(self):
        return "Customer({}, {})".format(self.cid, self.arrival_time)
    
    def __repr__(self):
        return str(self)

def simulate_md1(lambd, mu, max_time, verbosity = 0):
    md1 = queue.Queue()
    served_customers = []
    unserved_customers = []
    
    next_arrival = random.expovariate(lambd)
    next_service = next_arrival + 1/mu

    t = next_arrival

    cid = 1
    
    while t < max_time:

        if t == next_arrival:
            customer = Customer(cid, arrival_time = t)
            cid += 1
            md1.put(customer)

            if verbosity >= 2:
                print("{:10.2f}: Customer {} arrives".format(t, customer.cid))

            next_arrival = t + random.expovariate(lambd)
            
        if t == next_service:
            done_customer = md1.get()
            done_customer.departure_time = t
            
            served_customers.append(done_customer)

            if verbosity >= 2:
                print("{:10.2f}: Customer {} departs".format(t, done_customer.cid))            
            
            if md1.empty():
                next_service = next_arrival + 1/mu
            else:
                next_service = t + 1/mu
            
        if verbosity >= 1:
            print("{:10.2f}: {}".format(t, "#"*md1.qsize()))
            
        t = min(next_arrival, next_service)
        
    while not md1.empty():
        unserved_customers.append(md1.get())
        
    return served_customers, unserved_customers

simulate_md1(1, 1, 100, verbosity = 2)