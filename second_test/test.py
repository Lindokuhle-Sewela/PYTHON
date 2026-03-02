# from collections import Counter
# import re
# import math 
# def frequency(string):
#     words = re.findall(r'\w+', string.lower())
#     return dict(Counter(words))


# print(frequency("the cat sat on the mat"))

# #[3,1,2,1,3] >>>> [3,1,2]
# def dupes_order(dupes):
#     d_o = []
#     for d in dupes:
#         if d not in d_o:
#             d_o.append(d)
#     return d_o
# print(dupes_order([3,1,2,1,3]))

# def two_d(n, size):
#     d = []
#     for i in n:
#         for j in i:
#             d = [j] 
#     return d


# print(two_d([[1,2,3],[4,5,6]], 2))



def pair(arr:list,k:int,check = []) -> bool:

    if len(arr) % 2 == 1:
        return False
    
    
    while len(arr) != 0:
        
        if (arr[0] + arr[-1]) % k == 0:
            arr.remove(arr[0])
            arr.remove(arr[-1])
            check.append(True)
        else:
            check.append(False)

    if len(arr) == 0:
            for i in check:
                if i == False:
                    return False
                else:
                    return True






new_list = [9, 5, 7, 3]
k = 6

print(pair(new_list,k))

def group(arr):
    res = {}
            
    for s in arr:
        s_sorted = sorted(s)
        key = tuple(s_sorted)
        
        if key not in res:
            res[key] = [s]
        else:
            res[key].append(s)
            
    return res.values()

print(group(["act", "god", "cat", "dog", "tac"]))