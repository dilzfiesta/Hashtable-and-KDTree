from KDTree import KDTree, Record
from pprint import pprint
from Visualize import Visualize

# Object that holds the result values
class ReturnObject:
    def __init__(self):
        self.code = 0
        self.message = ""
        self.data = []

# Hash Table implementation
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self._createBuckets()
  
    # Create buckets based on the input size 
    def _createBuckets(self):
        return [[] for _ in range(self.size)]

    # Create KD Tree for each bucket
    def _createKDTree(self, point):
        tree = KDTree()
        tree.create(point)
        return tree

    # Generate hash of the string using the default hash function
    def _getHash(self, loc):
        return hash(loc) % self.size

    # Find all elements with the value of "loc"
    def findLoc(self, loc):
        returnObj = ReturnObject()
        hashed_key = self._getHash(loc)
        tree = self.hash_table[hashed_key]
        if isinstance(tree, list):
            returnObj.code = 404
            returnObj.message = "Error: The hash value is not mapped to any bucket, hence the data is not present"
        else:
            tree.result = []
            tree.findLoc(tree.tree, Record(loc))
            returnObj.code = 200
            returnObj.message = "Node(s) found -"
            for record in tree.result:
                returnObj.data.append(record)
        return returnObj

    # Find all elements with the value of "loc" and 'x
    def findLocX(self, loc, x):
        returnObj = ReturnObject()
        hashed_key = self._getHash(loc)
        tree = self.hash_table[hashed_key]
        if isinstance(tree, list):
            returnObj.code = 404
            returnObj.message = "Error: The hash value is not mapped to any bucket, hence the data is not present"
        else:
            records = tree.findLocX(Record(loc, x))
            returnObj.code = 200
            returnObj.message = "Node(s) found -"
            for record in records:
                returnObj.data.append(record)
        return returnObj

    # Internal method to add a single object to the bucket
    def _add(self, point):
        hashed_key = hash(point[0]) % self.size
        tree = self.hash_table[hashed_key]
        if isinstance(tree, list):
            tree = self._createKDTree(point)
        else:
            tree.add(point)
        self.hash_table[hashed_key] = tree

    # Add (loc,xyval[][],N), add N records each with loc==str and x==xyval[i][0] and y==xyval[i][1]
    def addLoc(self, loc, xyval, N):
        for i, d in enumerate(xyval):
            self._add((loc, d[0], d[1]))

    # Supplimentary methods to print the result 
    def printResult(self, output):
        if(output.code == 200):
            print(output.message)
            for branch in output.data:
                pprint(vars(branch))
        elif(output.code == 404):
            print(output.message)
        else:
            print("Error: Something went wrong")

    # Supplimentary methods to visualize the whole tree per bucket
    def visualize(self):
        for i, tree in enumerate(self.hash_table):
            print("Bucket: {} -".format(i))
            if type(tree) == KDTree:
                node = tree.tree
                v = Visualize()
                v.printBTree(node, lambda n:(str(n.data), n.left, n.right)) 
            else:
                print("Error: Bucket is empty")
            print("\n")