#lists mutable, expandable, sortable
a=[]
print(type(a),a)
a=[1,2,3,4,5]
type(a)
print(a)
a=[1,2,3,4,5,'python',True,print,[1,2,3],4.5]
print(a,a[5])
print(len(a))
print(a[-len(a)]) #negative indexing
print(a[2:8])
print(a[:6])
print(a[:3])
print(a[:])
print(a[1:8:2]) #slicing with step
print(a[-6:-5:1])
print(a[-2:-8:-1])
print(a[1:-2])
#program to reverse a list in python
b=[2,4,6,8,10]
print(b)
print(b[::-1])
#adding to lists
b.append(12)
print(b)
print([23,45,67]+b)
#2D arrays
c=[[1,2,3],[4,5,6],[7,8,9]]
print(c)
print(c[0][1]) #accessing elements in 2D array
##ticktactoe game using 2D arrays
board=[[""]*3]*3
print(board)
board[1][1]="X"
print(board) #this is a common mistake when creating 2D arrays using list multiplication. It creates references to the same inner list, so modifying one element modifies all rows. To avoid this, we can use a list comprehension to create independent inner lists.

g=[9,8,7,6,5,4,3,2,1]
print(g)
g[0]=1000
print(g)
g.append(7)
print(g)
g.append([1,2,3])
print(g)
g.extend([4,5,6])
print(g)
g.pop() #removes the last element
print(g)
g.pop(5) #removes the element at index 5
print(g)
g.remove(7) #removes the first occurrence of 7
print(g)

a=[10,20,30,40,50]
enumerated_a=enumerate(a)
list(enumerated_a) #[(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]
#linear search
def linear_search(arr,target):
    for index,value in enumerate(arr):
        if value==target:
            return index
    return -1
print(linear_search(a,30)) #2
print(linear_search(a,50))#4

#tuples = immutable lists
a1=()
print(type(a1),a1)
a=(1,2,3,4,5)
type(a)
print(a,id(a))
a=(1,2,3,4,5)
print(a,id(a))
#no append function
a=(1,2,3)
x,y,z = a #unpacking a tuple
print(x,y,z)#1 2 3
# python needs same number of variables on the left side of the assignment 
# operator as the number of elements in the tuple on the right side.
# If there are more variables than elements, it will raise a ValueError.
# If there are fewer variables than elements, it will also raise a ValueError.
# To avoid this, we can use the * operator to unpack the remaining elements
# into a list.
def foo():
    return 1,2,3
bar = foo()
print(bar,type(bar)) #(1, 2, 3)
a,b,c = foo() #ValueError: too many values to unpack (expected 3)
print(a,b,c) #1 2 3
#legacway to swap two tupples
a=30
b=40
print(a,b) #30 40
a,b=b,a #swapping two variables using tuple unpacking
print(a,b) #40 30

#sets = unordered collection of unique elements
s=set()
print(type(s),s)

#Dictionaries => are non ordered, mutable,
# key-value pairs and are indexeble using keys
# they are iterable and can be nested
# they are implemented as hash tables and are optimized for fast lookups
# keys are immutable and must be unique, while values can be of any data type and can be duplicated
d = {}
print(type(d),d)
a={
    "name":"Alice",
    "age":30,
    "city":"New York"
}
print(a)
print(a["name"]) #Alice
print(a.get("age")) #30
print(a.get("country","Not Found")) #Not Found
print(a.keys()) #dict_keys(['name', 'age', 'city'])
print(a.values()) #dict_values(['Alice', 30, 'New York'])
print(a.items()) #dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
a["age"]=21 #updating a value
print(a) #{'name': 'Alice', 'age': 21, 'city': 'New York'}

avenger = {"name" : "thor",
    "age" :1500,
    "weapon" : "mjolnir",
    "power" : "thunder",
    "nickname" : "God of thunder",
    "strongest" : False
}
print(avenger)
avenger.update({"strongest":"true",
                "nick_name":"God Killer",
                "jane_dead":True}) #updating a value using update method
print(avenger)
for i in avenger:
    print(i) #prints keys
for i in avenger.keys():
    print(i) #prints keys
for key,value in avenger.items():
    print(key,"->",value) #prints key and value

#enumeration in dictionaries
    rando=enumerate(avenger)
    print(rando)
    print(list(rando)) #[(0, 'name'), (1, 'age'), (2, 'weapon'), (3, 'power'), (4, 'nickname'), (5, 'strongest')]
#keys are immutable and values are mutable
d1={
    "key1":123,
    (1,2,3):"value2",
    45:"value3",
    True:[1,2,3],
    5.6:{
        "random":"value4"
    }
}

new_dict = {
    1: "x",
    2: "y",
    3: "z"
}
print(new_dict)
random = new_dict.get(7,"Not Found") #returns "Not Found" if key is not found
print(random) #Not Found

d={}
d[1.1]="B"
d[1]="C"
d[True]="D"
d[1+0j]="E"
print(d) #{1.1: 'B', 1: 'D', 1j: 'E'} 
#mathamatical value or 1,1.+0j and True are all considered as 1 in python,
#so the last assignment will overwrite the previous ones.
#Hence we get {1.1: 'B', 1: 'D', 1j: 'E'} as the final dictionary.
A={1,2,3,4,5}
B={4,5,6,7,8}
N={0,1,2,3,4,5,6,7,8,9}
print(A.union(B)) #{1, 2, 3, 4, 5, 6, 7, 8}
print(A|B) #{1, 2, 3, 4, 5, 6, 7, 8}
print(A.intersection(B)) #{4, 5}
print(A&B) #{4, 5}
print(A.difference(B)) #{1, 2, 3}
print(A-B) #{1, 2, 3}
print(A.symmetric_difference(B)) #{1, 2, 3, 6, 7, 8}
print(A^B) #{1, 2, 3, 6, 7, 8}
print(A.issubset(B)) #False
print(B.issubset(A)) #False
print(A.issuperset(B)) #False
print(A.isdisjoint(B)) #False
print(A.issubset(N)) #True
print(B.issubset(N)) #True
print(A.issuperset(N)) #False
print(B.issuperset(N)) #False
print(N.issuperset(A)) #True
print(N.issuperset(B)) #True
print(len(N)) #10

a=[1,1,2,3,4,67,6.89,6.89,"python","python",True,True]
print(set(a)) #{1, 2, 3, 4, 67, 6.89, 'python', True}
print(type(A)) #<class 'set'>
set(a)
print(a,type(a)) #[1, 1, 2, 3, 4, 67, 6.89, 6.89, 'python', 'python', True, True] <class 'list'>

