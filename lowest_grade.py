class sort_stu():
    # this is method is to add zero in all the empty indexes
    def add_zero(array):
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == "":
                    array[i][j] = 0
        return array

    # to sort from lowest to highest
    def lowest_highest(array, num):
        array.sort(key=lambda x: x[num])
        return array
