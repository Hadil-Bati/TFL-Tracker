import pandas as pd
import math
from DoublyLinkedList import *
from datetime import datetime, timedelta

file = pd.read_excel(r'tube.xlsx', usecols='A,B,C,D')
# Using pandas to read through the excel file.
seen_stations = []
trains_timetable, bakerloo_timetable = [],[]
[trains_timetable.append(i*5) for i in range(0,13)]
[bakerloo_timetable.append(i*2.5) for i in range(0,25)]
# Since trains run every 5 minutes, we created a tuple containing multiples of 5, so it would be easy to figure out
# how long it would take for the next train to arrive. The variable next_train includes a function that finds the
# first greater value in that list than the current minutes, so by subtracting them we obtain the waiting time for
# the next train. arrival_time will be the sum of time_of_travel, which is the time the user inputs in the GUI,
# the time spent waiting on the platform(s) waiting for the train(s), and the time spent travelling.
class tube:
    def get_lines():
        DLL = DoublyLinkedList()
        for index, row in file.iterrows():
            if pd.isnull(file.iloc[index][2]):
                DLL.append(file.iloc[index][1], file.iloc[index][0])
            if DLL.tail:
                if DLL.tail not in seen_stations:
                    seen_stations.append(DLL.tail)
        return DLL

    # The function 'get_lines' will go through the excel file row by row and will check if the third column is empty;
    # if it is it means that it's going through the parts of the excel sheet where it just lists the stations in the
    # differente lines, and hence it will store them in a double linked list. This function will also save every
    # single station in the list 'seen_station', which will be used by the dijstra's algorithm.

    def link_same_line(DLL):
        for index, row in file.iterrows():
            if not pd.isnull(file.iloc[index][2]):
                temp = DLL.search(file.iloc[index][1], file.iloc[index][0])
                temp2 = DLL.search(file.iloc[index][2], file.iloc[index][0])
                temp.links[temp2] = math.trunc(file.iloc[index][3])
                temp2.links[temp] = math.trunc(file.iloc[index][3])

    # The function link_same_line will go through the excel file again, and this time will check that the third
    # column is NOT empty if the condition is true it means that it's going through the bit where the excel sheet
    # lists the path from one end of the line to the other end, and it will store that in the attribute 'links' of
    # the Nodes corrisponding to those stations.

    def link_all_stations(DLL, seen_stations):
        cur = DLL.head
        while cur:
            for i in seen_stations:
                if cur.line != i.line and i.data == cur.data:
                    cur.links[i] = 3
                    i.links[cur] = 3
            cur = cur.next


# The function 'link_all_stations' will read through the whole doubly linked list and the list 'seen_stations',
# and will compare each station in the DLL with every element in the list 'seen_station', and if their name is the
# same but their line is different it means that the same stations has got two lines which go through it and hence
# you can change lines at that station. If a change is found, it will be appended to the attribute 'links' of both
# nodes, with a cost of 3, which is the amount of time we assumed it takes to walk from one platform to another.

def get_unseen_nodes():
    unseenNodes = []
    temp = underground.head
    while temp:
        unseenNodes.append(temp)
        temp = temp.next
    return unseenNodes

# This function will create and return a list called 'unseenNodes' that contains every node of the DLL
# and it will be used by Dijkstra's algorithm.
def checkBakerloo(time_of_travel):
    if 9 <= int(time_of_travel.strftime('%H')) <= 15 or 19 <= int(time_of_travel.strftime('%H')) <= 23:
        return True
    else:
        return False

def dijkstra(start, end, starting_time):
    shortest_distance = {}
    previous_node = {}
    infinity = 10000
    # Infinity is set to 10.000, as it's a number considerably larger than the distance between stations.
    track_path = []
    unseenNodes = get_unseen_nodes()
    if start.line == 'Bakerloo' and checkBakerloo(starting_time):
        time_of_travel = next_train(starting_time,bakerloo_timetable)[0]
    else:
        time_of_travel = next_train(starting_time)[0]
    # The time of travel gets updated here to when the train leaves the station. This was done for two reasons:
    # 1- If it doesn't get updated the program might mistakenly allow travels that go past the closing times of the
    # underground. 2- The program would misjudge the current time and it would think that the Bakerloo line is
    # operating at twice the normal speed outside the designed time slots. e.g. if the user inputs 15.56, the program
    # will think that those 4 minutes before 4 o'clock will count as time travelling on a train, when in fact those
    # minutes will be spent on the platform waiting for the train to arrive. By updating the time with the function
    # 'next_train', we make sure that this does not happen and the output will be more precise.

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    # Setting the distance of every node to infinity except for the starting node.
    count = 0
    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        # While there still are unseen nodes, the program will keep on exploring every possible path to find the
        # quickest one.
        path_options = min_distance_node.links
        for child_node, cost in path_options.items():
            if cost + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = path_options[child_node] + shortest_distance[min_distance_node]
                previous_node[child_node] = min_distance_node
        unseenNodes.remove(min_distance_node)
    # The node that was just checked gets removed from unseenNodes, in order to progress with the loop and avoid
    # an infinite loop.
    currentNode = end
    while currentNode != start:
        track_path.insert(0, currentNode)
        currentNode = previous_node[currentNode]
    # Going through the found path from end to start. If the route found leads from end to start it means the path is
    # valid.
    if start.data != track_path[0].data:
        track_path.insert(0, start)
    # These two lines will make sure that the first element in the list is the starting station.
    if shortest_distance[end] != infinity:
        times = []
        changes = 0
        for i in range(len(track_path)):
            try:
                if track_path[i].data == track_path[i + 1].data and track_path[i].line != track_path[i + 1].line:
                    if track_path[i+1].line == 'Bakerloo' and checkBakerloo(time_of_travel):
                        changes += 1
                        time_of_travel += timedelta(minutes=4)
                        times.append(4 + next_train(time_of_travel,bakerloo_timetable)[1])
                        time_of_travel += timedelta(minutes=times[-1] - 4)
                    else:
                        changes += 1
                        times.append(4)
                        time_of_travel += timedelta(minutes=4)
                        times[-1] += (next_train(time_of_travel)[1])
                        time_of_travel += timedelta(minutes=times[-1] - 4)
                        continue
                elif track_path[i+1].line == 'Bakerloo' and checkBakerloo(time_of_travel):
                    times.append((track_path[i + 1].links[track_path[i]] + 1) / 2)
                    time_of_travel += timedelta(minutes=times[-1])
                else:
                    times.append(track_path[i + 1].links[track_path[i]] + 1)
                    time_of_travel += timedelta(minutes=times[-1])
            except IndexError:
                pass
        # This for loop will save the number of changes and the minutes it takes to travel from each station to the
        # next one and it will store the values in the list 'times' and the variable 'changes' If there is a change
        # the program will append '4' to the list 'times', as we assumed it will take 3 minutes for the passenger to
        # change lines, and 1 extra minute to wait for the train to let passenger (dis)embark. The program will also
        # check what time it is and calculate when the next train will get to the platform and aditionally it will
        # check if the user is traveling on the bakerloo line within the time slots where trains go faster. If that
        # is the case it means that waiting times are halved. If there is no change and the passenger is just
        # traveling on a single line, the program will add to the list 'times' the time it takes to get from station
        # A to station B plus 1 extra minute of waiting for letting passengers (dis)embark, and will still calculate
        # if it is the case to half the travel time for the bakerloo line.

    if track_path[-1].data == track_path[-2].data:
        track_path.pop(-1)
        times.pop(-1)
        changes -= 1
    # If for some reason the program changes to another line at the final station, it will just check
    # if the last two stations have the same name, and if they do it will just delete the last change.
    return track_path, changes, times

