# ScheduleArray
A class of a list that returns elements with a specified delay.

Example:

```python
a = [1, 2, 3]

sa = ScheduleArray((i, 0) for i in a)

for i in sa:
    print(i)

    if <some condition>:
        sa.append(10, 10)

```

result:
```
1
2
3
after 10 seconds..
10
```
