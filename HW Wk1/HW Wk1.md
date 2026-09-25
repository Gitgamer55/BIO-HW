# The ULTIMATE CS Cheatsheet

## WORLD 1: Concrete structures inside the language

### LEVEL 1: The beginning of it all

#### Arrays
An array (or 'list') is a data structure that allows storage of multiple objects. 
It works with simple operations such as adding, retrieving, and deleting elements. 
On its own it is simple, but this is the foundation to a lot of the next few data structures.

##### Code Example
```python
# Creating a simple array (list)
scores = [85, 90, 78, 92, 88]

# Retrieving an item instantly by its index position
first_score = scores[0]

# Inserting an item in the middle (forces subsequent elements to shift)
scores.insert(2, 95)

# Deleting an item from the middle (forces subsequent elements to shift)
scores.pop(3)

print("Modified scores list:", scores)
```

##### Expected Output
```text
Modified scores list: [85, 90, 95, 92, 88]
```

Before we see what more we can do with arrays, let us actually look at one more quick structure that lots, if not all, future structures use.

#### Pointers
A pointer is a structure that simply references another location in memory. 
It doesn't really have operations, but instead it merges with a data structure with functions (like arrays) to create special combinations.

##### Code Example
```python
# In Python, variables acting on objects are implicit pointers (references)
# Let's create two node components referencing each other via memory paths
node_a = {"data": "First Item", "next": None}
node_b = {"data": "Second Item", "next": None}

# Storing a reference (pointer) to node_b inside node_a
node_a["next"] = node_b

print("Node A contains a pointer to Node B's address data:", node_a["next"]["data"])
```

##### Expected Output
```text
Node A contains a pointer to Node B's address data: Second Item
```

Now we can level up.

---

### LEVEL 2: Direct derivations/dependencies from Level 1

#### Linked list
A linked list is an array where elements are not stored next to each other in memory, but are instead chained together using pointers. 
It works with similar operations to the humble list, but instead it dynamically allocates memory by linking its elements (as they are in a nonlinear order). 
It is mainly used to not require a block of space in memory like arrays do, but it also provides the foundation for more advanced structures like the stack and queue.

##### Code Example
```python
# Definition of a single node in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer initialized to nothing

# Instantiating elements
head = Node("Data Alpha")
second = Node("Data Beta")
tail = Node("Data Gamma")

# Chaining components dynamically via pointer variables
head.next = second
second.next = tail

# Traversing the linear pointer references
current = head
while current:
    print(f"[{current.data}] -> ", end="")
    current = current.next
print("None")
```

##### Expected Output
```text
[Data Alpha] -> [Data Beta] -> [Data Gamma] -> None
```

#### Hash Table/Dictionary
Ah, the humble hash table. It actually has a lot of uses for what it is. 
It is quite an advanced array, because it stores array indices (or 'keys') and uses a mathematical formula to quickly and efficiently find the value associated to the specific key. 
It works with, once again, simple operations such as insertion and deletion. The difference is that since it uses a mathematical formula to find the value, two keys can clash, and therefore it dynamically resolves that. 
It is used in the cases where it is critical for item lookup to be as fast as possible (as it becomes O(1) time compared to usual slow O(n)), but it itself provides the basis to sets.

##### Code Example
```python
# Initializing a key-value hash store
student_directory = {"ID_47": "Alice", "ID_142": "Bob"}

# Insertion of a new entry
student_directory["ID_183"] = "Charlie"

# Instant O(1) retrieval using a hashed lookup key
target_student = student_directory["ID_142"]

# Deletion of an entry
del student_directory["ID_47"]

print("Directory Contents:", student_directory)
print("Looked up student:", target_student)
```

##### Expected Output
```text
Directory Contents: {'ID_142': 'Bob', 'ID_183': 'Charlie'}
Looked up student: Bob
```

And that concludes our whistle-stop tour of Level 2! Now for the abstract concepts in the next.

---

### LEVEL 3: Structures defined by concepts, instead of new components

This is the real meat. We're getting into the likes of sets, stacks, queues and deques. For those wanting trees, that comes a lot later as even MORE just a concept, as those in the next World 2 (including Trees) do not even have their own structures - instead, they're defined using the previous structures from Levels 1-4.