def next_train(time_of_travel, timetable = trains_timetable):
    next_train = next(i for i, minute in enumerate(timetable) if minute >= int(time_of_travel.strftime('%M')))
    time_to_next_train = (timetable[next_train] - int(time_of_travel.strftime('%M')))
    time_of_travel += timedelta(minutes=time_to_next_train)
    return time_of_travel, time_to_next_train
# The function next_train is used to get the time to the next train and also to get what time it will be when the
# next train arrives. We decided to create a function that does this because we needed to do this operation in
# different occasions: When changing lines the user has to wait for another train, so knowing how long the wait would
# be is useful for a more precise result. We also needed this for the first station. When the user enters the station
# we assumed the train will never already be there; therefore calculating the wait is needed.

underground = tube.get_lines()
tube.link_same_line(underground)
tube.link_all_stations(underground, seen_stations)
# We decided to create the DLL before the main function as this will make the program run more smoothly due to the
# fact that the DLL will be created when the file is imported in the GUI rather than when the user hits the 'find
# lpath' button. This will prevent the GUI from stuttering.

def main(start=None, end=None, time_of_travel=None):
    start, end = underground.search_without_line(start), underground.search_without_line(end)
    # The previous line will take the inputs from the users, which are two strings representing the two stations,
    # and it will search for two nodes with the same name in the DLL using the function 'search_without_line'.

    if time_of_travel:
        temp = (time_of_travel.split(':'))
        temp[0], temp[1] = int(temp[0]), int(temp[1])
        time_of_travel = datetime.now()
        time_of_travel = (time_of_travel.replace(hour=temp[0], minute=temp[1]))

    # This bit of code will take the time from the user input and do some string manipulation in order to get two
    # integers representing the time, so they are compatible with the datetime objects.

    if not start or not end:
        return ("Check the name of the stations (start/end). They might be spelled incorrectly.")
    if 0 <= int(time_of_travel.strftime('%H')) < 5:
        return 'Trains run from 5:00 to 00:00.'
    elif start == end:
        return ("You are already there!")
    else:
        output = list(dijkstra(start, end, time_of_travel))
        if sum(output[2]) + int(time_of_travel.strftime('%M')) > 59 and int(time_of_travel.strftime('%H')) == 23:
            return ("There is not enough time to travel to your destination before the"
                    "underground closes.\nTrains run from 5:00 to 00:00.")
        else:
            if start.line == 'Bakerloo' and checkBakerloo(time_of_travel):
                time_to_next_train = next_train(time_of_travel, bakerloo_timetable)[1]
            else:
                time_to_next_train = next_train(time_of_travel)[1]
            #If the user is travelling on the barkerloo line in the designated time slots, trains will run every
            #2.5 minutes instead of 5, making the waiting time shorter.

            arrival_time = time_of_travel + timedelta(minutes=time_to_next_train) + timedelta(minutes=sum(output[2]))
            output.append(arrival_time)
            output.append(time_to_next_train)
            return output

# The function 'main' will check if the travel time is between midnight and 5am, and if it is it will return an error
# message as train don't run during that time slot. If one of the two stations is None, it will return an error. If
# station A is the same station as station B, the program will not run as the user is already in that station.
# Finally, if none of those conditions are true, the program will check if the time to travel to the destination will
# not go past the time of operation of the Underground. If it does, it will return that there is not enough time to
# go to station B before the underground closes, otherwise it will return the shortest path between two stations,
# and the time of arrival which will be calculated by adding to the starting time the time spent waiting for the
# train and the time spent travelling.

