# semantic analyszer for C Minus language

* Josh Lowy | N01177471 | cop4620

## symbol table data type (python)

```[  [ {dictionary1-1}, {dictionary1-2}, {dictionary1-3} ], [ {dictionary2-1} ], [ {dictionary3-1} ]  ]```

## performs the following semantic checks:

### expression declarations e.g. ``a = 24;`` ... a must be a variable of type int

* each variable used being used in an expression must have matching data types ``[ arrays special case ? ]``
* for assignments, the variable being given a value must have been declared to be a data type that matches the value of which it is being assigned ``again [ arrays may be special case ] because you could have a variable declared as an int legally be assigned a single value from an array of integers``

### scope

* when a function call is made, append the arguments (parameters) given to the dictionary fields of the respective function scope
* if function call is used in an assignment expression, use the return value of the function called
* 

### nested scope i.e. functions declared within function 

* reason for creating **list of lists of dictionaries**  ... the second layer of lists is used for nested scope ( i.e. functions declared within functions )

### return value checks

* return value must match the data type of the given function

### function declarations:

* **main() function must be last function declared in program**
* no duplicate function declarations
* declared data type matches return data type -> ex. ``int foo(int num1){}`` returns an int 
* no return if function data type is void

### function calls

* number of arguments passed in function **MUST** match the number of parameters declared in the function
* data type of each argument passed in function call **MUST** match the associated parameter data types declared in the function

### special cases

## Uses a list of lists of dictionaries ex. [[]]

* each list of dictionaries defines a scope 
* the first dictionary in each list will define the name of the scope/function

ex. [[dict1(func declaration), dict2(local declarations), dict3, dict4,etc..], [dict1(func declcaration), dict2, etc..]]
[[scope1], [scope2], [scope3]]