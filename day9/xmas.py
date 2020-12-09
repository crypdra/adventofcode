def find_set(numbers, target):
    for key, number in enumerate(numbers):
        summe = number
        pointer = 0
        while(summe < target):
            pointer += 1
            if(key+pointer < len(numbers)):
                summe += numbers[key+pointer]
            else:
                break
        if summe == target:
            return min(numbers[key:key+pointer+1])+max(numbers[key:key+pointer+1])

with open("numbers", "r") as f:
    
    preamble_length = 25
    numbers = [int(item.strip()) for item in f.readlines()]
    pointer = preamble_length
    
    for pointer in range(preamble_length, len(numbers)):
        current_number = numbers[pointer]
        found = False
        for x in numbers[pointer-preamble_length: pointer]:
            for y in numbers[pointer-preamble_length: pointer]:
                if x != y and x + y == current_number:
                    found = True
        if not found:
            print(current_number)
            print(find_set(numbers[0:pointer], current_number))
            break

