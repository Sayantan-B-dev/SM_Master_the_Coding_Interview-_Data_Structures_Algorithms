# Implementation of Undirected Unweighted Graph using Adjacency List

## Introduction

The implementation of graph data structures using adjacency lists provides an efficient and intuitive approach for representing relationships between entities. This document presents a complete, production-ready implementation of an undirected, unweighted graph using a hash table (JavaScript object) as the underlying storage mechanism for the adjacency list.

The adjacency list representation maintains a collection where each vertex identifier serves as a key, mapping to an array containing all directly connected neighboring vertices. This approach offers O(1) vertex lookup time and O(V + E) space complexity, making it suitable for most practical graph applications.

## Graph Structure to be Implemented

The implementation targets a specific undirected, unweighted graph with seven vertices numbered 0 through 6. The connectivity pattern is illustrated below:

```
        0 ----- 1 ----- 3 ----- 4
         \      |             / |
          \     |            /  |
           \    |           /   |
            \   |          /    |
             \  |         /     |
              \ |        /      |
                2 ----- 5 ----- 6
```

### Connectivity Specification

| Vertex | Connected Neighbors |
|--------|---------------------|
| 0      | 1, 2                |
| 1      | 0, 3                |
| 2      | 0, 5                |
| 3      | 1, 4, 5             |
| 4      | 3, 5, 6             |
| 5      | 2, 3, 4, 6          |
| 6      | 4, 5                |

## Implementation Design

### Choice of Adjacency List with Object Storage

The adjacency list is implemented using a JavaScript object (hash table) for the following reasons:

- **Constant-time vertex access:** Keys provide O(1) lookup regardless of graph size.
- **Flexible vertex identifiers:** Vertices may be numbers, strings, or any valid object key.
- **Efficient vertex removal:** Deleting a key avoids index shifting associated with array-based implementations.
- **Sparse storage:** Only vertices that exist consume memory, unlike adjacency matrices.

### Class Structure

The `Graph` class encapsulates the graph state and operations. The constructor initializes the adjacency list and a vertex counter.

## Complete Graph Implementation

The following JavaScript code provides a fully functional undirected, unweighted graph using the adjacency list representation.

```javascript
/**
 * Graph class implementing an undirected, unweighted graph
 * using an adjacency list stored in a hash table (JavaScript object).
 */
class Graph {
    constructor() {
        // Tracks the total number of vertices currently in the graph.
        // Useful for algorithms requiring vertex count information.
        this.numberOfNodes = 0;

        // Adjacency list implemented as an object.
        // Structure: { vertexKey: [neighbor1, neighbor2, ...] }
        // Using an object provides O(1) average access time for vertices.
        this.adjacencyList = {};
    }

    /**
     * Adds a new isolated vertex to the graph.
     * 
     * When a vertex is added, it initially has no connections.
     * The adjacency list entry is initialized with an empty array.
     * 
     * @param {string|number} node - The identifier for the new vertex.
     * @returns {void}
     */
    addVertex(node) {
        // Check if the vertex already exists to prevent overwriting.
        // If it does not exist, create a new key in the adjacencyList object
        // and assign an empty array to store future neighbor connections.
        if (!this.adjacencyList[node]) {
            this.adjacencyList[node] = [];
            // Increment the vertex count to maintain accurate graph size.
            this.numberOfNodes++;
        }
        // If the vertex already exists, the method silently ignores the request.
        // This prevents accidental data loss of existing connections.
    }

    /**
     * Adds an undirected edge between two existing vertices.
     * 
     * For an undirected graph, the relationship is symmetric.
     * Therefore, both vertices must include each other in their respective neighbor lists.
     * 
     * @param {string|number} node1 - The first vertex identifier.
     * @param {string|number} node2 - The second vertex identifier.
     * @returns {void}
     */
    addEdge(node1, node2) {
        // Retrieve the neighbor array for node1 and append node2.
        // The adjacencyList[node1] is guaranteed to exist if addVertex was called
        // for node1 prior to establishing edges.
        this.adjacencyList[node1].push(node2);
        
        // Retrieve the neighbor array for node2 and append node1.
        // This second push ensures the undirected (bidirectional) property.
        this.adjacencyList[node2].push(node1);
        
        // Note: This basic implementation assumes both vertices already exist.
        // In a production environment, validation should be added.
    }

    /**
     * Displays the graph structure in a human-readable format.
     * 
     * Output format: "vertex --> neighbor1 neighbor2 neighbor3"
     * This method is essential for debugging and verifying graph construction.
     * 
     * @returns {void}
     */
    showConnections() {
        // Iterate over all keys (vertex identifiers) in the adjacency list.
        const allVertices = Object.keys(this.adjacencyList);
        
        for (let vertex of allVertices) {
            // Retrieve the array of connected neighbors for the current vertex.
            let connections = this.adjacencyList[vertex];
            
            // Build a string representation by concatenating all neighbors.
            let connectionString = '';
            for (let neighbor of connections) {
                connectionString += neighbor + ' ';
            }
            
            // Log the formatted output. trim() removes trailing whitespace.
            console.log(vertex + ' --> ' + connectionString.trim());
        }
    }
}
```

