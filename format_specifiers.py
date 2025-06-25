# Format Specifiers (value : flag)

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:.2f}")   # how many digits after decimal point 
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.3f}")

print(f"Price 1 is ${price1:10}")   # 10 spaces to contain the output
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

print(f"Price 1 is ${price1:010}")  # 0 padding and 10 spaces to contain the output
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

print(f"Price 1 is ${price1:<10}")   # left justifying 
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

print(f"Price 1 is ${price1:>10}")  # right justifying 
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

print(f"Price 1 is ${price1:^10}")  # Center Aligning
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

print(f"Price 1 is ${price1:+}")    # positive number will have positive sign and negative number will have negative sign
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3: }")

print(f"Price 1 is ${price1:,}")    # Thousand separator
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

print(f"Price 1 is ${price1:+,.2f}")    # flags mixing
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")






