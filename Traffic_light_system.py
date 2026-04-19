light=input("Enter the color of light : ")

def traffic(light):
    if light == 'green':
        print("Go ......")
    elif light == 'red':
        print("stop .....")
    elif light == 'yellow':
        print("start the engine ...")
    else:
        print("invlaid input")
traffic(light)