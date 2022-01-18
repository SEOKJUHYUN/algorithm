def BubbleSort(data) :
    len_data: int = len(data)
    swap_bool: bool = False

    for i in range(len_data - 1) :
        for j in range(len_data - i - 1) :
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
                swap_bool = True

        if swap_bool is False :
            break

    return data

if __name__ == "__main__" :
    import random
    data_list = random.sample(range(100), 50)
    print(BubbleSort(data_list))
