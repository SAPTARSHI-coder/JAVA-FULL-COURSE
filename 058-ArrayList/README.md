# 058 — ArrayList

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
`ArrayList` is a **resizable array** — it grows automatically as you add elements.  
Best for: **random access** (get by index), **iteration**.  
Slower for: frequent insert/delete in the middle.

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();

        // Adding
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");
        names.add(1, "Dave");   // insert at index 1
        System.out.println(names);  // [Alice, Dave, Bob, Charlie]

        // Accessing
        System.out.println(names.get(0));    // Alice
        System.out.println(names.size());    // 4

        // Updating
        names.set(2, "Eve");
        System.out.println(names);  // [Alice, Dave, Eve, Charlie]

        // Removing
        names.remove("Dave");         // by value
        names.remove(2);              // by index
        System.out.println(names);    // [Alice, Eve]

        // Checking
        System.out.println(names.contains("Alice"));  // true
        System.out.println(names.isEmpty());          // false

        // Iterating
        for (String name : names) {
            System.out.print(name + " ");
        }
        System.out.println();

        // Sorting
        ArrayList<Integer> nums = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5));
        Collections.sort(nums);
        System.out.println(nums);  // [1, 1, 3, 4, 5]

        // Convert to array
        Object[] arr = names.toArray();
        System.out.println(Arrays.toString(arr));
    }
}
```

**Output:**
```
[Alice, Dave, Bob, Charlie]
Alice
4
[Alice, Dave, Eve, Charlie]
[Alice, Eve]
true
false
Alice Eve
[1, 1, 3, 4, 5]
[Alice, Eve]
```

## 📝 Exam Tips
- `add(val)` → end | `add(index, val)` → insert
- `get(index)` → retrieve | `set(index, val)` → update
- `remove(index)` or `remove(Object)` → delete
- `size()` → count (not `length`!)
- `Collections.sort(list)` → sort | `Collections.reverse(list)` → reverse
- Initial capacity: 10 (grows by 50% when full)

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
