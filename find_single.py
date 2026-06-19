def find_single(lst):
    result = 0
    for num in lst:
        result ^= num
    return result
def test_libraries_installed():
    import numpy
    import pandas
    import matplotlib
    import seaborn

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 3, 1, 2]
    print(f"Input: {my_list}")
    print(f"Single element: {find_single(my_list)}")
