# 019 — The String Class

## 1. Definition and Core Concept

In Java, a `String` is an object that represents a sequence of characters. It is arguably the most heavily used class in all of Java programming. 

Two critical concepts define the `String` class:
1. **Immutability:** Once a `String` object is created, its state cannot be altered. If you perform an operation that seems to alter the string (like making it uppercase), Java actually creates a brand new `String` object in memory and returns it.
2. **The String Pool:** To conserve memory, Java stores all literal strings in a special memory area called the "String Constant Pool". If you create two String literals with the exact same text, Java will point both variables to the exact same object in the pool.

---

## 2. Code Examples

### Creation and the String Pool
```java
public class StringPoolDemo {
    public static void main(String[] args) {
        // Created using a Literal (Goes into the String Pool)
        String s1 = "Hello";
        String s2 = "Hello"; // Re-uses the object from the pool!
        
        System.out.println(s1 == s2); // true (same memory address)

        // Created using 'new' keyword (Forces a new object on the Heap, ignores pool)
        String s3 = new String("Hello");
        
        System.out.println(s1 == s3); // false (different memory addresses)
        
        // Proper way to compare text content
        System.out.println(s1.equals(s3)); // true (contents are identical)
    }
}
```

### Essential String Methods
```java
public class StringMethods {
    public static void main(String[] args) {
        String text = " Java Programming ";

        // 1. Length
        System.out.println(text.length()); // 18
        
        // 2. Character at index
        System.out.println(text.charAt(2)); // 'a'
        
        // 3. Substring (start inclusive, end exclusive)
        System.out.println(text.substring(6, 13)); // "Program"
        
        // 4. Transform (Returns a NEW string!)
        String upper = text.toUpperCase(); 
        
        // 5. Trim (removes leading/trailing whitespace)
        String cleanText = text.trim(); // "Java Programming"
        
        // 6. Searching
        System.out.println(cleanText.indexOf("Pro")); // 5
        System.out.println(cleanText.contains("Java")); // true
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Comparing strings with `==`:** The `==` operator checks if two references point to the exact same object in memory. Because Strings can be created outside the pool using `new`, two Strings with the text `"Java"` might not be the same object. **ALWAYS use `.equals()` to compare String text.**
* **Ignoring Immutability:** 
  ```java
  String name = "alice";
  name.toUpperCase(); 
  System.out.println(name); // Still prints "alice"!!!
  ```
  **Fix:** You must reassign the result: `name = name.toUpperCase();`

---

## 4. Exam Tips and Key Takeaways

> [!IMPORTANT]
> **Exam Focus:** Be absolutely certain you know the difference between `==` and `.equals()` for Strings. Exam scenarios love to use `new String("text")` to force a false result on a `==` check.

* **Takeaway 1:** Strings are zero-indexed, just like arrays.
* **Takeaway 2:** Because Strings are immutable, they are inherently thread-safe and excellent to use as keys in a `HashMap`.
---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
