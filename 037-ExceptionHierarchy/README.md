# 037 — Exception Hierarchy

## 1. Definition and Core Concept

In Java, every exception is an Object. Because they are objects, they all belong to a massive class hierarchy based on inheritance. 

At the very top of this hierarchy is the **`java.lang.Throwable`** class. Only objects that are instances of `Throwable` (or its subclasses) can be thrown using the `throw` keyword or caught in a `catch` block.

### The Two Main Branches of `Throwable`
`Throwable` splits immediately into two major subclasses:
1. **`java.lang.Error`:** Represents severe, unrecoverable problems that occur in the Java Virtual Machine (JVM) itself. Applications should *never* try to catch these.
2. **`java.lang.Exception`:** Represents conditions that a reasonable application might want to catch and recover from.

---

## 2. The Hierarchy Tree

Here is a simplified view of the Java Exception Hierarchy:

```text
                  Object
                    |
                Throwable
                /       \
            Error      Exception
            /   \          /       \
  OutOfMemoryError   IOException   RuntimeException
  StackOverflowError SQLException       |
                                  NullPointerException
                                  ArithmeticException
                                  IndexOutOfBoundsException
```

---

## 3. Errors vs. Exceptions

### 1. Errors (`java.lang.Error`)
Errors are catastrophic system failures. They happen outside the control of the application programmer.
* **Examples:** `OutOfMemoryError` (the JVM ran out of RAM), `StackOverflowError` (a recursive method went too deep).
* **Handling:** Do not catch them. Let the program crash. You cannot write code to magically create more RAM.

### 2. Exceptions (`java.lang.Exception`)
Exceptions are problems caused by the environment, the user, or logical bugs in the code.
* **Examples:** `FileNotFoundException` (the user deleted the file), `NullPointerException` (the programmer forgot to instantiate an object).
* **Handling:** You *should* catch and handle these to prevent the program from crashing.

---

## 4. Common Mistakes or Pitfalls

* **Catching `Throwable` or `Error`:** Beginners sometimes write `catch (Throwable t)` or `catch (Error e)`. This is incredibly dangerous because it catches JVM system failures (like `OutOfMemoryError`) and attempts to continue running the application in a corrupted state. **Always catch `Exception` instead.**
* **Not understanding the hierarchy in multiple catch blocks:** If you have multiple `catch` blocks, you MUST catch the most specific (child) exceptions first, and the most general (parent) exceptions last. (Covered more in Topic 040).

---

## 5. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Memorize that the root of the entire error-handling structure is `Throwable`, not `Exception`. `Exception` is just a child of `Throwable`.

* **Takeaway 1:** `Error` = JVM crashes. `Exception` = Application errors.
* **Takeaway 2:** Because of inheritance, a `catch(Exception e)` block will successfully catch a `NullPointerException`, an `IOException`, and any other class that extends `Exception`.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
