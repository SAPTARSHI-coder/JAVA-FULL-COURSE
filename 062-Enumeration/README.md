# 062 — Enumeration

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
`Enumeration` is a **legacy interface** (Java 1.0) for iterating over elements of `Vector`, `Hashtable`, `Stack`.  
It's been mostly replaced by **`Iterator`** (Java 1.2), but still tested in exams.

| Feature | Enumeration | Iterator |
|---------|------------|---------|
| Since | Java 1.0 | Java 1.2 |
| Methods | `hasMoreElements()`, `nextElement()` | `hasNext()`, `next()`, `remove()` |
| Can remove? | ❌ No | ✅ Yes |
| Works with | Legacy classes | All Collection classes |

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Vector<String> v = new Vector<>();
        v.add("Apple");
        v.add("Banana");
        v.add("Cherry");

        // Enumeration — legacy iteration
        Enumeration<String> e = v.elements();
        System.out.print("Enumeration: ");
        while (e.hasMoreElements()) {
            System.out.print(e.nextElement() + " ");
        }
        System.out.println();

        // Hashtable enumeration
        Hashtable<String, Integer> ht = new Hashtable<>();
        ht.put("A", 1);
        ht.put("B", 2);
        ht.put("C", 3);

        Enumeration<String> keys = ht.keys();
        System.out.print("Keys: ");
        while (keys.hasMoreElements()) {
            System.out.print(keys.nextElement() + " ");
        }
        System.out.println();

        Enumeration<Integer> values = ht.elements();
        System.out.print("Values: ");
        while (values.hasMoreElements()) {
            System.out.print(values.nextElement() + " ");
        }
        System.out.println();

        // Modern equivalent — Iterator
        Iterator<String> it = v.iterator();
        System.out.print("Iterator: ");
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }
    }
}
```

**Output:**
```
Enumeration: Apple Banana Cherry
Keys: C B A
Values: 3 2 1
Iterator: Apple Banana Cherry
```

## 📝 Exam Tips
- `hasMoreElements()` → check | `nextElement()` → get next
- Enumeration cannot **remove** elements during iteration
- Used with: `Vector.elements()`, `Hashtable.keys()`, `Hashtable.elements()`
- Modern code: use `Iterator` or enhanced for-each loop

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
