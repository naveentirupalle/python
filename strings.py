'''
type of strings 
upper
lower
startswith 
endswith
replace(old,new)
split
count
rstrip
Lstrip
strip
remove prefix
remove sufix
index 
find

'''

# upper() &lower()
'''
pythonlife="nainu python nairchukuntuna"
print(pythonlife.upper())         #  NAINU PYTHON NAIRCHUKUNTUNA



pythonlife=" NAINU PYTHON NAIRCHUKUNTUNA"
print(pythonlife.lower())         #nainu python nairchukuntuna


'''
#endswith
'''
pythonlife=" NAINU PYTHON NAIRCHUKUNTUNA"
print(pythonlife.endswith('A') )   #true

#startswith 

pythonlife=" NAINU PYTHON NAIRCHUKUNTUNA"
print(pythonlife.startswith('A') )    #false 

'''

#replace

'''
pythonlife=" python language"
print(pythonlife.replace('python','java') )  # java language


pythonlife=" python language"
print(pythonlife.replace('language','programming') )   # python programming
 
'''
#split
'''
pythonlife="adudam anadhra"
print(pythonlife.split())    #split it converts string into list

'''
#count

'''
pythonlife="fighter movie"
print(pythonlife.count('i'))  # 2 it counts n.o  i in string


pythonlife="fighter movie"
print(pythonlife.count('m'))   # 1

'''

#strip, rstrip, lstrip

'''
pythonlife="    fighter movie     "
print(pythonlife.strip()) 
print(pythonlife.strip('fighter')) 
print(len(pythonlife))           
print(pythonlife.rstrip())
print(len(pythonlife))
print(pythonlife.lstrip())

'''
# remove prefix ,remove sufix
'''
pythonlife="fighter movie"
print(pythonlife.removeprefix('fighter')) 
print(pythonlife.removesuffix('movie'))

'''

# index, find 
'''
pythonlife="fighter movie"
print(pythonlife.index('fighter')) # returns 0


pythonlife="fighter movie"
print(pythonlife.index('fighter'))  # returns 0
print(pythonlife.find('naveen'))   #returns -1
print(pythonlife.find('movie'))


pythonlife="fighter movie"
print(pythonlife.find('naveen'))   #returns -1

'''
