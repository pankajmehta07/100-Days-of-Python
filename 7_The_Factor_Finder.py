

print("\n\t\tFactor Finder,\n\n")

run = True
while run:
    inp = input("\nEnter a number to factor (or 'QUIT' to quit):\t")
    if inp.lower()!="quit" and inp.isnumeric():
        num = int(inp)
        factors = [str(x) for x in range(1,num+1) if num%x==0]
        print(", ".join(factors))
    else:
        run=False

