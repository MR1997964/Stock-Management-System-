current_stock = 25
reorder_threshold = 35

if current_stock > reorder_threshold:
    status = "stock level is sufficient no need to reorder."

elif current_stock == reorder_threshold:
    status = "Stock level is at threshold, consider reorder soon."

else:
    status = "Stock level is low, reorder immediately."
    
    
print(f"Current stock: {current_stock} units")
print(status)


