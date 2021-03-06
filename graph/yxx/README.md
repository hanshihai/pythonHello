# y = ax^2 + bx + c

```
y = ax^2 + bx + c
  = a(x^2 + bx/a) + c
  = a(x + b/2a)^2 - b^2/4a + c
  = a(x + m)^2 + n

 m = b/2a
 n = (4ac - b^2)/4a
```

So

### the middle line: x = -m = -(b/2a)
### the delta of y: n

the origin curve m = 0 and n = 0:
![origin curve](init.png)

the move-left curve m = 1 and n = 0:
![origin curve](left.png)

the move-right curve m =-1 and n =0:
![origin curve](right.png)

the move-up curve m = 0 and n = 1:
![origin curve](up.png)

the move-down curve m = 0 and n = -1:
![origin curve](down.png)


The python code: https://github.com/hanshihai/pythonHello/blob/master/graph/yxx.py
