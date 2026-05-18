# 003 — Data Types in Java

## 1. Definition and Core Concept

In Java, every variable must have a declared **data type**. A data type determines the values that a variable can contain, plus the operations that can be performed on it. Java is a **statically-typed** and **strongly-typed** language, meaning all variables must be declared before they can be used, and type mismatches are strictly caught by the compiler.

Java data types are divided into two main categories:
1. **Primitive Data Types** (The basic building blocks)
2. **Non-Primitive / Reference Data Types** (Objects and Arrays)

### Primitive Data Types (8 types)
Primitives are predefined by the language and are named with a lowercase letter. They hold raw values directly in memory (on the stack).

| Data Type | Size | Description / Range | Default Value |
| :--- | :--- | :--- | :--- |
| `byte` | 1 byte | -128 to 127 | 0 |
| `short` | 2 bytes | -32,768 to 32,767 | 0 |
| `int` | 4 bytes | ~ -2 billion to 2 billion | 0 |
| `long` | 8 bytes | Extremely large integers | 0L |
| `float` | 4 bytes | Floating-point (up to 7 decimal digits) | 0.0f |
| `double` | 8 bytes | Floating-point (up to 16 decimal digits) | 0.0d |
| `boolean` | 1 bit | `true` or `false` | false |
| `char` | 2 bytes | Single 16-bit Unicode character | '\u0000' |

### Reference Data Types
Reference types hold memory addresses (references) pointing to objects stored on the heap. Examples include `String`, `Arrays`, `Classes`, and `Interfaces`. Their default value is `null`.

---

## 2. Code Examples

```java
public class DataTypeExamples {
    public static void main(String[] args) {
        // Primitives
        byte age = 25;
        int population = 800000000;
        long distanceToStar = 9876543210L; // 'L' suffix is required for longs out of int range
        
        float pi = 3.14f; // 'f' suffix is required for float
        double price = 19.99;
        
        boolean isJavaFun = true;
        char grade = 'A'; // Single quotes for char

        // Reference Data Type
        String name = "Techtonics"; // Double quotes for String
        int[] scores = {95, 88, 92};
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Forgetting the `f` suffix on floats:** Writing `float f = 3.14;` causes a compilation error because Java treats decimal literals as `double` by default. You MUST write `3.14f`.
* **Forgetting the `L` suffix on longs:** Writing `long l = 3000000000;` throws an error because the number is too big for an `int`, and Java parses literals as `int` by default. Use `3000000000L`.
* **String vs Char:** Confusing `'A'` (a primitive char) with `"A"` (a String object). They are entirely different data types.

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Memorize the size in bytes of the primitives (especially `int` is 4, `double` is 8) and their default values (specifically that reference types default to `null`).

* **Takeaway 1:** `int` and `double` are the standard go-to primitives for whole numbers and decimals, respectively. 
* **Takeaway 2:** Primitive types are not objects. You cannot call methods on an `int`. (e.g., `age.toString()` will not compile). Java provides "Wrapper Classes" (like `Integer`) for when you need object behavior.
