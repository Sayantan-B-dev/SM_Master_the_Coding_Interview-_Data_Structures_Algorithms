# Trie Data Structure (Prefix Tree)

## 1. Introduction

A **Trie** (pronounced "try"), also known as a **Prefix Tree**, is a specialized tree-based data structure optimized for string-based search operations. Unlike binary search trees or hash tables, a trie organizes data by decomposing keys (typically strings) into their constituent characters. Each node in the trie represents a common prefix, and the path from the root to a node spells out a specific string or substring.

Tries are exceptionally efficient for applications involving dictionary lookups, autocomplete suggestions, spell checking, and IP routing, where prefix-based searching is fundamental.

## 2. Structure and Terminology

### 2.1 Root Node

A trie typically begins with an **empty root node** that contains no character value. This root serves as the entry point for all searches and insertions. All words or strings descend from this single root.

### 2.2 Character Nodes

Each child node represents a single character. A node may have up to as many children as there are characters in the alphabet being used. For English language applications, each node may have up to **26 children** (one for each lowercase letter `'a'` through `'z'`), though implementations may optimize storage using maps or arrays.

### 2.3 End-of-Word Marker

Nodes may contain a flag (e.g., a boolean property `isEndOfWord`) indicating that the path from the root to that node forms a complete, valid word. This distinction is crucial because a valid word may also be a prefix of another word (e.g., `"are"` is both a word and a prefix of `"area"`).

### 2.4 Visual Representation (ASCII)

```
                          (Root)
                         /  |   \
                        a   n    t
                       /    |     \
                      r    o*      o*
                     / \    \       \
                    e*  t*   t*      r
                    |          \      \
                    a*          e*     e*
                                \      \
                                 s*     e*
```

**Legend:** `*` denotes end-of-word marker.

**Interpretation of the Trie Above:**
- Words stored: `"are"`, `"art"`, `"area"`, `"no"`, `"not"`, `"note"`, `"notes"`, `"to"`, `"tor"`, `"tree"`.
- The path `a → r → e` spells `"are"` (valid word).
- The path `a → r → e → a` spells `"area"` (valid word).
- The path `n → o` spells `"no"` (valid word).
- The prefix `"no"` is shared among `"no"`, `"not"`, `"note"`, and `"notes"`.

## 3. Core Operations

### 3.1 Search (Lookup)

Searching for a word in a trie involves traversing the tree character by character, starting from the root.

**Algorithm:**
1. Set current node to root.
2. For each character `ch` in the target word:
   - If the current node has a child corresponding to `ch`, move to that child.
   - Otherwise, the word does **not** exist in the trie; return `false`.
3. After processing all characters, check the `isEndOfWord` flag of the final node.
   - If `true`, the exact word exists.
   - If `false`, the prefix exists but is not marked as a complete word.

**Time Complexity:** **O(L)**, where `L` is the length of the word being searched. The number of nodes examined equals exactly the number of characters in the word.

### 3.2 Insertion

Inserting a word follows a similar traversal, creating missing nodes as necessary.

**Algorithm:**
1. Set current node to root.
2. For each character `ch` in the word:
   - If the current node lacks a child for `ch`, create a new node and add it as a child.
   - Move to the child node for `ch`.
3. After the final character, set `isEndOfWord = true` on the last node.

**Time Complexity:** **O(L)** per insertion.

### 3.3 Prefix Search (StartsWith)

A common trie operation is to determine whether any word in the trie begins with a given prefix. This is identical to the search traversal without checking the `isEndOfWord` flag at the end.

**Algorithm:**
1. Traverse the trie following the prefix characters.
2. If traversal succeeds for all characters of the prefix, return `true`.
3. If any character is missing, return `false`.

**Time Complexity:** **O(P)**, where `P` is the length of the prefix.

### 3.4 Autocomplete (Collecting All Words with a Given Prefix)

To generate suggestions, the trie is traversed to the node representing the prefix. From that node, a depth-first search (DFS) collects all descendant paths that terminate with `isEndOfWord = true`.

**Time Complexity:** O(P + N), where `P` is the prefix length and `N` is the number of nodes in the subtree.

## 4. Performance Characteristics

### 4.1 Time Complexity

| Operation | Time Complexity | Explanation |
|-----------|-----------------|-------------|
| Insert    | O(L) | Each character of the word is processed once. |
| Search    | O(L) | Traversal follows exactly the word's length. |
| Delete    | O(L) | Traversal to find node, then backward cleanup. |
| Prefix Search | O(P) | P is the length of the prefix. |

**Comparison with Hash Tables:** While hash tables offer O(1) average-case lookup, they cannot efficiently support prefix-based queries (e.g., "find all words starting with `'pre'`"). A hash table would require scanning all keys—an O(n) operation—whereas a trie accomplishes this in O(P + number of matching words).

