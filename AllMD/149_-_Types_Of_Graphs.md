# Graph Characteristics and Classification

## Introduction

Graphs exhibit diverse structural properties that determine their applicability to various problem domains. Understanding these characteristics is essential for selecting appropriate graph representations and algorithms. This document examines three fundamental dichotomies used to classify graphs: directed versus undirected, weighted versus unweighted, and cyclic versus acyclic.

## Directed and Undirected Graphs

The distinction between directed and undirected graphs centers on the nature of edges and whether they permit bidirectional traversal.

### Undirected Graphs

In an undirected graph, edges represent symmetric relationships. An edge between vertex A and vertex B implies that traversal is possible in both directions.

**Characteristics:**
- Edges have no orientation or directionality
- The edge (A, B) is identical to the edge (B, A)
- Represents mutual connections or bidirectional pathways

**Visual Representation:**

```
A ---- B
|      |
|      |
C ---- D
```

Each line segment indicates a two-way connection.

**Real-World Example: Facebook Friendships**
- When user A is friends with user B, user B is automatically friends with user A
- The relationship is inherently symmetric and mutual
- Graph operations consider the edge as a single undirected connection

### Directed Graphs

In a directed graph (also called a digraph), edges possess orientation. Each edge points from a source vertex to a destination vertex, permitting traversal only in the specified direction.

**Characteristics:**
- Edges are represented as ordered pairs (A, B) where A is the source and B is the destination
- The edge (A, B) does not imply the existence of (B, A)
- Can model asymmetric relationships or one-way flows

**Visual Representation:**

```
A ---→ B
↑      ↓
|      |
C ←--- D
```

Arrows indicate the permitted direction of traversal.

**Real-World Example: Twitter Following Relationship**
- User A may follow user B without user B following user A
- The follower-followee relationship is unidirectional by default
- The graph contains directed edges from follower to followee

### Comparison Table

| Aspect | Undirected Graph | Directed Graph |
|--------|------------------|----------------|
| Edge Representation | Unordered pair {u, v} | Ordered pair (u, v) |
| Traversal | Bidirectional | Unidirectional |
| Degree Concept | Single degree value | In-degree and out-degree |
| Symmetry | Inherently symmetric | May be asymmetric |
| Typical Applications | Social networks, road networks | Web links, dependency graphs |

## Weighted and Unweighted Graphs

Edges in a graph may carry associated numerical values, known as weights, which quantify the strength, cost, distance, or capacity of the connection.

### Unweighted Graphs

In an unweighted graph, all edges are considered equal in value. The mere existence of a connection is the sole information captured.

**Characteristics:**
- No numerical value attached to edges
- Focus is on connectivity and topology
- Traversal algorithms consider each edge as having unit cost

**Use Cases:**
- Basic social network connectivity
- Unweighted state transition diagrams
- Simple reachability analysis

### Weighted Graphs

Weighted graphs assign a numerical weight to each edge. These weights provide additional semantic information about the relationship between connected vertices.

**Characteristics:**
- Each edge carries a numeric weight value
- Weights may represent distances, times, costs, capacities, or probabilities
- Algorithms leverage weights for optimization problems

**Visual Representation:**

```
A ---5--- B
|         |
3         7
|         |
C ---2--- D
```

Numbers along edges denote their respective weights.

**Real-World Example: Google Maps Navigation**
- Vertices represent locations or intersections
- Edges represent road segments
- Weights represent:
  - Physical distance (kilometers)
  - Travel time (minutes)
  - Traffic congestion factor
  - Toll costs

