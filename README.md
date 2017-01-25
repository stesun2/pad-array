
# Create Two Methods to Pad an Array

## This challenge will help you to:
- Break a large problem down into smaller steps using pseudocode
- Research and use Ruby methods
- Differentiate between destructive and non-destructive methods

So far we have mainly worked with non-destructive methods, which do not modify the original input as it returns a new object with a different set of values. In this challenge, you'll explore destructive methods, which replace the original data. N.B. In Ruby, the general convention is to add a "banger" (`!`) to destructive methods, but not always. 

Can you identify situations in which each approach would be used?


## Let's get started

In this challenge, you'll want to write two methods `pad` and `pad!`. Each method accepts an array, a minimum size (non-negative integer) for the array, and an optional argument of what the array should be "padded" with (see the example with "apple" below).

If the array's length is less than the minimum size, `pad` should return a new array padded with the pad value up to the minimum size.

For example,
```ruby
pad([1,2,3], 5)
```

should return

```ruby
[1,2,3,nil,nil]
```

And

```ruby
pad([1,2,3], 5, 'apple')
```

should return

```ruby
[1,2,3,'apple', 'apple']
```

If the minimum size is less than or equal to the length of the array, it should just return the array.

That is, `pad([1,2,3], 3)` should return `[1,2,3]`.

`pad(my_array, 0)` should always return an array equal to `my_array`. `pad` should also always return a new object, so it should be non-destructive.


Keep your initial solution basic and concentrate on passing the tests in the included RSpec suite. There is no need to use a ton of fancy built-in Ruby methods in your initial solutions.

## Stretch challenge:

Now go into the Ruby Docs to see if there are any enumerable methods you can simplify your code with. Also refactor for readability, and remember, one liners aren't necessarily the most efficient or "best" code.

Make sure your code still passes the tests!

