#slicing = creating a substring by extracting elements from aonther string

#             indexing[] or slicing()
#    ***        [start:stop:step]           ***

#indexing

place = "pol kuvemppapa"
city = place[0:6]
area = place[7:19]
city = place[:6]
area = place[7:]
#step
punkcity = place[0:19:3]
punkcity = place[::3]
print(area)
print(city)
print(punkcity)

#***how to reverse a string in python using slicing***
reversed_place = place[::-1]
print(reversed_place)

#slice function part 2

website1 = "http://youtube.com"
website2 = "http;//twitch.com"
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])
