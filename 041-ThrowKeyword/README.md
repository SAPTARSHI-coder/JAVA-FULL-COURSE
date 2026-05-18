# 041 — The `throw` Keyword

## 1. Definition and Core Concept

So far, we have looked at catching exceptions generated automatically by the JVM (like dividing by zero). But what if you want to generate an error yourself based on your own business logic?

The **`throw` keyword** is used to explicitly and manually trigger an exception from within a method. You literally create a new exception object and "throw" it at the JVM. 

### Why use `throw`?
To enforce validation. For example, if someone tries to create a `BankAccount` with a negative starting balance, the JVM won't crash (negative numbers are mathematically valid). However, logically, it breaks your business rules. You can use `throw` to generate an `IllegalArgumentException`.

---

## 2. Code Examples

### Basic Throw Example
```java
public class ThrowDemo {
    
    public static void checkAge(int age) {
        if (age < 18) {
            // Manually creating and throwing an exception object
            throw new IllegalArgumentException("Access Denied - You must be 18 or older.");
        } else {
            System.out.println("Access Granted!");
        }
    }

    public static void main(String[] args) {
        try {
            checkAge(15); 
        } catch (IllegalArgumentException e) {
            // We catch the exact exception we threw!
            System.out.println("Error: " + e.getMessage()); 
        }
    }
}
```

### Re-throwing an Exception
Sometimes a `catch` block catches an exception to log it, but then decides it cannot fully resolve the issue. It can re-throw the same exception to let a higher-level method handle it.
```java
public void processFile() {
    try {
        // risky code
    } catch (Exception e) {
        System.out.println("Logging error before passing it up...");
        throw e; // Re-throwing the exact same object
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Confusing `throw` with `throws`:** 
  * `throw` (no 's') is an action keyword used *inside* a method body to trigger a specific exception object.
  * `throws` (with an 's') is used in a method *signature* to declare that a method *might* throw an exception. (Covered in Topic 042).
* **Throwing Checked Exceptions without declaring them:** If you manually `throw new Exception("Error");` (which is a checked exception), the compiler will immediately yell at you unless your method signature includes `throws Exception` or you wrap the throw in a try-catch (which defeats the purpose of throwing it).

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be sure to note that `throw` requires an *instance* of a class. You must use the `new` keyword (e.g., `throw new RuntimeException();`). You cannot do `throw RuntimeException;`.

* **Takeaway 1:** `throw` is used by the programmer to manually break execution when custom validation rules fail.
* **Takeaway 2:** Any line of code immediately following a `throw` statement in the same block is unreachable code (a compile error), because `throw` instantly terminates the block.


---

## ⚔️ Java vs C++ (Key Differences)

> **Both use `throw` to throw an exception, but Java requires you to throw a `Throwable` object, while C++ can `throw` primitives (like `int` or `char*`).**
