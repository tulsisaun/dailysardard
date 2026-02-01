#[Naive Approach] By Sorting the array - O(n log n) Time and O(1) Space
#The idea is to firstly sort the array in ascending order.
##Once the array is sorted, the first element of the array will be the minimum element and the last element of the array will be the maximum element.

#Number of Comparisons
#The number of comparisons is equal to the number of comparisons made during the sorting process. For any comparison-based sorting algorithm, the minimum number of comparisons required in the worst case to sort an array of n elements is O(n log n). Hence, the number of comparisons made in this approach is O(n log n).

def findMinMax(arr):
    
    # Sort array
    sorted_arr = sorted(arr)
    return [sorted_arr[0], sorted_arr[-1]] 

if __name__ == "__main__":
    arr = [3, 5, 4, 1, 9]
    result = findMinMax(arr)
    print("%d %d" % (result[0], result[1]))