#### Stack
A stack is a linked list which has a strict insertion, deletion, and lookup order. 
All of its operations are last in, first out (LIFO). 
All elements are inserted, deleted, and looked up at the end of the structure. 
It is useful for certain tasks such as tracking the largest element after the kth element (using a monotonic stack), and tracking the history of past elements.

##### Code Example
```python
# Simulating a strict linear stack using primitive arrays
action_history = []

# Performing Push operations at the end of the structure
action_history.append("Click Home")
action_history.append("Open Settings")
action_history.append("Toggle Dark Mode")

# Performing Pop operation from the end - Last In, First Out (LIFO)
undone_action = action_history.pop()

print("Remaining Stack States:", action_history)
print("Popped (Undone) Action:", undone_action)
```

##### Expected Output
```text
Remaining Stack States: ['Click Home', 'Open Settings']
Popped (Undone) Action: Toggle Dark Mode
```

#### Set
A set is a hash table that simply uses only the keys for efficient operations. 
Much of the operations to a hash table remain identical, but it also dynamically detects and removes duplicate elements. 
This structure is used for counting unique elements in a list (as it removes duplicates) and also forms the basis of the Multiset.

##### Code Example
```python
# Initializing a set container
unique_tags = {"cs", "coding", "revision"}

# Attempting to add a duplicate item
unique_tags.add("cs")

# Adding a unique item
unique_tags.add("algorithms")

print("Set elements (duplicates automatically stripped):", unique_tags)
```

##### Expected Output
```text
Set elements (duplicates automatically stripped): {'cs', 'coding', 'revision', 'algorithms'}
```

#### Queue
This is a very commonly used linked list structure where it follows a first in, first out (FIFO), much like a real queue would. 
Elements are inserted at the end of the structure but looked up and deleted at the beginning. Once again, like a queue. 
It is useful for processing nodes in a tree or a graph, such as in algorithms like BFS.

##### Code Example
```python
from collections import deque

# Initializing an efficient queue pipeline
task_line = deque()

# Inserting at the end of the structure (Enqueue)
task_line.append("Render Frame 1")
task_line.append("Render Frame 2")
task_line.append("Render Frame 3")

# Deleting from the beginning of the structure (Dequeue) - First In, First Out (FIFO)
completed_task = task_line.popleft()

print("Remaining tasks in line:", list(task_line))
print("Processed task:", completed_task)
```

##### Expected Output
```text
Remaining tasks in line: ['Render Frame 2', 'Render Frame 3']
Processed task: Render Frame 1
```

---

### LEVEL 4: Subderivations of Level 3

This section is very short as it simply contains structures that are almost identical to Level 3, except with minimal changes.

#### Deque
This is a queue that can insert, lookup, and delete elements on both ends. 
This structure also used for BFS.

#### Multiset
This is a set that handles multiple copies of the same element. Enough said.

---

## APPENDIX: World 1 Complexity Mapping Master Table

| Structure | Access (Avg / Worst) | Search (Avg / Worst) | Insertion (Avg / Worst) | Deletion (Avg / Worst) | Space Complexity (Worst) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Array** | O(1) / O(1) | O(n) / O(n) | O(n) / O(n) | O(n) / O(n) | O(n) |
| **Pointer** | O(1) / O(1) | N/A | N/A | N/A | O(1) |
| **Linked List** | O(n) / O(n) | O(n) / O(n) | O(1) / O(1)* | O(1) / O(1)* | O(n) |
| **Hash Table** | N/A | O(1) / O(n) | O(1) / O(n) | O(1) / O(n) | O(n) |
| **Stack** | O(n) / O(n) | O(n) / O(n) | O(1) / O(1) | O(1) / O(1) | O(n) |
| **Set** | N/A | O(1) / O(n) | O(1) / O(n) | O(1) / O(n) | O(n) |
| **Queue** | O(n) / O(n) | O(n) / O(n) | O(1) / O(1) | O(1) / O(1) | O(n) |
| **Deque** | O(n) / O(n) | O(n) / O(n) | O(1) / O(1) | O(1) / O(1) | O(n) |
| **Multiset** | N/A | O(1) / O(n) | O(1) / O(n) | O(1) / O(n) | O(n) |

*\*Note: Insertion and deletion operations at the extreme structural head or tail of a Linked List are O(1). If you have to find a specific node coordinate in the middle of the chain first, the structural lookup phase requires O(n) time.*
