
#__________________________________ n * n 

def remove_duplicates(li):
    result = []
    if not li:
        return result
    for item in li:
        if item not in result:
            result.append(item)
    return result
#__________________________________
#Optimization of an algorithm: o(n log n)

def remove_duplicates(li):
    result = []
    if not li:
        return result
    # [1, 1, 1, 2, 2, , 3, 4]
    li.sort()
    prev = li[0]
    result.append(prev)
    for item in li:
        if item != prev:
            result.append(item)
            prev = item
    return  result

#________________________________________________
#The best solution for this problem


def remove_duplicates(li):
    visited = {}
    # visited[item] o(n)
    for item in li:
        if item not in visited:
            visited[item] = True
    return  list(visited.keys())




if __name__ == "__main__":
    list_ = [4, 2, 2, 3, 1, 1, 1, 4, 2]
    results = remove_duplicates(list_)
    print(results)

