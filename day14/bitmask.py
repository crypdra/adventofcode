import re
import sys
mem = {}
mem_part_two = {}
bits = 36
from copy import deepcopy
def convert_to_bit(value):
    code = [0]*bits
    summe = 0
    for i in range(bits):
        if(2**(bits-i-1) + summe) <= value:
            code[i] = 1
            summe += 2**(bits-i-1)
    return code

def convert_to_decimal(array):
    value = 0
    for i in range(len(array)):
        value += array[i]*2**(bits-i-1)
    return value

def mask_bits(mask, orig_array, mask_memory=False):
    orig_array = deepcopy(orig_array)
    if mask_memory:
        arrays = []
        for key, bit in enumerate(mask):
            if bit == "X":
                for x, array in enumerate(deepcopy(arrays)):
                    arrays.append(array + [0])
                    arrays[x].append(1)
                if len(arrays) == 0:
                    arrays.append([0])
                    arrays.append([1])
            elif bit == "0":
                for x, array in enumerate(arrays):
                    arrays[x].append(orig_array[key])
                if len(arrays) == 0:
                    arrays.append([orig_array[key]])
            else:
                for x, array in enumerate(arrays):
                    arrays[x].append(int(bit))
                if len(arrays) == 0:
                    arrays.append([int(bit)])
        return arrays
    else:    
        for key, bit in enumerate(mask):
            if bit != "X":
                orig_array[key] = int(bit)
        return orig_array


if __name__ == "__main__":
    with open("program", "r") as f:
        mask = 0
        for line in f.readlines():
            line = line.strip()
            maskmatch = re.search("mask = (\w+)", line)
            if maskmatch:
                mask = maskmatch.groups()[0]
            else:
                read = re.search("mem\\[(\d+)\\] = (\d+)", line)
                if read:
                    address, value = read.groups()
                    address = int(address)
                    value = int(value)
                else:
                    print(line)
                    sys.exit(1)
                mem[address] = mask_bits(mask, convert_to_bit(value))
                addresses = mask_bits(mask, convert_to_bit(address), True)
                for convaddress in addresses:
                    mem_part_two[convert_to_decimal(convaddress)] = convert_to_bit(value)
    summe = 0
    summe2 = 0
    for key in mem:
        summe += convert_to_decimal(mem[key])
    for key in mem_part_two:
        summe2 += convert_to_decimal(mem_part_two[key])
    print(summe)
    print(summe2)