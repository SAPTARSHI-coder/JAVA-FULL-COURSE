# 018 — Building Strings (`StringBuilder` and `StringBuffer`)

## 1. Definition and Core Concept

In Java, standard `String` objects are **immutable**, meaning once a String is created, its value cannot be changed. Whenever you "modify" a String (e.g., concatenating in a loop), Java is actually destroying the old String and creating a brand new one in memory. This is highly inefficient for heavy manipulation.

To solve this, Java provides two **mutable** classes specifically designed for building and modifying strings dynamically:

1. **`StringBuilder`:** Fast, mutable string class. Not thread-safe. (This is the go-to choice 99% of the time).
2. **`StringBuffer`:** Thread-safe (synchronized), mutable string class. Because of the synchronization overhead, it is slower than `StringBuilder`.

---

## 2. Code Examples

### The Inefficient Way (Avoid in loops)
```java
// BAD PRACTICE for heavy concatenation
String result = "";
for (int i = 0; i < 1000; i++) {
    result += i; // Creates 1000 new String objects in memory!
}
```

### The Efficient Way (`StringBuilder`)
```java
public class StringBuilderDemo {
    public static void main(String[] args) {
        
        // 1. Create a StringBuilder
        StringBuilder sb = new StringBuilder("Tech");
        
        // 2. append(): Add to the end
        sb.append("tonics");
        sb.append(" ").append(2026); // Method chaining
        
        // 3. insert(): Insert at a specific index
        sb.insert(4, "-"); // "Tech-tonics 2026"
        
        // 4. delete(): Remove characters
        sb.delete(4, 5); // Removes the '-' -> "Techtonics 2026"
        
        // 5. reverse(): Flips the string
        sb.reverse(); // "6202 scinotnceT"
        
        // 6. Convert back to an immutable String when finished!
        sb.reverse(); // Flip it back
        String finalResult = sb.toString();
        
        System.out.println(finalResult);
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Comparing with `.equals()`:** `StringBuilder` does NOT override the `.equals()` method from the `Object` class. This means it only checks memory addresses, not the actual text.
  ```java
  StringBuilder sb1 = new StringBuilder("Java");
  StringBuilder sb2 = new StringBuilder("Java");
  System.out.println(sb1.equals(sb2)); // Outputs FALSE!
  ```
  **Fix:** You must convert them to Strings first: `sb1.toString().equals(sb2.toString())`.
* **Using `StringBuffer` unnecessarily:** Unless you are explicitly writing multi-threaded code where multiple threads are modifying the exact same string concurrently, you should always use `StringBuilder`.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions love testing if you know that `StringBuilder` methods actually modify the object itself, rather than returning a new object. `sb.append("A")` changes `sb` forever. `str.concat("A")` does not change `str` unless reassigned.

* **Takeaway 1:** Use `StringBuilder` when you have to concatenate strings inside a loop.
* **Takeaway 2:** Method chaining works perfectly with `StringBuilder` because methods like `append` return `this` (a reference to the same builder object).

---

## ⚔️ Java vs C++ (Key Differences)

> **Java uses StringBuilder for mutable string operations to avoid memory overhead. In C++, std::string is mutable by default, so a separate builder class isn't strictly necessary.**
