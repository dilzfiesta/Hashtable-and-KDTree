import csv
from pprint import pprint
from Hashtable import HashTable

loc_records = []
xy_records = []

# Open records.csv and import records line by line
with open('records.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            loc = row[0].strip()
            x = int(row[1].strip())
            y = int(row[2].strip())

            try:
                loc_index = loc_records.index(loc)
            except ValueError:
                loc_records.append(loc)
                loc_index = loc_records.index(loc)
            
            try:
                xy_records[loc_index].append((x, y))
            except IndexError:
                xy_records.append([(x, y)])

            line_count += 1

# Create a Hashtable with buckets of size 1/4 of total number of objects
# Reason - we are creating KDTree to store collisions optimally
size = int(line_count/4)
ht = HashTable(size)

# Enumerate records and add them in Hashtable
for i, d in enumerate(loc_records):
    ht.addLoc(loc_records[i], xy_records[i], len(xy_records))

# Results
print("Print contents of all buckets:")
ht.visualize()
print("")

print("Find all strings with (loc: mango)")
ht.printResult(ht.findLoc("mango"))
print("")

print("Find all strings with (loc: mango, x: 2)")
ht.printResult(ht.findLocX("mango", 2))
print("")