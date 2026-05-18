# 063 — Iterator

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
`Iterator` is the modern way to loop through any `Collection`. It can also **safely remove** elements during iteration.

**Methods:**
- `hasNext()` → returns true if more elements
- `next()` → returns next element
- `remove()` → removes last element returned by `next()`

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>(
            Arrays.asList("Alice", "Bob", "Charlie", "Dave", "Eve")
        );

        // Basic iteration
        Iterator<String> it = list.iterator();
        System.out.print("All: ");
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }
        System.out.println();

        // Remove elements during iteration (safe way)
        // Remove names shorter than 4 chars
        Iterator<String> it2 = list.iterator();
        while (it2.hasNext()) {
            String name = it2.next();
            if (name.length() <= 3) {
                it2.remove();  // safe removal during iteration
            }
        }
        System.out.println("After removing short names: " + list);

        // ListIterator — can go forward AND backward
        ListIterator<String> lit = list.listIterator(list.size()); // start at end
        System.out.print("Reverse: ");
        while (lit.hasPrevious()) {
            System.out.print(lit.previous() + " ");
        }
        System.out.println();
    }
}
```

**Output:**
```
All: Alice Bob Charlie Dave Eve
After removing short names: [Alice, Charlie, Dave]
Reverse: Dave Charlie Alice
```

## ⚠️ Common Mistakes
- Modifying a collection with `list.remove()` inside a for-each loop → `ConcurrentModificationException`
- Always use `iterator.remove()` to safely remove during iteration

## 📝 Exam Tips
- `Iterator` = one-directional (forward only)
- `ListIterator` = bidirectional (forward + backward), only for `List`
- `for-each` internally uses Iterator
- `ConcurrentModificationException` → happens when you modify collection while iterating with for-each

