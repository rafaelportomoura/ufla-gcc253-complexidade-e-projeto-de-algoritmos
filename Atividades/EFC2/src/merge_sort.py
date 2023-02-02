def merge(array, begin, half, end):
    i = begin
    j = half + 1
    aux = begin
    list_len = end - begin + 1
    aux_array = [0] * len(array)

    while i <= half and j <= end:
        if array[i] <= array[j]:
            aux_array[aux] = array[i]
            i += 1
        else:
            aux_array[aux] = array[j]
            j += 1
        aux += 1

    while i <= half:
        aux_array[aux] = array[i]
        i += 1
        aux += 1

    while j <= end:
        aux_array[aux] = array[j]
        j += 1
        aux += 1
        
    for aux in range(0,list_len):
        array[end] = aux_array[end]
        end -= 1

def mergeSort(array, begin, end):
    if begin < end:
        half = int((begin + end) / 2)
        mergeSort(array, begin, half)
        mergeSort(array, half + 1, end)
        merge(array, begin, half, end)
    return array
