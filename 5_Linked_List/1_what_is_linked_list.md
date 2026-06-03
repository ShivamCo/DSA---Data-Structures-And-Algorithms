# 📚 Linked List

A **Linked List** is a linear data structure in which elements are stored in  **non-contiguous memory locations** . Unlike arrays, linked list elements (nodes) do not need to be stored next to each other in memory.

Nodes are connected using references (or pointers), allowing the list to maintain a sequence of elements.

---

## 🧩 Structure of a Node

Each node consists of two parts:

```text
+---------+---------+
|  Data   |  Next   |
+---------+---------+
```

### Components

* **Data** → Stores the actual value or information.
* **Next** → Stores a reference to the next node in the list.

Example:

```text
Head
 ↓
+----+------+    +----+------+    +----+------+
| 10 |   •-----> | 20 |   •-----> | 30 | None |
+----+------+    +----+------+    +----+------+
```

---

## 🔥 Why Use Linked Lists?

### Advantages

* Dynamic size (can grow or shrink at runtime).
* Efficient insertion and deletion operations.
* No need for contiguous memory allocation.

### Disadvantages

* Extra memory is required for storing references.
* No direct indexing like arrays.
* Traversal is slower because elements must be accessed sequentially.

---

# Types of Linked Lists

## 1️⃣ Singly Linked List (SLL)

In a Singly Linked List, each node stores a reference to the  **next node only** .

### Characteristics

* Traversal is possible only in the forward direction.
* Cannot directly access the previous node.
* Last node points to `None`.

### Representation

```text
Head
 ↓
10 → 20 → 30 → None
```

### Python Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

## 2️⃣ Doubly Linked List (DLL)

In a Doubly Linked List, each node stores:

* Reference to the next node
* Reference to the previous node

### Characteristics

* Supports traversal in both directions.
* Easier deletion operations.
* Requires extra memory.

### Representation

```text
None ← 10 ⇄ 20 ⇄ 30 → None
```

### Node Structure

```text
+------+-------+------+
| Prev | Data  | Next |
+------+-------+------+
```

---

## 3️⃣ Circular Singly Linked List (CSLL)

A Circular Singly Linked List is similar to a Singly Linked List, but the last node points back to the head node.

### Representation

```text
      ┌─────────────┐
      │             ▼
10 → 20 → 30 → 40
▲                │
└────────────────┘
```

### Characteristics

* No node contains `None`.
* Useful in round-robin scheduling.
* Traversal can start from any node.

---

## 4️⃣ Circular Doubly Linked List (CDLL)

A Circular Doubly Linked List is a Doubly Linked List where:

* Tail's next points to Head.
* Head's previous points to Tail.

### Representation

```text
      ┌─────────────┐
      ▼             │
10 ⇄ 20 ⇄ 30 ⇄ 40
▲                ▼
└────────────────┘
```

### Characteristics

* Traversal in both directions.
* No `None` references.
* Frequently used in navigation systems and playlists.
