#Name: Hash_Map.py
#Author: Harrison Reed
#Date: 10/30/2023
#Description: Program for EECS_330 lab 7, in which we implement a hash map, and test its functionality


class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size
    
    #Name: put
    #Description: Inserts key, value pair into hash_table based on the index given by hash_function
    def put(self, key, value):
        hashedval = self._hash_function(key)
        if((self.hash_table[hashedval].count(value) == 0)):#Check if value is already contained in the hash_table, if so then we don't need to add the value
            self.hash_table[hashedval].append(value)#if not contained insert into bucket at index     
        pass
    #Name: get
    #Description: Finds hash_value(index) based on given key, then returns bucket at that index
    def get(self, key) -> int: 
        hashedVal = self._hash_function(key)
        return self.hash_table[hashedVal]
        pass
    #Name: remove
    #Description removes an value stored using given key
    def remove(self, key, value):
        hashedVal = self._hash_function(key)#calculate index
        if(self.hash_table[hashedVal].count(value) > 0):#Check if item is contained in the bucket
            self.hash_table[hashedVal].remove(value)#if so remove it
        pass
    #Name:display
    #description: Prints out the given hash table
    def display(self):
        for i in range(len(self.hash_table)):
            print
            print("Bucket",i,self.hash_table[i])
    #Name: displayFlight
    #Description: Prints out the given passengers for a flight
    #Note: Differnet than display since our values are objects
    def displayFlight(self):
        for i in range(len(self.hash_table)):
            print("Bucket",i,"{", end="")
            for j in range(len(self.hash_table[i])):
                print(self.hash_table[i][j].getPassengers(), end=" , ")
            print("}")
            print(end="\n")
            
    #Name: max_passengers_in_flight
    #Description: Finds the maximum ammout of passengers for a given flight number
    def max_passengers_in_flight(self, flight_number)-> (str , int):
        tempList = self.get(flight_number)#Get the bucket associated with the flight number
        if(tempList[0].getId() == flight_number):#Handle in the case where there are collisions, this is to make sure there is the same flight, instead of other flights that might be stored in this bucket
            currTrip = tempList[0]
        else:#if first item is not the same flight, then create a place holder flight node
            currTrip = FlightNode(-1, "", -1)
        for i in range(len(tempList)):#go through list and find maximum ammount of passengers associated with the given flight
            if((currTrip.getPassengers() < tempList[i].getPassengers()) and tempList[i].getId() == flight_number):
                currTrip = tempList[i]
        return currTrip#return the Flight node with most passengers
        pass


class FlightNode:
    def __init__(self, flight_number, trip_id, passengers):
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers
    #getter functions to return information about flight node
    def getPassengers(self):
        return self.passengers
    
    def getFlight(self):
        return self.trip_id
    
    def getId(self):
        return self.flight_number


#Name: main
#Description: Driver method that allows us to test the functionality of our hash_map
if __name__ == '__main__':
    print("Part A _______________________________________________")
    my_hash_map = HashMap(7)
    my_hash_map.put("aaa", 0)
    my_hash_map.put("bbb", 1)
    my_hash_map.put("ccc", 4)
    my_hash_map.put("ddd", 9)
    my_hash_map.put("eee", 16)
    my_hash_map.put("fff", 25)
    my_hash_map.put("ggg", 36)
    my_hash_map.put("hhh", 49)
    my_hash_map.put("ccc", 64)
    my_hash_map.put("ccc", 81)
    my_hash_map.display()  

# Retrieve values
    print("Retrieve values:")
    print("aaa:", my_hash_map.get("aaa"))  
    print("bbb:", my_hash_map.get("bbb"))
    print("ccc:", my_hash_map.get("ccc"))

# Remove a key-value pair
    my_hash_map.remove("bbb", 1)  

# Display the updated hash map
    my_hash_map.display() 

    print("Part B____________________________________________")

#Max Passengers on Trip
    my_map = HashMap(5)
# Add flight nodes (flight_number, trip_id, passengers)
    my_map.put(16, FlightNode(16, "Trip 1", 300))
    my_map.put(16, FlightNode(16, "Trip 2", 700))
    my_map.put(29, FlightNode(29, "Trip 1", 800))
    my_map.put(29, FlightNode(29, "Trip 2", 250))
    my_map.put(29, FlightNode(29, "Trip 3", 500))
    my_map.put(36, FlightNode(36, "Trip 1", 500))
    my_map.put(36, FlightNode(36, "Trip 2", 340))
    my_map.put(36, FlightNode(36, "Trip 3", 900))
    my_map.put(36, FlightNode(36, "Trip 4", 400))
    my_map.put(49, FlightNode(49, "Trip 1", 250))
    my_map.put(49, FlightNode(49, "Trip 2", 550))

    my_map.displayFlight()

    max_passengers = my_map.max_passengers_in_flight(49)
    if max_passengers is not None:
        print("Largest number of people in flight ",max_passengers.getId() ,", is",max_passengers.getFlight(), "with", max_passengers.getPassengers(), "passengers")
    else:
        print("Flight not found in the map")
    pass