# Graph Representation Techniques

## Introduction

The implementation of graph data structures requires selecting an appropriate representation that balances memory efficiency with operational performance. Three fundamental approaches exist for encoding graph structure in computer memory: edge lists, adjacency lists, and adjacency matrices. Each method offers distinct trade-offs in terms of space complexity and the efficiency of various graph operations.

Understanding these representation techniques is essential for implementing graph algorithms and selecting the optimal structure for specific application requirements.

## Edge List Representation

### Definition

An edge list represents a graph as an explicit enumeration of all edges present in the structure. Each edge is stored as a pair or tuple identifying the two vertices it connects.

### Structure

The edge list is typically implemented as an array where each element is itself an array containing two vertex identifiers.

### Example Construction

Consider the following undirected, unweighted graph:

```
    0 --- 2
         / \
        1   3
         \ /
          *
```

The edge list representation for this graph is:

```javascript
const graph = [
    [0, 2],
    [2, 3],
    [2, 1],
    [1, 3]
];
```

### Interpretation

- The first entry `[0, 2]` indicates an edge connecting vertex 0 to vertex 2
- `[2, 3]` indicates an edge connecting vertex 2 to vertex 3
- `[2, 1]` indicates an edge connecting vertex 2 to vertex 1
- `[1, 3]` indicates an edge connecting vertex 1 to vertex 3

For undirected graphs, each edge appears once. The order within the pair does not imply direction.

### Weighted Edge List

For weighted graphs, each edge entry expands to include the weight value:

```javascript
const weightedGraph = [
    [0, 2, 5],   // Edge from 0 to 2 with weight 5
    [2, 3, 7],   // Edge from 2 to 3 with weight 7
    [2, 1, 3],   // Edge from 2 to 1 with weight 3
    [1, 3, 2]    // Edge from 1 to 3 with weight 2
];
```

### Characteristics

| Aspect | Description |
|--------|-------------|
| Space Complexity | O(E) where E is the number of edges |
| Edge Existence Check | O(E) - requires linear search |
| Neighbor Discovery | O(E) - must scan all edges |
| Memory Efficiency | Excellent for sparse graphs |
| Implementation Simplicity | Very simple to construct |

### Use Cases

