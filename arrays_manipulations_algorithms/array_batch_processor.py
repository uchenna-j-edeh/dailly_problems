

def batch_processor(my_list):
    stepper = 10
    counter = 0
    my_length = len(my_list)
    max_num = my_list[0]
    while(counter < my_length):
        
        if my_length - counter - stepper > 0:
            current_batch = my_list[ counter: counter + stepper ]
        else:
            current_batch = my_list[ counter: ]
        
        print(current_batch)
        counter += stepper

        for num in current_batch:
            if num > max_num:
                max_num = num

    return max_num


print(batch_processor([i for i in range(23)]))

