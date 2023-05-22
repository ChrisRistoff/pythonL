def round_robin(jobs, time_slice, index):

    queue = list(jobs)
    total_time = 0

    while queue[index] > 0:
        current_job = queue.pop(0)
        run_time = min(current_job, time_slice)
        current_job -= run_time
        total_time += run_time

        queue.append(current_job)

        if index == 0:
            index = len(queue) - 1
        else:
            index -= 1

    return total_time


print(round_robin([10, 20, 1], 5, 0))  # 22
print(round_robin([10, 20, 1], 5, 1))  # 23
print(round_robin([10, 20, 1], 5, 2))  # 11
print(round_robin([10, 20, 1, 5, 32, 24], 5, 4))  # 92
