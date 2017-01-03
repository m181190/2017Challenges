#Program used to identify the only element without a pair from a given list

#list used as an example 
mylist = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7,8,8,8,20,22,22,92] 

#this is a tuple list in the form [x,y] where x = one of the numbers from the list and y = the number of times it appears
occur_index = [[x, mylist.count(x)] for x in set(mylist)]

#converting the tuple in a simple list
single_tuple = [(x,y) for (x,y) in occur_index if y == 1]

#removing the y-index of the tuple 
simple_list = [i[0] for i in single_tuple]

print str(simple_list)[1:-1]