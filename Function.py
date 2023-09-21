start = input("Starting from ____")
end = input("Going to ____")
transport = input("I am taking a _____ to get there")
time = input("Based on this data I will get there in _____ hours")

def trip_plan(start, end, time, transport = 'car'):
    print(f"It  looks like your starting trip from {start}")
    print(f"Your are planning to go to {end}")
    print(f"You are going by {transport}")
    print(f"This trip will take around {time} hours")

trip_plan()

