from datetime import datetime
import random

def partition(xs, start, end):
  follower = leader = start
  while leader < end:
    if xs[leader] <= xs[end]:
      xs[follower], xs[leader] = xs[leader], xs[follower]
      follower += 1
    leader += 1
  xs[leader], xs[follower] = xs[follower], xs[leader]
  return follower

def _quicksort(xs, start, end):
  if start >= end:
    return
  p = partition(xs, start, end)
  _quicksort(xs, start, p-1)
  _quicksort(xs, p+1, end)

def quicksort(xs):
  _quicksort(xs, 0, len(xs)-1)

xs = [random.randrange(1000) for _ in range(100000)]
print(xs[:10], xs[-10:])

# Here we start the clock
t1 = datetime.now()
quicksort(xs)
t2 = datetime.now()
print("Sorted list of size {} in {}".format(len(xs), t2-t1))

print(xs[:10], xs[-10:])