Edge lists are particularly suitable for:
- Algorithms that process all edges sequentially (e.g., Kruskal's minimum spanning tree)
- Storage formats where graph data is serialized
- Situations with extremely sparse graphs

## Adjacency List Representation

### Definition

An adjacency list represents a graph by maintaining, for each vertex, a collection of its directly connected neighbors. The vertex itself serves as a key, and its associated value is a list of adjacent vertices.

### Structure

The adjacency list can be implemented using:
- Arrays where the index corresponds to the vertex number
- Objects (hash tables) where keys are vertex identifiers
- Maps where vertex objects map to neighbor collections

### Array-Based Implementation

When vertices are sequential integers starting from zero, an array of arrays provides a natural representation:

```javascript
const adjacencyList = [
    [2],        // Vertex 0 is connected to 2
    [2, 3],     // Vertex 1 is connected to 2 and 3
    [0, 1, 3],  // Vertex 2 is connected to 0, 1, and 3
    [1, 2]      // Vertex 3 is connected to 1 and 2
];
```

### Object-Based Implementation

When vertex identifiers are non-sequential or non-numeric, an object provides clearer semantics:

```javascript
const adjacencyListObject = {
    0: [2],
    1: [2, 3],
    2: [0, 1, 3],
    3: [1, 2]
};
```

This approach extends naturally to vertices with meaningful labels:

```javascript
const cityGraph = {
    'Mumbai': ['Delhi', 'Bangalore'],
    'Delhi': ['Mumbai', 'Kolkata', 'Chennai'],
    'Bangalore': ['Mumbai', 'Chennai'],
    'Chennai': ['Bangalore', 'Delhi'],
    'Kolkata': ['Delhi']
};
```

### Weighted Adjacency List

For weighted graphs, each neighbor entry stores both the adjacent vertex and the edge weight:

```javascript
const weightedAdjacencyList = {
    0: [{ node: 2, weight: 5 }],
    1: [{ node: 2, weight: 3 }, { node: 3, weight: 2 }],
    2: [{ node: 0, weight: 5 }, { node: 1, weight: 3 }, { node: 3, weight: 7 }],
    3: [{ node: 1, weight: 2 }, { node: 2, weight: 7 }]
};
```

### Characteristics

| Aspect | Description |
|--------|-------------|
| Space Complexity | O(V + E) where V is vertices, E is edges |
| Edge Existence Check | O(degree(v)) - proportional to vertex degree |
| Neighbor Discovery | O(1) to access list, O(degree(v)) to iterate |
| Memory Efficiency | Good for sparse to moderately dense graphs |
| Flexibility | Accommodates any vertex identifier type |

### Visual Representation from VisualGo

The VisualGo platform displays adjacency lists using a hash table structure. Each vertex key maps to an array of neighbor entries. For weighted graphs, weights appear alongside neighbor references.

### Advantages

- Efficient iteration over all neighbors of a vertex
- Memory proportional to actual connections
- Simple addition and removal of vertices and edges
- Compatible with linked list, array, or dynamic array implementations

## Adjacency Matrix Representation

### Definition

An adjacency matrix represents a graph using a two-dimensional V × V matrix where the entry at row i, column j indicates the presence (and possibly weight) of an edge from vertex i to vertex j.

### Structure

The matrix is typically implemented as a two-dimensional array with dimensions equal to the number of vertices.

### Unweighted Adjacency Matrix

For unweighted graphs, the matrix contains binary values:
- `1` indicates the presence of an edge
- `0` indicates the absence of an edge

```javascript
const adjacencyMatrix = [
    [0, 0, 1, 0],  // Vertex 0: connected to 2
    [0, 0, 1, 1],  // Vertex 1: connected to 2 and 3
    [1, 1, 0, 1],  // Vertex 2: connected to 0, 1, and 3
    [0, 1, 1, 0]   // Vertex 3: connected to 1 and 2
];
```

### Reading the Matrix

- Row 0, Column 2 contains `1` → Edge exists from 0 to 2
- Row 1, Column 0 contains `0` → No edge from 1 to 0
- Row 2, Column 1 contains `1` → Edge exists from 2 to 1

For undirected graphs, the matrix is symmetric about the main diagonal.

### Weighted Adjacency Matrix

For weighted graphs, the matrix stores weight values instead of binary flags. A special sentinel value (such as `0`, `null`, or `Infinity`) indicates the absence of an edge:

```javascript
const weightedMatrix = [
    [0, 0, 5, 0],  // Edge 0→2 with weight 5
    [0, 0, 3, 2],  // Edges 1→2 (weight 3), 1→3 (weight 2)
    [5, 3, 0, 7],  // Edges 2→0 (5), 2→1 (3), 2→3 (7)
    [0, 2, 7, 0]   // Edges 3→1 (2), 3→2 (7)
];
```

### Object-Based Adjacency Matrix

When vertex identifiers are non-numeric, an object-of-objects structure can emulate matrix behavior:

```javascript
const objectMatrix = {
    'A': { 'A': 0, 'B': 1, 'C': 0 },
    'B': { 'A': 1, 'B': 0, 'C': 1 },
    'C': { 'A': 0, 'B': 1, 'C': 0 }
};
```

### Characteristics

| Aspect | Description |
|--------|-------------|
| Space Complexity | O(V²) regardless of edge count |
| Edge Existence Check | O(1) - direct array access |
| Neighbor Discovery | O(V) - must scan entire row |
| Memory Efficiency | Poor for sparse graphs, excellent for dense graphs |
| Addition/Removal | Vertex addition requires matrix resizing |

### Visual Representation from VisualGo

VisualGo illustrates adjacency matrices with cells containing either binary values (unweighted) or numeric weights (weighted). The matrix visualization enables immediate identification of connection patterns and graph density.

## Comparison of Representation Methods

| Criterion | Edge List | Adjacency List | Adjacency Matrix |
|-----------|-----------|----------------|------------------|
| Space | O(E) | O(V + E) | O(V²) |
| Add Vertex | O(1) | O(1) | O(V²) |
| Add Edge | O(1) | O(1) | O(1) |
| Remove Vertex | O(E) | O(V + E) | O(V²) |
| Remove Edge | O(E) | O(degree) | O(1) |
| Query Edge | O(E) | O(degree) | O(1) |
| Iterate Neighbors | O(E) | O(degree) | O(V) |
| Memory for Sparse Graph | Excellent | Good | Poor |
| Memory for Dense Graph | Good | Good | Excellent |

### Selection Guidelines

**Choose Edge List when:**
- Graph is extremely sparse
- Primary operation is iterating over all edges
- Memory is severely constrained
- Serialization to storage is required

**Choose Adjacency List when:**
- Graph is sparse to moderately dense
- Frequent neighbor iteration is required
- Vertices have non-numeric identifiers
- Dynamic graph modifications are common

**Choose Adjacency Matrix when:**
- Graph is dense (|E| ≈ |V|²)
- Edge existence queries must be O(1)
- Matrix operations (multiplication, eigenvalues) are needed
- Graph is static or small

## JavaScript Implementation: Graph Class with Adjacency List

The following implementation demonstrates a flexible graph class using an adjacency list with object-based storage:

```javascript
class Graph {
    constructor() {
        // Use an object to store adjacency lists
        // Keys: vertex identifiers, Values: arrays of connected vertices
        this.adjacencyList = {};
    }

    // Add a new vertex to the graph
    addVertex(vertex) {
        // Only add if the vertex does not already exist
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
            return true;
        }
        return false;
    }

    // Add an undirected edge between two vertices
    addEdge(vertex1, vertex2) {
        // Both vertices must exist before creating edge
        if (this.adjacencyList[vertex1] && this.adjacencyList[vertex2]) {
            // For undirected graph, add bidirectional connection
            this.adjacencyList[vertex1].push(vertex2);
            this.adjacencyList[vertex2].push(vertex1);
            return true;
        }
        return false;
    }

    // Remove an edge between two vertices
    removeEdge(vertex1, vertex2) {
        if (this.adjacencyList[vertex1] && this.adjacencyList[vertex2]) {
            // Filter out the vertex from neighbor lists
            this.adjacencyList[vertex1] = this.adjacencyList[vertex1]
                .filter(v => v !== vertex2);
            this.adjacencyList[vertex2] = this.adjacencyList[vertex2]
                .filter(v => v !== vertex1);
            return true;
        }
        return false;
    }

    // Remove a vertex and all its connected edges
    removeVertex(vertex) {
        if (!this.adjacencyList[vertex]) return false;

        // Remove all edges referencing this vertex
        while (this.adjacencyList[vertex].length) {
            const adjacentVertex = this.adjacencyList[vertex].pop();
            this.removeEdge(vertex, adjacentVertex);
        }

        // Delete the vertex entry
        delete this.adjacencyList[vertex];
        return true;
    }

    // Display the adjacency list representation
    display() {
        for (let vertex in this.adjacencyList) {
            console.log(`${vertex} → ${this.adjacencyList[vertex].join(', ')}`);
        }
    }

    // Convert to edge list representation
    toEdgeList() {
        const edges = [];
        const visited = new Set();

        for (let vertex in this.adjacencyList) {
            for (let neighbor of this.adjacencyList[vertex]) {
                // Create a canonical edge representation to avoid duplicates
                const edgeKey = [vertex, neighbor].sort().join('-');
                if (!visited.has(edgeKey)) {
                    visited.add(edgeKey);
                    edges.push([vertex, neighbor]);
                }
            }
        }
        return edges;
    }

    // Convert to adjacency matrix representation
    toAdjacencyMatrix() {
        const vertices = Object.keys(this.adjacencyList).sort();
        const n = vertices.length;
        const indexMap = {};
        vertices.forEach((v, i) => indexMap[v] = i);

        // Initialize n×n matrix with zeros
        const matrix = Array(n).fill().map(() => Array(n).fill(0));

        for (let vertex in this.adjacencyList) {
            const row = indexMap[vertex];
            for (let neighbor of this.adjacencyList[vertex]) {
                const col = indexMap[neighbor];
                matrix[row][col] = 1;
            }
        }
        return { vertices, matrix };
    }
}

// Example usage demonstrating all three representations
const graph = new Graph();

// Add vertices
graph.addVertex('0');
graph.addVertex('1');
graph.addVertex('2');
graph.addVertex('3');

// Add edges as per the example graph
graph.addEdge('0', '2');
graph.addEdge('2', '3');
graph.addEdge('2', '1');
graph.addEdge('1', '3');

console.log('Adjacency List Representation:');
graph.display();

console.log('\nEdge List Representation:');
console.log(graph.toEdgeList());

console.log('\nAdjacency Matrix Representation:');
const { vertices, matrix } = graph.toAdjacencyMatrix();
console.log('Vertices:', vertices);
console.log('Matrix:');
matrix.forEach(row => console.log(row));
```

### Expected Output

```
Adjacency List Representation:
0 → 2
1 → 2, 3
2 → 0, 3, 1
3 → 2, 1

Edge List Representation:
[ [ '0', '2' ], [ '2', '3' ], [ '2', '1' ], [ '1', '3' ] ]

Adjacency Matrix Representation:
Vertices: [ '0', '1', '2', '3' ]
Matrix:
[ 0, 0, 1, 0 ]
[ 0, 0, 1, 1 ]
[ 1, 1, 0, 1 ]
[ 0, 1, 1, 0 ]
```

### Implementation Notes

- The adjacency list uses a plain JavaScript object, enabling O(1) vertex access
- The `toEdgeList()` method generates the edge list representation on demand
- The `toAdjacencyMatrix()` method constructs the matrix format with sorted vertex ordering
- Edge addition assumes an undirected graph; directed graphs would require asymmetric addition

## Relationship to Other Data Structures

Graph representations leverage fundamental data structures previously studied:

- **Arrays**: Underlying storage for adjacency matrices and edge lists
- **Linked Lists**: Alternative implementation for adjacency list neighbor collections
- **Hash Tables**: Object-based adjacency lists providing O(1) vertex lookup
- **Trees**: Special case of acyclic connected graphs

The directed acyclic graph shown in earlier examples can be represented using any of the three methods. The adjacency list approach most closely mirrors the linked tree structures with parent-child pointer relationships.

## Conclusion

The selection of a graph representation significantly impacts the performance characteristics of graph algorithms. Edge lists optimize for edge-centric operations and sparse graphs. Adjacency lists provide balanced performance for most practical applications, particularly with dynamic graphs. Adjacency matrices enable constant-time edge queries at the cost of quadratic space complexity.

Understanding these representation trade-offs enables informed design decisions when implementing graph-based solutions. The JavaScript implementation presented using an adjacency list with object storage provides a flexible foundation suitable for most graph algorithm implementations encountered in academic and professional contexts.