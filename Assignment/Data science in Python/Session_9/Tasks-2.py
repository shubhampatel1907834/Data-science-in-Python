def get_delivery_charge(amount, city='Ahmedabad'):
    if city == 'Ahmedabad':
        return 0
    else:
        return 50

# Examples
print(get_delivery_charge(500))              # Output: 0
print(get_delivery_charge(500, 'Mumbai'))    # Output: 50
    
