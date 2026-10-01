dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])


dimensions[0]=250
print(dimensions)          #tuples are immutable

for dimension in dimensions:
    print(dimension)
    
new_dimensions = (200,50)
print("original dimensions: ")
for dimension in new_dimensions:
    print(new_dimensions)
    
new_dimensions = (40,100)
print("Modified dimensions: ")
for dimension in new_dimensions:
    print(new_dimensions)        #you can modify whole of the elements in the tuple


