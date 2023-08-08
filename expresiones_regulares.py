#Expresiones regulares 
import re


"""
regex = r"(y|Y)o"
findall = re.findall(regex, "Yo vivo en Quito")
print(findall)
"""

#Longitud fija.{5,8}
"""
regex = r"((M|m)+) .{5,9} ((M|m)+)"
findall = re.search(regex, "mmmmMMMM cualquier MmmM")
print(findall)
"""

#Longitud entre letras y numeros
#parte central, puede ser letra o numero entre 5 y 9 caracteres
"""
regex = r"((M|m)+) [a-z0-9]{5,9} ((M|m)+)"
findall = re.search(regex, "mmmmMMMM cualq2345 MmmM")
print(findall)
"""
"""
#Validador de URL
regex = r"(https://|http://)\w{3,}"
findall = re.search(regex, "https://moure.dev")
print(findall)
"""

#Validador de URL
regex = r"((https?://(www\.)?)|www\.)\w{3,}\.[a-z]{2,3}"
findall = re.search(regex, "https://moure.dev")
print(findall)