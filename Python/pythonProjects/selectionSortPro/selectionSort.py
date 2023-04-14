
# Swaps each elements in the array
def swapElements(list, pos1, pos2):
    num1 = list[pos1]
    num2 = list[pos2]
    list[pos1] = num2
    list[pos2] = num1
    return list

# Sorts the array from least to greatest using selection sort
def main():
    numbers = [12,6,15,8,5,56,1]
    min = 0 # Index of the current lowest number found
    for j in range(0, len(numbers), 1):
        for i in range(min, len(numbers), 1):
            if numbers[min] <= numbers[i]:
                continue
            else:
                min = i
        numbers = swapElements(numbers, j, min)
        min = j + 1
    print(numbers)

if __name__ == "__main__":
    main()