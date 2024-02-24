# Please write a program to generate all sentences where subject is in
# ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

#MY SOLUTION:
subject = ["I", "You"]
verb = ["Play", "Love"]
ob_ject = ["Hockey","Football"]

# Efficient way of doing it.
for subs in subject:
    for vrb in verb:
        for obj in ob_ject:
            print(subs, vrb, obj)

# Manual way of doing it.
a = [subject[0], verb[0], ob_ject[0]]
print(' '.join(a))
b = [subject[0], verb[0], ob_ject[1]]
print(' '.join(b))
c = [subject[0], verb[1], ob_ject[0]]
print(' '.join(c))
d = [subject[0], verb[1], ob_ject[1]]
print(' '.join(d))
e = [subject[1], verb[0], ob_ject[0]]
print(' '.join(e))
f = [subject[1], verb[0], ob_ject[1]]
print(' '.join(f))
g = [subject[1], verb[1], ob_ject[0]]
print(' '.join(g))
h = [subject[1], verb[1], ob_ject[1]]
print(' '.join(h))

#COURSE SOLUTION:
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))
