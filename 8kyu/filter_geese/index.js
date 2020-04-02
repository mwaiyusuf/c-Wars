geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    // #your code here
    if(birds in geese):
        return True
    else:
        return False

filtered_geese = filter(geese, birds)

print('The filtered geese are:')
for geese in filtered_geese:
    print(geese)