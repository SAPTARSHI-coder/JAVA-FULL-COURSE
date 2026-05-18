# 055 — Introduction to Collection Framework

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
The **Java Collections Framework (JCF)** is a set of classes and interfaces for storing and manipulating groups of objects.

**Why not just arrays?**
- Arrays are fixed size
- Arrays can't hold different types easily
- Arrays have no built-in search, sort, insert, delete helpers

**Key Interfaces hierarchy:**
```
Collection
    ├── List        (ordered, allows duplicates) → ArrayList, LinkedList, Vector
    ├── Set         (no duplicates) → HashSet, LinkedHashSet, TreeSet
    └── Queue       (FIFO) → LinkedList, PriorityQueue

Map (key-value pairs, not Collection) → HashMap, LinkedHashMap, TreeMap
```

## 💻 Quick Preview

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // List — ordered, allows duplicates
        List<String> list = new ArrayList<>();
        list.add("Alice");
        list.add("Bob");
        list.add("Alice");  // duplicate allowed
        System.out.println("List: " + list);

        // Set — no duplicates
        Set<String> set = new HashSet<>();
        set.add("Alice");
        set.add("Bob");
        set.add("Alice");  // ignored
        System.out.println("Set: " + set);

        // Map — key-value pairs
        Map<String, Integer> map = new HashMap<>();
        map.put("Alice", 90);
        map.put("Bob", 85);
        System.out.println("Map: " + map);
        System.out.println("Alice's score: " + map.get("Alice"));
    }
}
```

**Output:**
```
List: [Alice, Bob, Alice]
Set: [Bob, Alice]
Map: {Bob=85, Alice=90}
Alice's score: 90
```

## 📝 Exam Tips
- `List` → ordered + duplicates allowed
- `Set` → unordered + no duplicates
- `Map` → key-value, no duplicate keys
- All in `java.util` package
- `Collections` (with 's') = utility class with `sort()`, `reverse()`, `shuffle()` etc.

