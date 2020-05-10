coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
def check(coordinates):
    if len(coordinates) == 2:
        return True
            # number of points can be both even and odd 
    first_slope = slope(coordinates[0], coordinates[1])
    cnt = 0 # check diff val
    for i in range(len(coordinates)-1):
        if first_slope != slope(coordinates[i], coordinates[i+1]):
            cnt += 1
    
    return cnt==0


def distance(p1, p2):
    if p2 > p1:
        return p2-p1
    else:
        return p1-p2

def slope(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    if distance(x1, x2) != 0:
        return distance(y1,y2)/distance(x1,x2)
    else:
        return 

print(slope([1,2],[2,5]))
    
def check2(coord):
    x1, y1 = coord[0]
    slope = None
    for x2, y2 in coord[1:]:
        if slope is None:
            slope = (y2-y1)/(x2-x1)
            continue 
        if slope != (y2-y1)/(x2-x1):
            return False
        
    return True
if __name__ == "__main__":
    print(check2(coordinates))