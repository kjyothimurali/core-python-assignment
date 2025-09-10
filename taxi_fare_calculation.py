#calculate fares
def fare_calculation(dist):
    fares=[]
    for i in dist:
        #add fares of each distance to fares list
        fares.append(50+i*10)

    return fares


trips=list(map(int,input("enter distances in km: ").split(",")))
fare=fare_calculation(trips)
#display each trip's fare
for i in range(len(trips)):
    print(f"Trip {i+1}: ${fare[i]}")

#display total fare of all trips
print(f"Total Fare: ${sum(fare)}")