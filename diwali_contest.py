def solve(n,p):
    contest_duration = 4*60

    travel_time = p
    remaining_time = contest_duration - travel_time

    time_per_problem = [5 * i for i in range(1,n+1)]

    count = 0

    for time in time_per_problem:
        if remaining_time >= time:
            print(time)
            remaining_time-=time
            count+=1
        else:
            break
    
    return count

n = 6 
p = 180
print(solve(n,p))