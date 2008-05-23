
def sched(l):
    rval = []
    if len(l) > 0:
        rval = sched1(l[0], l[1:]) + sched(l[1:])
    return rval

def sched1(o, l):
    return [(o, i) for i in l]

def schedule(l, n):
    num = len(l)
    iters = (n / (num - 1)) + 1
    return sched(l) * iters

def count(sched, o):
    return sum([1 for item in sched if o in item]) 


def remove(sch, item):
    index = sch.index(item)
    rval = [sch[i] for i in range(index)]
    rval += [sch[i] for i in range(index+1, len(sch))]
    return rval

def num_per(n):
    a, b = 2, 1
    while a < n:
        a, b = a+1, a+b
    return b


def remove_n(sch, l, threshold):
    new_sch = sch
    more = True
    while more:
        removed = {}
        for g in new_sch:
            if g[0] not in removed and g[1] not in removed:
                new_sch = remove(new_sch, g)
                removed[g[0]] = 1
                removed[g[1]] = 1
                if max([count(new_sch, o) for o in l]) == threshold:
                    more = False
                    break
    return new_sch

def sched_exact(l, n):
    """
    Schedule the list of 'teams' in l to play each other where
    each team should have at least n games
    """
    return remove_n(schedule(l, n), l, n)

def print_nums(sch, l):
    print [(o, count(sch, o)) for o in l]
    

# test
def test():
    l =  [1, 2, 3, 4]
    sch = sched_exact(l, 6)
    sch.sort()
    print sch
    print_nums(sch, l)




    
    
    
        
