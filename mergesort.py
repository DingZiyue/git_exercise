import matplotlib.pyplot as plt


def merge_sort(ls):
    """
    Sorts a list in ascending order using the merge sort algorithm.
    The sorting is done in-place.
    """
    if len(ls) > 1:
        mid = len(ls) // 2
        left = ls[:mid]
        right = ls[mid:]

        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        i = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                ls[i] = left[left_idx]
                left_idx += 1
            else:
                ls[i] = right[right_idx]
                right_idx += 1
            i += 1

        while left_idx < len(left):
            ls[i] = left[left_idx]
            left_idx += 1
            i += 1

        while right_idx < len(right):
            ls[i] = right[right_idx]
            right_idx += 1
            i += 1


if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plt.plot(range(len(my_list)), my_list)
    plt.title("Before Sorting")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

    merge_sort(my_list)

    plt.plot(range(len(my_list)), my_list)
    plt.title("After Sorting")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()
