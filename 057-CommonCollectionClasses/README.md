# 057 — Common Collection Classes Overview

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
A quick reference of the most used collection classes and when to use each.

| Class | Interface | Ordered? | Duplicates? | Thread-safe? | Use when |
|-------|-----------|---------|------------|-------------|---------|
| `ArrayList` | List | ✅ | ✅ | ❌ | Default list, fast read |
| `LinkedList` | List/Queue | ✅ | ✅ | ❌ | Frequent insert/delete |
| `Vector` | List | ✅ | ✅ | ✅ | Legacy thread-safe list |
| `Stack` | Stack | ✅ | ✅ | ✅ | LIFO stack |
| `HashSet` | Set | ❌ | ❌ | ❌ | Unique items, fast lookup |
| `LinkedHashSet` | Set | ✅ | ❌ | ❌ | Unique + insertion order |
| `TreeSet` | Set | ✅ sorted | ❌ | ❌ | Sorted unique items |
| `HashMap` | Map | ❌ | Keys: ❌ | ❌ | Fast key-value lookup |
| `LinkedHashMap` | Map | ✅ | Keys: ❌ | ❌ | Ordered key-value |
| `TreeMap` | Map | ✅ sorted | Keys: ❌ | ❌ | Sorted keys |

## 💻 Quick Comparison

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // ArrayList — fast access by index
        ArrayList<Integer> al = new ArrayList<>(Arrays.asList(3, 1, 2, 1));
        Collections.sort(al);
        System.out.println("ArrayList sorted: " + al);

        // HashSet — unique, unordered
        HashSet<Integer> hs = new HashSet<>(Arrays.asList(3, 1, 2, 1));
        System.out.println("HashSet (unique): " + hs);

        // TreeSet — unique, sorted
        TreeSet<Integer> ts = new TreeSet<>(Arrays.asList(3, 1, 2, 1));
        System.out.println("TreeSet (sorted): " + ts);

        // HashMap
        HashMap<String, Integer> hm = new HashMap<>();
        hm.put("C", 3); hm.put("A", 1); hm.put("B", 2);
        System.out.println("HashMap: " + hm);

        // TreeMap — sorted by key
        TreeMap<String, Integer> tm = new TreeMap<>(hm);
        System.out.println("TreeMap (sorted): " + tm);
    }
}
```

**Output:**
```
ArrayList sorted: [1, 1, 2, 3]
HashSet (unique): [1, 2, 3]
TreeSet (sorted): [1, 2, 3]
HashMap: {A=1, B=2, C=3}
TreeMap (sorted): {A=1, B=2, C=3}
```

## 📝 Exam Tips
- Need duplicates? → List | No duplicates? → Set
- Need key-value? → Map | Need sorted? → Tree variant
- Default choices: `ArrayList`, `HashSet`, `HashMap`

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
