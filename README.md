# AI-Algorithms-Python
Optimising and modifying major AI algorithms by dealing with problems


#Solving Water Jug problem using Depth First Search Algorithm
Rules:
1. if x<a (x,y)=(a,y)
2. if y<b (x,y)=(x,b)
3. if x>0 (x,y)=(0,y)
4. if y>0 (x,y)=(x,0)
5. if x>0 (x,y)=(max(0, x + y - b), min(x + y, b))
6. if y>0 (x,y)=(min(x + y, a),max(0, x + y - a))

Algorithm:

1. Initialize visited nodes to null list and append start node into path list.
2. create next state according to rules and if it is not present in visited append into path and visited.
3. Call dfs recursively and if the result is found return path else pop the last state
