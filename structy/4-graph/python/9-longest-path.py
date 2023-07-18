"""
Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) # -> 2
graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

longest_path(graph) # -> 4
graph = {
  'h': ['i', 'j', 'k'],
  'g': ['h'],
  'i': [],
  'j': [],
  'k': [],
  'x': ['y'],
  'y': []
}

longest_path(graph) # -> 2
graph = {
  'a': ['b'],
  'b': ['c'],
  'c': [],
  'e': ['f'],
  'f': ['g'],
  'g': ['h'],
  'h': []
}

longest_path(graph) # -> 3
"""

def longest_path(graph):
  distance = {}
  
  for node in graph:
    if (len(graph[node]) == 0):
      distance[node] = 0
  
  for node in graph:
    traverse(graph, node, distance)
  
  return max(distance.values())

def traverse(graph, node, distance):
  if node in distance: 
    return distance[node]
  
  maxDistance = 0
  for neighbor in graph[node]:
    attempt = traverse(graph, neighbor, distance)
    if attempt > maxDistance:
      maxDistance = attempt
  
  distance[node] = maxDistance + 1
  return distance[node]
  