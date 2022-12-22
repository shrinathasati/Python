def remove_strip(string,word):
    newstring=string.replace(word,"")
    return newstring.strip()
string="  sanu is a good girl         "
newstring=remove_strip(string,"good")
print(newstring)