"""

Import dependent libraries
    - numpy for random draw and array manupulation
    - matplotlib for visualizations
    - time, to check compuation time s

"""
import numpy as np 
import matplotlib.pyplot as plt
import time

def set_size(n_size): # uniform distribution between 0 to 1 as default  
    v = np.random.uniform(size = (2, n_size))  # 2 dimensional, draw 'n_size' out of uniform distribution 
    x = v[0]  # set the first draw as x values
    y = v[1]  # set the second darw as y values 
    return x, y   # return x, and y 

def scatter_draw(x, y):  # Purple, Diamond points scatter diagram: my favorite
    plt.figure(figsize = (20, 12))  # prefer big size picture as it is easier to read 
    plt.scatter(x, y, c = 'purple', marker = 'D')  # set the point's color to purple, and shape of diamond
    plt.axvline(x = 0.5)  # add vertical line in the middle point x = 0.5
    plt.show()
    return

def pair_xy(X, Y): # pair x and y to (x,y) 2-dim coordinates
    pair = []
    for x, y in zip(X, Y):
        pair.append((x,y))
    return pair

def get_distance(pt1, pt2):  # calculate Uclidean distance between two points in 2d
    return np.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2) 

def split_LR(pairs, by = 0.5):  # split in half, default threshold is 0.5 (as 0,1 uniform distribution setting)
    pairs_L = [pair for pair in pairs if pair[0] <= by]
    pairs_R = [pair for pair in pairs if pair[0] > by]
    return pairs_L, pairs_R

def brute_dist_plane(pairs):  # calculate distances within a plane containing multiple coordinates 
    collection_distances = []
    for i in range(len(pairs)-1):
        for j in range(i+1, len(pairs)):
            collection_distances.append(get_distance(pairs[i], pairs[j]))
    return collection_distances

def special_case(d, pairs): 
    """
    d: minimum out of minimum value of Left, and minimum value of Right
    """
    tmp = []
    for i in pairs:
        if i[0]>= 0.5-d and i[0] <= 0.5+d:
            tmp.append(i)
    return tmp  # list containing xy tuples 

def sort_and_new(tmp):  # return special points sorted by y values 
    sorted_by_y = sorted(tmp, key = lambda tup:tup[1])
    #print(sorted_by_y)
    return sorted_by_y

def replace_d(sorted_by_y, d):
    tmp2 = []
    for i in range(len(sorted_by_y)-1):
        for j in range(i+1, len(sorted_by_y)):
            if (sorted_by_y[j][1]-sorted_by_y[i][1])<=d:
                tmp2.append(get_distance(sorted_by_y[j],sorted_by_y[i]))
    #print(tmp2)
    if sum(tmp2) == 0:
        return d
    elif min(tmp2) < d:
        d = min(tmp2)
    
    return d

if __name__ == "__main__":
    start_time = time.time()
    n = int(input("Enter n: "))
    x, y = set_size(n)
    pairs = pair_xy(x, y)
    L, R = split_LR(pairs)
    _left, _right = brute_dist_plane(L), brute_dist_plane(R)
    d = min(min(_left), min(_right)) 
    tmp = special_case(d, pairs) 
    sorted_by_y = sort_and_new(tmp)
    replace_d(sorted_by_y, d) 
    print("--- %s seconds ---" % (time.time() - start_time))

# def brutal_bruteForce():
#     start_time = time.time()  # record the starting time
#     n = int(input("Enter n: "))  # get the input value to decide how many random samples to take
#     x, y = set_size(n)  # draw points out of uniform distribution [0,1]
#     pairs = pair_xy(x, y)  # Set up pairs 
#     d = 1 # just starting value, which surely will be replaced with another smaller values 
#     for i in range(len(pairs)-1):  # 
#         for j in range(i+1, len(pairs)):
#             if get_distance(pairs[i], pairs[j]) <= d:
#                 d = get_distance(pairs[i], pairs[j])
#     print("--- %s seconds ---" % (time.time() - start_time))
#     return d
