'''
[5] You have an unordered array X of n integers. Find the array M containing n elements where M_i is the product of all integers in X except for X_i.
You may not use division. You can use extra memory.
(Hint: there are solutions faster than O(n^2).)
'''
'''

e.g. 
input =     [4 3 2 1 3 2]
output =    []

pre >>>>>
post <<<<<<

index:
0th - post[1]
1st - pre[0] * post[2]
2nd - pre[1] * post[3]
...
nth - pre[n-1]


'''

def productExceptSelf(unordered_list: list) -> list:

    # define vars.
    n = len(unordered_list)
    forward, backward = [], [0] * n
    cumu_fwd, cumu_bwd = 1, 1
    res = []

    # build out helper arrays.
    for i in range(n):
        cumu_fwd *= unordered_list[i]
        cumu_bwd *= unordered_list[n-i-1]
        forward.append(cumu_fwd)
        backward[n-i-1] = cumu_bwd
    

    # build res
    for k in range(n):
        if k == 0:
            res.append(backward[1])
        elif k == n-1:
            res.append(forward[n-2])
        else:
            res.append(forward[k-1] * backward[k+1])
    return res


# Driver code.
if __name__=="__main__":

    unsorted_list = [3,2,2,1,2,4]

    print(f"productExceptSelf: {productExceptSelf(unsorted_list)}")