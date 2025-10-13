def delivery_fee(dist, rate) :
    fee = dist*rate
    return fee
    
dist = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))
print(f"Total Delivery Fee: ₱{delivery_fee(dist, rate):.2f}")