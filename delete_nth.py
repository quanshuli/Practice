def delete_nth(order,max_e):
    ans = []
    for o in order:
        if order.count(o) < max_e: ans.append(o)
    return ans
    
#
def delete_nth(order,max_e):
    # code here
    order_set = list(set(order))
    order_count = [order.count(i) for i in order_set]
    
    for i in range(len(order_count)):

        if order_count[i] > max_e:
            k = 0
            for j in range(len(order)):
                if order[j] == order_set[i]:
                    k += 1
                    if k > max_e:
                        order[j] = ''
                    
    order_new = []
    for i in range(len(order)):
        if order[i] != '':
            order_new.append(order[i])
            
    return order_new