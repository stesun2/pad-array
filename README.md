
# Create Two Methods to Pad an Array

## This challenge will help you to:
- Break a large problem down into smaller steps using pseudocode
- Research and use Python methods
- Differentiate between destructive and non-destructive methods

So far we have mainly worked with non-destructive methods, which do not modify the original input as it returns a new object with a different set of values. In this challenge, you'll explore destructive methods, which replace the original data.  

Can you identify situations in which each approach would be used?


## Let's get started

In this challenge, you'll want to write two methods `pad` and `pad_destructive`. Each method accepts a list, a minimum size (non-negative integer) for the list, and an optional argument of what the list should be "padded" with (see the example with "apple" below).

If the list's length is less than the minimum size, `pad` should return a new list padded with the pad value up to the minimum size.

For example,
```python
pad([1,2,3], 5)
```

should return

```python
[1,2,3,None,None]
```

And

```python
pad([1,2,3], 5, 'apple')
```

should return

```python
[1,2,3,'apple', 'apple']
```

If the minimum size is less than or equal to the length of the list, it should just return the list.

That is, `pad([1,2,3], 3)` should return `[1,2,3]`.

`pad(my_array, 0)` should always return a list equal to `my_array`. `pad` should also always return a new object, so it should be non-destructive.


Keep your initial solution basic and concentrate on passing the tests in the included test suite. There is no need to use a ton of fancy built-in python methods in your initial solutions.



