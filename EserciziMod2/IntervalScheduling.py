def IS(intervals:list)->list:

    # sorting the intervals
    intervals.sort(key=lambda x: x[2])

    # print(intervals)
    # counting the events
    count = 0
    # keeping track of ending of intervals
    end = 0
    # list of the intervals in which person will attend the events
    answer = []

    # traversing the list of intervals
    for interval in intervals:
        # starting time of next interval will >= ending
        # time of previous interval
        if end <= interval[1]:
            # update the and
            end = interval[2]
            # increment the count by one
            count += 1
            # insert the non-conflict interval in the list
            answer.append(interval)
    return answer

intervals = [("B",1,4), ("C",3,5), ("A",0,6), ("E",4,7), ("D",3,8), ("F",5,9), ("G",6,10), ("H",8,11)]

answer = IS(intervals)
print(f"Scheduled intervals : {answer}")
