from pprint import pprint

# Class representing node of the tree
class Node(object):
    def __init__(self, data=None, left=None, right=None, level=None):
        self.data = data
        self.left = left
        self.right = right
        self.level = level

# Class with 2 variables representing 2 dimensions of KDTree
class Record(object):
    def __init__(self, loc=None, x=None, y=None):
        self.loc = loc
        self.xy = (x, y)

    def __str__(self):
        return ("(loc: {}, xy: {})".format(self.loc, self.xy))

# KDTree implementation with 2 dimensions
class KDTree(object):
    def __init__(self):
        self.tree = None
        self.result = []

    # Initialize the KDTree of 2 dimensions with root record
    def create(self, point):
        record = Record(point[0], point[1], point[2])
        self.tree = Node(record, None, None, 1)

    # Add a record based on below logic
    # 1. Root node has level 1 and it increases by 1 as we move to its children and grandchildren
    # 2. If the value of level is even, compare the incoming record on "loc"
    # 3. If the value of level is odd, compare the incoming record on "x"
    def add(self, point):
        record = Record(point[0], point[1], point[2])
        current = self.tree
        previous_level = current.level

        while True:
            previous_level = current.level

            if current.level % 2 != 0:
                if current.data.loc > record.loc:
                    if current.left is None:
                        current.left = Node(record, None, None, previous_level+1)
                        return current
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(record, None, None, previous_level+1)
                        return current
                    else:
                        current = current.right
            else:
                if current.data.xy[0] > record.xy[0]:
                    if current.left is None:
                        current.left = Node(record, None, None, previous_level+1)
                        return current
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(record, None, None, previous_level+1)
                        return current
                    else:
                        current = current.right

    # Find the nodes with 2 dimensions i.e. "loc" and "x"
    # Duplicate records are always placed to right of the node
    def findLocX(self, record):
        result = []
        current = self.tree
        while True:
            if current is None:
                return result

            if current.level % 2 != 0:
                if current.data.loc == record.loc and current.data.xy[0] == record.xy[0]:
                    result.append(current.data)
                    current = current.right
                elif current.data.loc > record.loc:
                    current = current.left
                else:
                    current = current.right
            else:
                if current.data.loc == record.loc and current.data.xy[0] == record.xy[0]:
                    result.append(current.data)
                    current = current.right
                elif current.data.xy[0] > record.xy[0]:
                    current = current.left
                else:
                    current = current.right

    # Find the nodes with 1st dimension i.e. "loc"
    def findLoc(self, current, record):
        if current != None:
            if current.data.loc == record.loc:
                self.result.append(current.data)
            self.findLoc(current.left, record)
            self.findLoc(current.right, record) 
        else:
            return False

    # Recursively call visualize to print left and right nodes of the tree
    def printAll(self, current):
        if current != None:
            pprint(vars(current.data))
            self.printAll(current.left)
            self.printAll(current.right) 
        else:
            return False