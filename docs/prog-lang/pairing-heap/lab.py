import random
from pprint import pprint

COMPS = 0
def INC_COMPS():
    global COMPS
    COMPS += 1

names = ["Valeria", "Victor", "Vincent", "Vivian", "Varsha",
          "Vidya", "Vinny", "Van", "Veda"]

codes = {"Red": (0, 1), "Amber": (1, 10), "Yellow": (11, 60),
          "Green": (61, 120), "Blue": (121, 240)}

patients = []
for name in names:
    code, triage = random.choice(list(codes.items()))
    value = int(random.uniform(*triage))
    patients.append([name, code, value])

patients = [
    ("Valeria", "amber", 1),
    ("Victor", "green", 84),
    ("Vincent", "amber", 6),
    ("Vivian", "red", 0),
    ("Varsha", "blue", 168),
    ("Vidya", "blue", 200),
    ("Vinny", "yellow", 56),
    ("Van", "green", 98),
    ("Veda", "blue", 223)
]

pprint(patients)

# Priority Queue with List
print("\nPQ as List")

def new():
    return []
def is_empty(pq):
    return not bool(pq)
def insert(pq, patient):
    def comp(p1, p2):
        INC_COMPS()
        return p1[2] < p2[2]

    i = 0
    while i < len(pq) and comp(pq[i], patient):
        i += 1
    pq.insert(i, patient)

pq = new()
for patient in patients:
    insert(pq, patient)
pprint(pq)

print()
print(f"Comps: {COMPS}")

# Priority Queue with Pairing Heap
print("\nPQ as Pairing Heap")

COMPS = 0

def new():
    return []
def build(patient, *subheaps):
    return [patient, list(subheaps)]
def is_empty(pq):
    return not bool(pq)
def merge(pq, heap):
    def comp(p1, p2):
        INC_COMPS()
        return p1[2] < p2[2]
    if is_empty(heap): return pq
    elif is_empty(pq): return heap
    elif comp(pq[0], heap[0]):
        pq[1].insert(0, heap)
        return pq
    else:
        heap[1].insert(0, pq)
        return heap
def meld(heaps):
    match heaps:
        case []: return new()
        case [e]: return e
        case [h1, h2, *rest]: return merge(merge(h1, h2), meld(rest))

pq = new()
for patient in patients:
    patient = build(patient)
    pq = merge(pq, patient)
pprint(pq)
print(f"Comps: {COMPS}\n")

pq = meld(pq[1])
pprint(pq)
print(f"Comps: {COMPS}")
