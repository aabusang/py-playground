
numbers = []
def copy_sort(array):
    copy = array[:]
    sorted_copy = []
    #algo seqs here
    while len(copy) > 0:
        min = 0
        for element in range(0, len(copy)):
            if copy[element] < copy[min]:
                min = element
        print("\tRemoving value", copy[minimum], "from", copy)
        sorted_copy.append(copy.pop(minimum))
    array = [5,3,1,2,6,4]
    print("Copy sorted...\nArray:", array)
    print("Copy:", copy_sobrted(array))
    print("Array:", array)

    return sorted_copy

        
