#adding to menu
def addItem(add_item,menu):
    menu.append(add_item)
    return menu

#removing item from menu
def removeItem(remove_item,menu):
    if remove_item in menu:
        menu.remove(remove_item)
    else:
        print("no such item in menu")
    return menu

#checking availability of item in menu
def checkItem(check_item,menu):
    if check_item in menu:
        return True
    else:
        return False



menu=input("enter menu items: ").split(",")
add_item=input("enter item to add: ")
addItem(add_item,menu)
remove_item=input("enter item to remove: ")
removeItem(remove_item,menu)
check_item=input("ente item to check in menu: ")
if(checkItem(check_item,menu)):
    print(f"Availability: {check_item} is available")
else:
    print(f"Availability: {check_item} is not available")
print(f"Updated menu: {menu}")