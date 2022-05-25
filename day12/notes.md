* in Python there is no Block Scope: if you create a variable within an if block, or a while loop, or a for loop, does not create a separate local scope.
* To modify a global variable inside a local scope, it is necessary to declare it with the global prefix. In example:

```python
enemies = 1

def increase_enemies():
  global enemies 
  enemies += 1
```

Anyways, it is not a recommended approach though. Try to avoid modifying global variables inside local scopes, you can read it and use it without having to declare it as a global inside the scope, but try to avoid modifying it.
