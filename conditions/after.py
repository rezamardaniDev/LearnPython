def total_price(auth:bool, item_price: int, item_count: int) -> int | str:
    if not auth:
        return "Auth error"
    
    if item_price <= 0:
        return "price must bigger than 0"
    
    if item_count <= 0:
        return "Count Error"
    
    return item_price * item_count


item_price = 25
item_count = -3
auth = True
total = total_price(auth, item_price, item_count)

print(f"Total price: ${total}") if isinstance(total, int) else print(f"Error: {total}")