**Applications of Weighted Graphs:**
- Shortest path computation (Dijkstra's algorithm, Bellman-Ford algorithm)
- Minimum spanning tree construction (Prim's algorithm, Kruskal's algorithm)
- Network flow optimization
- Traveling salesman problem solutions

## Cyclic and Acyclic Graphs

The presence or absence of cycles fundamentally influences graph traversal strategies and the applicability of certain algorithms.

### Cyclic Graphs

A cyclic graph contains at least one cycle—a path that starts and ends at the same vertex without reusing any edges.

**Characteristics:**
- Contains at least one closed loop
- Traversal may return to previously visited vertices
- Requires careful handling to avoid infinite loops during traversal

**Visual Representation:**

```
A --- B
|     |
|     |
C --- D
```

The path A → B → D → C → A constitutes a cycle.

**Common Occurrences:**
- Road networks (typically cyclic to allow return journeys)
- Communication networks with redundancy
- Social networks with mutual connections

### Acyclic Graphs

An acyclic graph contains no cycles. Traversal from any vertex cannot return to that vertex without retracing edges.

**Characteristics:**
- No closed loops exist
- Hierarchical or linear structure
- Enables simplified algorithms and guaranteed termination

**Special Cases:**
- **Directed Acyclic Graph (DAG)**: A directed graph with no directed cycles
- **Tree**: A connected acyclic undirected graph
- **Forest**: A collection of disjoint trees

**Visual Representation of a DAG:**

```
A ---→ B ---→ C
↓       ↓
D ---→ E
```

No path exists that returns to its starting vertex.

**Applications of Acyclic Graphs:**
- Dependency resolution (package managers, build systems)
- Task scheduling with prerequisites
- Version control histories
- Expression trees in compilers

## JavaScript Implementation of Graph Types

The following code illustrates how directed and undirected graphs can be implemented using adjacency lists, with optional weight support.

```javascript
class Graph {
    constructor(directed = false, weighted = false) {
        this.adjacencyList = new Map();
        this.directed = directed;
        this.weighted = weighted;
    }

    // Add a vertex to the graph
    addVertex(vertex) {
        if (!this.adjacencyList.has(vertex)) {
            this.adjacencyList.set(vertex, []);
        }
    }

    // Add an edge between two vertices
    addEdge(source, destination, weight = 1) {
        // Ensure both vertices exist
        if (!this.adjacencyList.has(source)) this.addVertex(source);
        if (!this.adjacencyList.has(destination)) this.addVertex(destination);

        // Create edge representation based on weighted property
        const edgeData = this.weighted ? { node: destination, weight } : destination;

        // Add edge from source to destination
        this.adjacencyList.get(source).push(edgeData);

        // For undirected graphs, add the reverse edge as well
        if (!this.directed) {
            const reverseEdgeData = this.weighted ? { node: source, weight } : source;
            this.adjacencyList.get(destination).push(reverseEdgeData);
        }
    }

    // Check for cycle existence (basic detection for directed graphs)
    hasCycle() {
        const visited = new Set();
        const recursionStack = new Set();

        const detectCycle = (vertex) => {
            visited.add(vertex);
            recursionStack.add(vertex);

            const neighbors = this.adjacencyList.get(vertex) || [];
            for (let neighbor of neighbors) {
                const neighborNode = this.weighted ? neighbor.node : neighbor;
                
                if (!visited.has(neighborNode)) {
                    if (detectCycle(neighborNode)) return true;
                } else if (recursionStack.has(neighborNode)) {
                    return true; // Cycle detected
                }
            }

            recursionStack.delete(vertex);
            return false;
        };

        for (let vertex of this.adjacencyList.keys()) {
            if (!visited.has(vertex)) {
                if (detectCycle(vertex)) return true;
            }
        }
        return false;
    }

    // Display graph structure
    display() {
        for (let [vertex, edges] of this.adjacencyList) {
            const edgeStrings = edges.map(edge => {
                if (this.weighted) {
                    return `${edge.node}(${edge.weight})`;
                }
                return edge;
            });
            const directionSymbol = this.directed ? '→' : '—';
            console.log(`${vertex} ${directionSymbol} ${edgeStrings.join(', ')}`);
        }
    }
}

// Example: Creating a directed weighted graph (e.g., one-way streets with distances)
const trafficNetwork = new Graph(true, true); // directed = true, weighted = true

trafficNetwork.addVertex('A');
trafficNetwork.addVertex('B');
trafficNetwork.addVertex('C');

trafficNetwork.addEdge('A', 'B', 5);
trafficNetwork.addEdge('B', 'C', 3);
trafficNetwork.addEdge('C', 'A', 7); // This creates a cycle

console.log('Traffic Network (Directed Weighted):');
trafficNetwork.display();
console.log('Contains cycle:', trafficNetwork.hasCycle());

// Example: Social network (undirected unweighted)
const socialGraph = new Graph(false, false); // directed = false, weighted = false

socialGraph.addVertex('Alice');
socialGraph.addVertex('Bob');
socialGraph.addVertex('Charlie');

socialGraph.addEdge('Alice', 'Bob');
socialGraph.addEdge('Bob', 'Charlie');

console.log('\nSocial Network (Undirected Unweighted):');
socialGraph.display();
```

### Code Explanation

The `Graph` class constructor accepts two boolean parameters:
- `directed`: Determines whether edges are one-way (true) or two-way (false)
- `weighted`: Determines whether edges store weight values (true) or simple connections (false)

Key methods:
- `addVertex()`: Inserts a new node into the graph
- `addEdge()`: Creates a connection between vertices, respecting directionality and weight settings
- `hasCycle()`: Demonstrates cycle detection for directed graphs using depth-first search with recursion stack tracking
- `display()`: Outputs the graph structure with appropriate visual indicators

## The Internet as a Graph

The global Internet infrastructure exemplifies the practical significance of graph theory at an unprecedented scale.

### The Opte Project Visualization

The Opte Project produces visual representations of Internet connectivity by mapping relationships between autonomous systems and IP address blocks. The resulting images depict:

- **Vertices**: Individual IP addresses or network nodes
- **Edges**: Physical or logical connections between nodes
- **Structure**: A complex web exhibiting both local clustering and global connectivity

This partial map of the Internet illustrates how graph abstractions enable comprehension of massively distributed systems. The visualization reveals:

- **Backbone networks** forming dense cores
- **Edge networks** radiating outward
- **Interconnection points** where multiple networks converge
- **Redundant pathways** providing fault tolerance

### Graph Characteristics of the Internet

The Internet graph demonstrates several of the classification properties discussed:

| Property | Manifestation |
|----------|---------------|
| Directed/Undirected | Predominantly undirected at physical layer; routing may impose directionality |
| Weighted/Unweighted | Weighted by bandwidth, latency, or hop count for routing decisions |
| Cyclic/Acyclic | Highly cyclic to ensure redundancy and alternative routes |

Understanding these characteristics is fundamental for network engineers designing routing protocols, content delivery networks, and fault-tolerant systems.

## Summary

Graph classification based on directionality, weighting, and cyclicity provides a framework for selecting appropriate data structures and algorithms. The following table summarizes key applications associated with each classification:

| Graph Type | Common Applications |
|------------|---------------------|
| Undirected Unweighted | Social friendships, basic connectivity |
| Undirected Weighted | Road networks with distances, communication links with latency |
| Directed Unweighted | Web links, citation networks |
| Directed Weighted | Traffic flow with costs, logistics networks |
| Acyclic (DAG) | Task scheduling, dependency resolution, version histories |
| Cyclic | Redundant networks, transportation systems with return paths |

Mastery of these fundamental graph properties enables effective modeling of diverse real-world systems and informed algorithm selection for problem-solving.