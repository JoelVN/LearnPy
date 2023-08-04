#Expresiones regulares 
import re

"""
regex = r"(y|Y)o"
findall = re.findall(regex, "Yo vivo en Quito")
print(findall)
"""

regex = r"((M|m)+) .{5,9} ((M|m)+)"
findall = re.search(regex, "mmmmMMMM cualquier MmmM")
print(findall)