### 4.2 Space Complexity

Tries achieve **space efficiency through prefix sharing**. Common prefixes among multiple words are stored only once.

**Example:** The words `"note"`, `"not"`, and `"notes"` share the prefix `"no"` and partially `"not"`. In a trie, the characters `'n'`, `'o'`, `'t'` are stored only once each along the shared path.

**Worst-Case Space:** In the absence of shared prefixes (e.g., storing words that have no common prefixes), a trie may consume more memory than storing the strings directly, due to the overhead of node objects and child references. However, for typical natural language dictionaries, prefix sharing yields substantial memory savings.

## 5. Applications of Tries

| Application | Description |
|-------------|-------------|
| **Autocomplete / Predictive Text** | Search engines, text editors, and mobile keyboards use tries to suggest completions based on a typed prefix. |
| **Spell Checkers** | Tries can quickly verify if a word exists in a dictionary and suggest corrections by exploring near-miss paths. |
| **IP Routing (Longest Prefix Matching)** | Routers use tries (specifically, Patricia tries or Radix trees) to efficiently match IP addresses against routing table prefixes. |
| **Genome Sequencing** | In bioinformatics, suffix tries index DNA sequences for fast pattern matching. |
| **Word Games** | Games like Scrabble or Boggle use tries to validate words and generate possible moves. |
| **T9 Predictive Text** | Classic mobile phone keypad input relied on tries to map numeric sequences to possible words. |

## 6. JavaScript Implementation Example

The following code outlines a basic trie implementation for lowercase English letters.

```javascript
class TrieNode {
    constructor() {
        // Children stored in an object (map) for dynamic alphabet support
        this.children = {};
        // Flag indicating end of a complete word
        this.isEndOfWord = false;
    }
}

class Trie {
    constructor() {
        // Root node is empty (no character)
        this.root = new TrieNode();
    }

    /**
     * Inserts a word into the trie.
     * @param {string} word - The word to insert.
     */
    insert(word) {
        let currentNode = this.root;
        for (const char of word) {
            // Create child node if it does not exist
            if (!currentNode.children[char]) {
                currentNode.children[char] = new TrieNode();
            }
            // Move to the child node
            currentNode = currentNode.children[char];
        }
        // Mark the end of the word
        currentNode.isEndOfWord = true;
    }

    /**
     * Searches for an exact word in the trie.
     * @param {string} word - The word to search.
     * @returns {boolean} - True if the word exists, false otherwise.
     */
    search(word) {
        let currentNode = this.root;
        for (const char of word) {
            if (!currentNode.children[char]) {
                return false; // Character path missing
            }
            currentNode = currentNode.children[char];
        }
        // Word exists only if we reached an end-of-word marker
        return currentNode.isEndOfWord;
    }

    /**
     * Checks if any word in the trie starts with the given prefix.
     * @param {string} prefix - The prefix to check.
     * @returns {boolean} - True if prefix exists, false otherwise.
     */
    startsWith(prefix) {
        let currentNode = this.root;
        for (const char of prefix) {
            if (!currentNode.children[char]) {
                return false;
            }
            currentNode = currentNode.children[char];
        }
        return true; // Prefix path exists
    }
}

// Example Usage
const trie = new Trie();
trie.insert("are");
trie.insert("area");
trie.insert("art");
trie.insert("no");
trie.insert("not");
trie.insert("note");

console.log(trie.search("are"));    // true
console.log(trie.search("ar"));     // false (prefix only)
console.log(trie.startsWith("ar")); // true
console.log(trie.search("notes"));  // false
```

## 7. Comparison with Other Data Structures

| Aspect | Trie | Hash Table | Binary Search Tree |
|--------|------|------------|---------------------|
| **Exact Word Search** | O(L) | O(1) average | O(log n) average |
| **Prefix Search** | O(P) (efficient) | O(n) (requires full scan) | Not natively supported |
| **Space Efficiency** | High for shared prefixes | Overhead for hash table array | Node overhead (two pointers) |
| **Ordered Traversal** | Not inherent (lexicographic via DFS) | No order | In-order traversal yields sorted order |
| **Key Type** | Strings (or sequences) | Any hashable type | Any comparable type |

## 8. Summary

- A **Trie** (Prefix Tree) is a tree-like data structure optimized for string prefix operations.
- Each node represents a character; the path from root to node forms a prefix.
- Core operations (insert, search, prefix check) execute in **O(L)** time, where L is the length of the word/prefix.
- Tries achieve **space efficiency** by storing shared prefixes only once.
- Primary applications include **autocomplete systems**, **dictionary implementations**, **spell checking**, and **IP routing**.
- Tries outperform hash tables and BSTs for prefix-oriented queries, though they may consume more memory when common prefixes are sparse.

Understanding tries is essential for solving string manipulation problems efficiently and for designing systems that rely on fast prefix lookups.