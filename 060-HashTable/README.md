# 060 — HashTable

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
`Hashtable` is a **legacy** key-value collection (like `HashMap`) that is **synchronized** (thread-safe).

| Feature | HashMap | Hashtable |
|---------|---------|-----------|
| Thread-safe | ❌ | ✅ |
| Null keys | ✅ (one) | ❌ |
| Null values | ✅ | ❌ |
| Performance | Faster | Slower |
| Since | Java 1.2 | Java 1.0 (legacy) |

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Hashtable<String, Integer> ht = new Hashtable<>();

        // Adding key-value pairs
        ht.put("Alice", 90);
        ht.put("Bob", 85);
        ht.put("Charlie", 78);
        System.out.println(ht);

        // Accessing
        System.out.println(ht.get("Alice"));       // 90
        System.out.println(ht.containsKey("Bob")); // true
        System.out.println(ht.containsValue(78));  // true
        System.out.println(ht.size());             // 3

        // Updating
        ht.put("Bob", 95);  // overwrites
        System.out.println("Bob updated: " + ht.get("Bob"));

        // Removing
        ht.remove("Charlie");
        System.out.println(ht);

        // Iterating via Enumeration (legacy)
        Enumeration<String> keys = ht.keys();
        while (keys.hasMoreElements()) {
            String k = keys.nextElement();
            System.out.println(k + " = " + ht.get(k));
        }

        // Null key/value throws NullPointerException
        try {
            ht.put(null, 100);
        } catch (NullPointerException e) {
            System.out.println("Null key not allowed!");
        }
    }
}
```

**Output:**
```
{Charlie=78, Bob=85, Alice=90}
90
true
true
3
Bob updated: 95
{Bob=95, Alice=90}
Bob = 95
Alice = 90
Null key not allowed!
```

## 📝 Exam Tips
- `Hashtable` ≠ `HashMap` (note: Hashtable is one word, no capital T in middle)
- Hashtable: null key/value NOT allowed | HashMap: one null key allowed
- For modern thread-safe map: use `ConcurrentHashMap` instead
- Legacy iteration: `Enumeration` | Modern: `keySet()`, `entrySet()`

