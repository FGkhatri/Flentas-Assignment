pattern=input("Enter the pattern:")
tstring=input("Enter the Text String:")
store= pattern in tstring #store true or false
if(store== False):
    tstring= tstring [::-1] #reverse the string
    print(pattern in tstring)#print true or falseafter reversed
else :
    print(store)#will print true if pattren recognised directly in tstring
