# Shipping Label 

def shipping_label(*args, **kwargs):
    for arg in args:
      print(arg, end=" ")  
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get("street")}")
        print(f"{kwargs.get("pobox")}")
    else:
        print(f"{kwargs.get("street")}")
        
    print(f"{kwargs.get("city")} {kwargs.get("state")} {kwargs.get("zip")}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 fake st.",
               apt="#200", 
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")








