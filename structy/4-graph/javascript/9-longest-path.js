/*
Write a function, longestPath, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.

const graph = {
  a: ['c', 'b'],
  b: ['c'],
  c: []
};

longestPath(graph); // -> 2
const graph = {
  a: ['c', 'b'],
  b: ['c'],
  c: [],
  q: ['r'],
  r: ['s', 'u', 't'],
  s: ['t'],
  t: ['u'],
  u: []
};

longestPath(graph); // -> 4
const graph = {
  h: ['i', 'j', 'k'],
  g: ['h'],
  i: [],
  j: [],
  k: [],
  x: ['y'],
  y: []
};

longestPath(graph); // -> 2
const graph = {
  a: ['b'],
  b: ['c'],
  c: [],
  e: ['f'],
  f: ['g'],
  g: ['h'],
  h: []
};

longestPath(graph); // -> 3
*/

const longestPath = (graph) => {
  const distance = {}

  for (let node in graph) {
    if (graph[node].length === 0) {
      distance[node] = 0
    }
  }

  for (let node in graph) {
    traverse(graph, node, distance)
  }
  return Math.max(...Object.values(distance))
};

const traverse = (graph, node, distance) => {
  if (node in distance) return distance[node]

  let maxDistance = 0;

  for (let neighbor of graph[node]) {
    const attempt = traverse(graph, neighbor, distance)
    if (attempt > maxDistance) maxDistance = attempt
  }

  distance[node] = 1 + maxDistance
  return distance[node]

}