## Usage Example: Building the Specified Graph

The following code demonstrates the construction of the graph depicted earlier using the `Graph` class methods.

```javascript
// Instantiate a new Graph object
const myGraph = new Graph();

// ----- Phase 1: Add all vertices -----
// Each vertex is added individually. The order of addition does not matter.
myGraph.addVertex('0');
myGraph.addVertex('1');
myGraph.addVertex('2');
myGraph.addVertex('3');
myGraph.addVertex('4');
myGraph.addVertex('5');
myGraph.addVertex('6');

// ----- Phase 2: Establish undirected edges -----
// Each edge is specified exactly once. The addEdge method automatically
// creates the reverse connection, maintaining the undirected property.

// Connections for vertex 0
myGraph.addEdge('0', '1');
myGraph.addEdge('0', '2');

// Connections for vertex 1
myGraph.addEdge('1', '3');

// Connections for vertex 2
myGraph.addEdge('2', '5');

// Connections for vertex 3
myGraph.addEdge('3', '4');
myGraph.addEdge('3', '5');

// Connections for vertex 4
myGraph.addEdge('4', '5');
myGraph.addEdge('4', '6');

// Connections for vertex 5
myGraph.addEdge('5', '6');

// ----- Phase 3: Verify the constructed graph -----
// Display the complete adjacency list to confirm correctness.
myGraph.showConnections();
```

## Expected Output

Execution of the above code produces the following console output:

```
0 --> 1 2
1 --> 0 3
2 --> 0 5
3 --> 1 4 5
4 --> 3 5 6
5 --> 2 3 4 6
6 --> 4 5
```

### Verification of Undirected Property

The output confirms the symmetric nature of the undirected graph:

- Vertex `0` lists `1` and `2` as neighbors; both `1` and `2` include `0` in their respective neighbor lists.
- Vertex `5` lists `2`, `3`, `4`, `6` as neighbors; each of those vertices reciprocates by including `5`.

## Implementation Analysis

### Time Complexity

| Operation | Time Complexity | Explanation |
|-----------|-----------------|-------------|
| `addVertex` | O(1) | Object property assignment is constant time. |
| `addEdge` | O(1) | Array `push` operations are amortized constant time. |
| `showConnections` | O(V + E) | Must iterate over all vertices and their neighbors. |

### Space Complexity

The space complexity is O(V + E), where:
- **V** represents the number of vertices (keys in the object plus empty arrays)
- **E** represents the number of edges (each undirected edge contributes two entries across the neighbor arrays)

### Design Considerations and Potential Enhancements

**1. Edge Duplication Prevention**

The basic implementation does not prevent duplicate edge additions. Repeated calls to `addEdge('0', '1')` would result in multiple entries of `1` in vertex `0`'s neighbor list. A robust implementation should include a check:

```javascript
addEdge(node1, node2) {
    // Avoid duplicate edges by checking existence before pushing
    if (!this.adjacencyList[node1].includes(node2)) {
        this.adjacencyList[node1].push(node2);
        this.adjacencyList[node2].push(node1);
    }
}
```

**2. Vertex Existence Validation**

The current `addEdge` method assumes both vertices exist. A defensive implementation would verify:

```javascript
addEdge(node1, node2) {
    if (this.adjacencyList[node1] && this.adjacencyList[node2]) {
        // Proceed with edge addition
    } else {
        throw new Error('Both vertices must exist before adding an edge.');
    }
}
```

**3. Vertex Removal**

Removing a vertex requires:
- Deleting its entry from the adjacency list
- Scanning all other vertices' neighbor lists to remove references
- Decrementing `numberOfNodes`

**4. Edge Removal**

Removing an edge entails filtering the neighbor arrays of both connected vertices.

## Relationship to Fundamental Data Structures

The graph implementation leverages core data structures previously studied:

| Data Structure | Role in Graph Implementation |
|----------------|------------------------------|
| Hash Table (Object) | Provides O(1) vertex lookup for the adjacency list |
| Array | Stores neighbor collections for each vertex |
| Linked List (Alternative) | Could replace arrays for neighbor storage, beneficial for frequent edge deletions |

This demonstrates that graphs are not fundamentally new abstractions but rather composite structures built upon foundational data organization principles.

## Conclusion

The implementation of an undirected, unweighted graph using an adjacency list with object-based storage is concise yet powerful. The code presented fulfills the requirements of creating a graph with seven vertices and the specified edge connections. Through careful use of hash table properties and array operations, the graph class achieves efficient performance characteristics suitable for a wide range of graph algorithm applications.

Understanding this implementation provides the necessary foundation for exploring advanced graph topics including traversal algorithms (breadth-first search, depth-first search), shortest path computations, and cycle detection mechanisms. The simplicity of the core operations belies the sophisticated modeling capabilities that graphs enable across diverse computational domains.