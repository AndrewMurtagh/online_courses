# Computing runtimes

The actual runtime of an algorithm depends on many attributes of the computer: speed of CPU, memory hierarchy, bus speed, compiler. Most of these factors multiply the runtime by a constant factor, i.e. a 100x faster CPU will scale the runtime by a constant.

Key idea of asymptotic notation is to measure runtime in a way that ignores constant multiples. In reality, the constants can matter and should be considered when doing optimisations.

So we look at how the runtime scales in proportion to the input size. So long as the input size is large enough, this is mostly what determines the actual runtime.


Ordering: `log(n) < sqrt(n) < n < nlog(n) < n<sup>2</sup> < 2<sup>n</sup> < n!`


![Large input sizes](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Comparison_computational_complexity.svg/330px-Comparison_computational_complexity.svg.png)


![Low input sizes](https://res.cloudinary.com/practicaldev/image/fetch/s--sMct5uyv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/8ci1gllgkvpo52kj2e7b.png)

## Big-O Notation

Definition: take two functions, `f(n)` and `g(n)`

`f(n) = O(g(n))` ,i.e. `f` is Big-O of `g` if there exists `N` and `c` so that for all `n > N`, `f(n) < c.g(n)`

so `f` is bounded by some constant multiple of `g` for large inputs.

g is actual runtime function but f (i.e. O(g) ) it is bounded pretty close (some multiple) of the real function.


### Advantages

* Gives idea of growth rate.

* Cleans up notation `O(nlog(n))` vs. `4nlog<sub>4</sub>(3n) + 7`

* Allows us to ignore computer architecture, i.e. constant multiples


### Disadvantages

* Ignores constant multiples, should look at these in optimisation stage.

* Only asymptotic, only tells you something about the algorithm when you give it large input sizes.


### Rules

* multiplicative constants can be ignored: `7n<sup>2</sup> -> O(n<sup>2</sup>)`, `n<sup>2</sup>/3 -> O(n<sup>2</sup>)`

* The larger power grows quicker: `O(n<sup>2</sup>)` < `O(2<sup>n</sup>)`

* Exponentials grow faster than polynomials: `O(n<sup>a</sup>) < O(n<sup>b</sup>)` where `a` < `b`

* Polynomials grow faster than logs: `O(log(n)<sup>a</sup>) < O(n<sup>a</sup>)`

* Disregard bases of logs: `log<sub>4</sub>(n) -> O(log(n))`

* Smaller terms can be omitted: `n<sup>2</sup> + n -> O(n<sup>2</sup>)`, `2<sup>n</sup> + n<sup>10</sup> -> O(2<sup>n</sup>)`

### e.g.

```
arr = []\tO(n)
arr[0] = 0\tO(1)
arr[1] = 1\tO(1)
for i in range(2,n+1):\tO(n)
\tarr[i] = arr[i-1] + arr[i-2]\tO(n)
return arr[n]\tO(1)

= O(n)+O(1)+O(1)+O(n) * O(n)+O(1)
= O(n<sup>2</sup>)
```

### Other notations

f is bounded below g, i.e. grows no slower than gthen f = omega(g), f > c.(g)

f grows at same rate as g. f is theta is omega is big-o of g

f grows strictly slower than g is little-o of g. Ratio of f and g goes to zero as n -> inf.
