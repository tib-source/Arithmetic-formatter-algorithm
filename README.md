# Arithmetic-formatter-algorithm
Arithmetic formatter


A function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function optionally takes a second argument - display. When the second argument is set to `True`, the answers are displayed.

### For example

Function Call:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```


Situations that will return an error:
  * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
    `Error: Too many problems.`
  * The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
    `Error: Operator must be '+' or '-'.`
  * Each number (operand) should only contain digits. Otherwise, the function will return:
    `Error: Numbers must only contain digits.`
  * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
    `Error: Numbers cannot be more than four digits.`

