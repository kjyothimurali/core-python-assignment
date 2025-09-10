def calculate(cart):
    total=0
    
    count=0
    if not cart:
        print("cart is empty")
        return 0
    else:
        for item in cart:
            #add values(price) of each item in cart
            total=total+int(cart[item])
            #counting items
            count+=1
        if count>5:
            price=total-(total*0.1)
        else:
            price=total
        return price
    

user_input=input("Enter items present in cart with their prices: ")

cart=dict(item.split(":") for item in user_input.split(","))
total_price=calculate(cart)
print(f"Total Price: {total_price}")
