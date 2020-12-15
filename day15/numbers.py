with open("start", "r") as f:
    numbers = [int(number) for number in f.readline().strip().split(",")]
    history = {}
    queue = []
    for i in range(30000000):
        if i < len(numbers):
            queue.append(numbers[i])
            if i > 0:
                history[numbers[i-1]] = i-1
        elif queue[-1] in history:
            history[queue[-1]] == 0

            queue.append(i-1-history[queue[-1]])
            history[queue[-2]] = i-1
        elif queue[-1] not in history:
            queue.append(0)
            history[queue[-2]] = i-1
        print(queue[-1])

            