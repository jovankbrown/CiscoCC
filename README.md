# Cisco Code Challenge

Author: Jovan Brown

## Test_001

Write a method that answers the following problem:

Accept as input:
- list: a singly-linked list.

Remove the middle element of the list without iterating the list more than once.  Assume the list size cannot be known until traversed.


```python
class Node:
    ...

class LinkedList:
    ...
```

## Test_002

Write a method that answers the following problem:

Accept as input:
- list: an unordered list of arrays each with 4 elements.
- target: an integer

Find and display the complete array that contains the provided target number. 


```python
def search_nested(mylist, val):
    ...
```

## Test 003
- Write a query that lists each member name, address, dues and location.
```sql
SELECT members.name, members.address, organization.dues, organization.location
FROM members
INNER JOIN mambers ON members.id = organization.id;
```
- Write a SQL Query to pull all members that are over 45
```sql
SELECT *
FROM members
WHERE age > 45
```
- Write a SQL Query to pull all members that have a dues value of 0.
```sql
SELECT *
FROM members
INNER JOIN mambers ON members.id = organization.id
WHERE organization.dues = 0
```