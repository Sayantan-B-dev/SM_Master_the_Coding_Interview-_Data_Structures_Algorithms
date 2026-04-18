# Implementation of Undirected Unweighted Graph using Adjacency List

## Introduction

Graph implementation using an adjacency list represents one of the most practical and efficient approaches for storing graph structures in computer memory. This document presents a complete implementation of an undirected, unweighted graph using a hash table (JavaScript object) as the underlying adjacency list storage mechanism.

The adjacency list approach maintains a collection where each vertex serves as a key, mapping to an array of its directly connected neighboring vertices. For undirected graphs, edge relationships are symmetric, requiring bidirectional updates during edge addition operations.

## Graph Structure Overview

The target graph for implementation contains seven vertices (0 through 6) with the following connectivity pattern:

```
    0 --- 1 --- 3 --- 4
     \    |         / |
      \   |        /  |
       \  |       /   |
        \ |      /    |
          2 --- 5 --- 6
```

This structure exhibits multiple cycles and varying vertex degrees, providing a suitable test case for graph implementation verification.

## Adjacency List Representation using Hash Table

### Rationale for Object-Based Storage

JavaScript objects (hash tables) offer distinct advantages over array-based adjacency lists for graph representation:

| Advantage | Explanation |
|-----------|-------------|
| Constant-time vertex lookup | O(1) access to any vertex's neighbor list regardless of identifier type |
| Non-sequential identifier support | Vertex identifiers need not be consecutive integers |
| Efficient vertex removal | No shifting or index reassignment required |
| Sparse storage | Only stores vertices that actually exist |

When vertices are removed from a graph, array-based representations suffer from index shifting costs or memory fragmentation. Object-based storage eliminates these concerns entirely.

### Expected Adjacency List Structure

After construction, the adjacency list object should contain entries similar to:

```javascript
{
    0: [1, 2],
    1: [0, 3],
    2: [0, 5],
    3: [1, 4, 5],
    4: [3, 5, 6],
    5: [2, 3, 4, 6],
    6: [4, 5]
}
```

## Graph Class Implementation

### Constructor

The constructor initializes the fundamental properties required for graph management:

```javascript
class Graph {
    constructor() {
        // Total count of vertices currently in the graph
        // Useful for algorithms requiring vertex count knowledge
        this.numberOfNodes = 0;

        // Adjacency list implemented as a hash table (JavaScript object)
        // Each key represents a vertex identifier
        // Each value is an array of connected neighbor vertices
        this.adjacencyList = {};
    }
}
```

### Method: addVertex(vertex)

This method introduces a new isolated vertex to the graph structure.

**Algorithm Steps:**
1. Verify that the vertex does not already exist in the adjacency list
2. Create a new entry with the vertex as key and an empty array as its neighbor list
3. Increment the vertex count

```javascript
/**
 * Adds a new vertex (node) to the graph.
 * @param {string|number} vertex - The identifier of the vertex to add.
 * @returns {boolean} - Returns true if vertex was added, false if it already exists.
 */
addVertex(vertex) {
    // Check if vertex already exists to prevent overwriting connections
    if (!this.adjacencyList[vertex]) {
        // Initialize empty neighbor list for the new vertex
        this.adjacencyList[vertex] = [];
        
        // Increment total vertex count
        this.numberOfNodes++;
        
        return true;
    }
    // Vertex already present; no duplicate addition
    return false;
}
```

### Method: addEdge(vertex1, vertex2)

This method establishes an undirected connection between two existing vertices. The undirected nature mandates symmetric updates to both vertices' neighbor lists.

**Algorithm Steps:**
1. Verify that both vertices exist in the graph
2. Add vertex2 to vertex1's neighbor list
3. Add vertex1 to vertex2's neighbor list
4. The order of vertices in function call does not affect the result

```javascript
/**
 * Adds an undirected edge between two existing vertices.
 * For undirected graphs, the connection is bidirectional.
 * @param {string|number} vertex1 - First vertex identifier.
 * @param {string|number} vertex2 - Second vertex identifier.
 * @returns {boolean} - Returns true if edge was added, false if either vertex missing.
 */
addEdge(vertex1, vertex2) {
    // Both vertices must exist before establishing connection
    if (this.adjacencyList[vertex1] && this.adjacencyList[vertex2]) {
        // Add vertex2 to the neighbor list of vertex1
        this.adjacencyList[vertex1].push(vertex2);
        
        // Add vertex1 to the neighbor list of vertex2 (undirected symmetry)
        this.adjacencyList[vertex2].push(vertex1);
        
        return true;
    }
    // One or both vertices do not exist
    return false;
}
```

**Important Considerations:**
- No duplicate edge prevention is implemented in this basic version; repeated calls would create duplicate entries
- For production implementations, consider checking existing connections before addition
- The order of parameters does not affect the resulting adjacency list structure

### Helper Method: showConnections()

This utility method displays the complete graph structure for verification and debugging purposes.

