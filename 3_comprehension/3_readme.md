# Comprehension
comprehension refers to a concise way to construct new sequences (like lists, dictionaries, or sets) using a single line of code. It’s typically more readable and faster than traditional loops.

Types :- 
1. List comprehension
2. Set comprehension
3. Dictionary comprehension
4. Generator comprehension

> [] is for lists

> {} is for sets and dicts

> () is for tuples and generators

## 1. List Comprehension

```python
num = [1,2,3,4,5,6,7]

squared_num= [x**2 for x in num]

squared_even_num = [x**2 for x in num if x%2==0]
```

## 2. Set Comprehension

```python
nums= [1, 2, 2, 3, 3]
unique_squares = {x**2 for x in nums}
print(unique_squares)  # Output: {1, 4, 9}


students = {
    'Arts':['Ravi','Mohit','Ashish'],
    'Commerce' :['Monu','Daksh','Ravi'],
    'Non Medical' :['Sahil','Pardeep',"Ashish","Mohit"]
}

# using multiple for conditions -- we can add more if we want
unique_students = [unique_student for student in students.values() for unique_student in student]
print(unique_students)
```

## 3. Dictionary Comprehension
```python
nums=[1,2,3,4,5]
squares_of_num = { x:x**2 for x in nums}
print(squares_of_num)

# 2nd example
milk_rate_inr={
    'Cow':40,
    'Buffalo':80,
    'Sheep' :150
}

milk_rate_usd = { animal:price/85 for animal,price in milk_rate_inr.items() }

print(milk_rate_usd)
```

## 4. Generators
Generators are a type of iterable, like lists or tuples, but they generate values on the fly instead of storing them all in memory at once. They are used to create iterators in a memory-efficient and lazy way(Values are computed only when needed (not all at once)).

```python
gen = (x**2 for x in range(5))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

```