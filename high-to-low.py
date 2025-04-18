pin = "123556"
if(len(pin) != 4 and len(pin) != 6):
    print(False)
elif (pin.isdigit()):
    print(True)
else:
    print(False)
    
# better answer
print(len(pin) in (4, 6) and pin.isdigit())
    