```javascript
/**
 * Displays all vertices and their corresponding connections.
 * Output format: "vertex --> neighbor1 neighbor2 neighbor3"
 */
showConnections() {
    // Iterate through all vertices in the adjacency list
    const allVertices = Object.keys(this.adjacencyList);
    
    for (let vertex of allVertices) {
        // Retrieve the array of connected neighbors
        let connections = this.adjacencyList[vertex];
        
        // Build a string representation of all connections
        let connectionString = '';
        for (let neighbor of connections) {
            connectionString += neighbor + ' ';
        }
        
        // Display the vertex and its connections
        console.log(vertex + ' --> ' + connectionString.trim());
    }
}
```

## Complete Implementation

The following code presents the complete Graph class with all described methods:

```javascript
class Graph {
    constructor() {
        // Track total number of vertices in the graph
        this.numberOfNodes = 0;
        
        // Adjacency list using object (hash table) storage
        // Structure: { vertex: [neighbor1, neighbor2, ...] }
        this.adjacencyList = {};
    }

    /**
     * Adds a new vertex to the graph.
     * @param {string|number} vertex - Vertex identifier.
     * @returns {boolean} Success indicator.
     */
    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
            this.numberOfNodes++;
            return true;
        }
        return false;
    }

    /**
     * Adds an undirected edge between two existing vertices.
     * @param {string|number} vertex1 - First vertex.
     * @param {string|number} vertex2 - Second vertex.
     * @returns {boolean} Success indicator.
     */
    addEdge(vertex1, vertex2) {
        // Verify both vertices exist before adding edge
        if (this.adjacencyList[vertex1] && this.adjacencyList[vertex2]) {
            // Bidirectional connection for undirected graph
            this.adjacencyList[vertex1].push(vertex2);
            this.adjacencyList[vertex2].push(vertex1);
            return true;
        }
        return false;
    }

    /**
     * Displays the adjacency list representation of the graph.
     * Format: "vertex --> neighbor1 neighbor2 ..."
     */
    showConnections() {
        const vertices = Object.keys(this.adjacencyList);
        
        for (let vertex of vertices) {
            let connections = this.adjacencyList[vertex];
            let connectionString = '';
            
            for (let neighbor of connections) {
                connectionString += neighbor + ' ';
            }
            
            console.log(vertex + ' --> ' + connectionString.trim());
        }
    }
}
```

## Usage Example

The following code constructs the graph depicted in the introduction and verifies its structure:

```javascript
// Create a new graph instance
const myGraph = new Graph();

// Add all vertices (0 through 6)
// Vertex addition order does not affect final structure
myGraph.addVertex('0');
myGraph.addVertex('1');
myGraph.addVertex('2');
myGraph.addVertex('3');
myGraph.addVertex('4');
myGraph.addVertex('5');
myGraph.addVertex('6');

// Establish undirected edges according to the target graph
// Each edge is specified exactly once due to bidirectional addition

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

// Display the resulting graph structure for verification
myGraph.showConnections();
```

## Expected Output

Execution of the above code produces the following adjacency list representation:

```
0 --> 1 2
1 --> 0 3
2 --> 0 5
3 --> 1 4 5
4 --> 3 5 6
5 --> 2 3 4 6
6 --> 4 5
```

This output correctly reflects the undirected, unweighted graph structure specified in the problem statement.

## Verification of Undirected Property

Notice the symmetric nature of connections:
- Vertex 0 lists 1 and 2 as neighbors; both 1 and 2 list 0 in their respective neighbor arrays
- Vertex 5 lists 2, 3, 4, 6 as neighbors; each of those vertices includes 5 in its neighbor list

This symmetry confirms the undirected nature of the implemented graph.

## Implementation Considerations

### Edge Duplication Prevention

The basic implementation does not prevent duplicate edge additions. Repeated calls to `addEdge(0, 1)` would result in multiple entries of `1` in vertex 0's neighbor list. A production implementation should include duplicate checking:

```javascript
addEdge(vertex1, vertex2) {
    if (this.adjacencyList[vertex1] && this.adjacencyList[vertex2]) {
        // Check for existing connection before adding
        if (!this.adjacencyList[vertex1].includes(vertex2)) {
            this.adjacencyList[vertex1].push(vertex2);
            this.adjacencyList[vertex2].push(vertex1);
        }
        return true;
    }
    return false;
}
```

### Vertex Removal

Removing a vertex requires:
1. Deleting the vertex entry from the adjacency list
2. Removing all references to that vertex from other vertices' neighbor lists
3. Decrementing the vertex count

### Memory Complexity

The adjacency list implementation exhibits space complexity of O(V + E), where V represents the number of vertices and E represents the number of edges. This efficiency makes it suitable for sparse to moderately dense graphs.

## Conclusion

The implementation presented demonstrates a complete, functional undirected unweighted graph using an adjacency list with object-based storage. The hash table approach provides efficient O(1) vertex access and flexible vertex identifier support. This implementation serves as a foundation for more advanced graph algorithms including traversal, shortest path computation, and cycle detection.

The modular design enables straightforward extension to support weighted edges, directed connections, and additional graph operations such as vertex and edge removal. Understanding this core implementation is essential for progressing to advanced graph theory concepts and applications.