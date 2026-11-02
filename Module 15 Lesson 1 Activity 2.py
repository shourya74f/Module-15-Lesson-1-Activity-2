input("Double loop at n=4 took 10 steps, Press enter to run.")
for n in [10, 100, 1000]:
    input("n= "+str(n)+", Press enter to run.")
    print("Total Steps: ", n*(n+1)//2)