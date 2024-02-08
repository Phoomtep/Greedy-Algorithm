def createActivity(activity=[], command = "y"):
    while command == "y":
      start = int(input("Start activity: "))
      end = int(input("End activity: "))
      while start >= end:
          print("Try again")
          start = int(input("Start activity: "))
          end = int(input("End activity: "))
      activity.append([start,end])
      command = input("Do you want to add activity?\n(y/n)>>")
      while command != "y" and command != "n":
        command = input("Wrong command!!! Try again\n(y/n)>>")
    return activity

def sort_activity(activity):
    return activity[1]

def greedy(activity, rooms = []):
    activity.sort(key=sort_activity)
    while len(activity) > 0:
        room = []
        temp = []
        room.append(activity[0])
        latest_activity = activity[0][1]
        activity.pop(0)
        if len(activity) > 0:
            for i in range(len(activity)):
                if activity[i][0] >= latest_activity:
                    room.append(activity[i])
                    latest_activity = activity[i][1]
                    temp.append(i)
            
            j = 0
            while len(temp) > 0:
                activity.pop(temp[0] - j)
                temp.pop(0)
                j += 1

        rooms.append(room)
    
    return rooms

activity = createActivity()
print(activity)
print("Activities: %d"%len(activity))
rooms = greedy(activity)
print("rooms: %d"%len(rooms))
for i in range(len(rooms)):
    print("Room%d: "%(i+1),end="")
    print(rooms[i])
