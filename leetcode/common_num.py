num_list = [1,2,2,2,3]

def common_num(num_list):
    new_list = list(set(num_list))
    freq_list = []
    freq_list


    for i in new_list:
        freq_list.append(num_list.count(i))
    return freq_list.index(max(freq_list))
        
common_num(num_list)
