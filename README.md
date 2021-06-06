# Requirement
Write a program to read a list of records of the form <loc,x,y>  from  a file and store them in a hashtable such that -  loc is used as the key for hashing - each bucket is a kd-tree for k=2. Note that loc is a string and x and y are positive integers.

# Implement Operations 
1. findLoc(str), find all records with loc==str 
2. findLocx(str, xval), find all records with loc==str and x==xval  
3. addLoc(str,xyval[][],N), add N records each with loc==str and x==xyval[i][0] and y==xyval[i][1]

# System Requirement
1. Python 3.6.4 and above

# Execution
1. Add records in records.csv in format - loc,x,y where loc is string and x & y are integers
2. Execute the program using below command - 
    ```
    python Main.py
    ```

# Add Records in KDTree
1. Root node has level 1 and it increases by 1 as we move to its children and grandchildren
2. If the value of level is even, compare the incoming record on x-axis ("loc"). If incoming record is less than the current node, move it to the left subtree or else right subtree respectively
3. If the value of level is odd, compare the incoming record on y-axis ("x"). If incoming record is less than the current node, move it to the left subtree or else right subtree respectively
4. Repeat steps 2 and 3 repeatedly until the new record is added at the leaf 

# Find Records in KDTree
1. Root node has level 1 and it increases by 1 as we move to its children and grandchildren
2. If the value of level is even, compare the incoming record on x-axis ("loc"). If incoming record is less than the current node, search the left subtree or else right subtree and repeat the process
3. If the value of level is odd, compare the incoming record on y-axis ("x"). If incoming record is less than the current node, search the left subtree or else right subtree and repeat the process
4. Repeat steps 2 and 3 repeatedly until the new record is found
5. Duplicate records are always found at the right subtree

# Sample Output

## Print contents of all buckets:
**Bucket: 0 -**
```
         (loc: apple, xy: (1, 2))        
                      \
            (loc: strawberry, xy: (9, 7))
                         /
(loc: chikoo, xy: (5, 7))
             \
  (loc: chikoo, xy: (5, 7))
```

**Bucket: 1 -**
```
           (loc: banana, xy: (4, 5))
                        \
             (loc: banana, xy: (4, 1))
                        / \
(loc: mango, xy: (2, 9))   (loc: mango, xy: (4, 6))
             \                          \
   (loc: mango, xy: (2, 1))   (loc: mango, xy: (9, 1))
                                        /
                  (loc: zoo, xy: (8, 3))
                           /  \
   (loc: phone, xy: (4, 1))    (loc: zoo, xy: (4, 1))
```

**Bucket: 2 -**
```
(loc: aam, xy: (4, 5))
            \
   (loc: laptop, xy: (1, 3))
```

## Find all strings with value {loc: mango}
```
Node(s) found -
{'loc': 'mango', 'xy': (2, 9)}
{'loc': 'mango', 'xy': (2, 1)}
{'loc': 'mango', 'xy': (4, 6)}
{'loc': 'mango', 'xy': (9, 1)}
```

## Find all strings with value {loc: mango, x: 2}
```
Node(s) found -
{'loc': 'mango', 'xy': (2, 9)}
{'loc': 'mango', 'xy': (2, 1)}
```
