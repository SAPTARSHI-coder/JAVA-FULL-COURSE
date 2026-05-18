# 059 — Vector

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
`Vector` is similar to `ArrayList` but is **thread-safe** (synchronized). All methods are synchronized, making it safe for multiple threads but **slower** than ArrayList.

It's a **legacy class** (from Java 1.0) — prefer `ArrayList` for single-threaded, `CopyOnWriteArrayList` for multi-threaded modern code.

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Vector<String> v = new Vector<>();

        // Adding
        v.add("Apple");
        v.add("Banana");
        v.addElement("Cherry");  // legacy method (same as add)
        v.add(1, "Mango");       // insert at index
        System.out.println(v);   // [Apple, Mango, Banana, Cherry]

        // Accessing
        System.out.println(v.get(0));          // Apple
        System.out.println(v.elementAt(0));    // Apple (legacy)
        System.out.println(v.firstElement());  // Apple
        System.out.println(v.lastElement());   // Cherry
        System.out.println(v.size());          // 4
        System.out.println(v.capacity());      // 10 (default, grows by 100%)

        // Removing
        v.remove("Mango");
        System.out.println(v);  // [Apple, Banana, Cherry]

        // Checking
        System.out.println(v.contains("Apple"));  // true
        System.out.println(v.indexOf("Banana"));  // 1

        // Iteration using Enumeration (legacy)
        Enumeration<String> e = v.elements();
        while (e.hasMoreElements()) {
            System.out.print(e.nextElement() + " ");
        }
    }
}
```

**Output:**
```
[Apple, Mango, Banana, Cherry]
Apple
Apple
Apple
Cherry
4
10
[Apple, Banana, Cherry]
true
1
Apple Banana Cherry
```

## 📝 Exam Tips
- Vector = synchronized ArrayList (thread-safe but slow)
- Grows by **doubling** capacity (ArrayList grows by 50%)
- Legacy methods: `addElement()`, `elementAt()`, `firstElement()`, `lastElement()`
- Modern preference: `ArrayList` (single-thread) or `Collections.synchronizedList(new ArrayList<>())` (multi-thread)

