# Water-Jug solution using DFS
visited = []
path = []


def dfs():
    current = path.pop()
    x = current[0]
    y = current[1]
    path.append(current)
    if x == end or y == end:
        print("Found!")
        return path
    # rule 1
    if current[0] < x_capacity and ([x_capacity, current[1]] not in visited):
        path.append([x_capacity, current[1]])
        visited.append([x_capacity, current[1]])
        res = dfs()
        if res == "Not Found":
            path.pop()
        else:
            return res

    # rule 2
    if current[1] < y_capacity and ([current[0], y_capacity] not in visited):
        path.append([current[0], y_capacity])
        visited.append([current[0], y_capacity])
        res = dfs()
        if res == "Not Found":
            path.pop()
        else:
            return res

    # rule 3
    if current[0] > 0 and ([0, current[1]] not in visited):
        path.append([0, current[1]])
        visited.append([0, current[1]])
        res = dfs()
        if res == "Not Found":
            path.pop()
        else:
            return res

    # rule 4
    if current[1] > 0 and ([x_capacity, 0] not in visited):
        path.append([x_capacity, 0])
        visited.append([x_capacity, 0])
        res = dfs()
        if res == "Not Found":
            path.pop()
        else:
            return res

    # rule 5
    # (x, y) -> (min(x + y, x_capacity), max(0, x + y - x_capacity)) if y > 0
    if current[1] > 0 and ([min(x + y, x_capacity), max(0, x + y - x_capacity)] not in visited):
        path.append([min(x + y, x_capacity), max(0, x + y - x_capacity)])
        visited.append([min(x + y, x_capacity), max(0, x + y - x_capacity)])
        res = dfs()
        if res == "Not Found":
            path.pop()
        else:
            return res

    # rule 6
    # (x, y) -> (max(0, x + y - y_capacity), min(x + y, y_capacity)) if x > 0
    if current[0] > 0 and ([max(0, x + y - y_capacity), min(x + y, y_capacity)] not in visited):
        path.append([max(0, x + y - y_capacity), min(x + y, y_capacity)])
        visited.append([max(0, x + y - y_capacity), min(x + y, y_capacity)])
        res = dfs()
        if res == "Not Found":
            path.pop()
        else:
            return res
    return "Not Found"


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


print("Solution for water jug problem")
x_capacity = int(input("Enter Jug 1 capacity:"))
y_capacity = int(input("Enter Jug 2 capacity:"))
end = int(input("Enter target volume:"))
start = [0, 0]
path.append(start)
# end = 2
# x_capacity = 4
# y_capacity = 3
if end % gcd(x_capacity, y_capacity) == 0:
    print(dfs())
else:
    print("No solution possible for this combination.")

