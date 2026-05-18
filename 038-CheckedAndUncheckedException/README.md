# 038 — Checked and Unchecked Exceptions

## 1. Definition and Core Concept

Within the `java.lang.Exception` branch of the Throwable hierarchy, Java divides exceptions into two distinct categories: **Checked** and **Unchecked**. This distinction is one of Java's most unique (and controversial) features.

### 1. Checked Exceptions (Compile-time Checked)
These are exceptions that the Java compiler *forces* you to handle. If you write code that might throw a Checked Exception, the code will literally fail to compile unless you surround it with a `try-catch` block or declare it in a `throws` clause.
* **What they represent:** External factors outside the program's control (e.g., File I/O, Network connections, Database connections).
* **Where they live:** Any class that inherits from `Exception` (EXCEPT for `RuntimeException`).
* **Examples:** `IOException`, `SQLException`, `FileNotFoundException`.

### 2. Unchecked Exceptions (Runtime Exceptions)
These are exceptions that the compiler does *not* force you to handle. They occur at runtime.
* **What they represent:** Programming mistakes or logical bugs (e.g., dividing by zero, accessing a null object, going out of array bounds).
* **Where they live:** Any class that inherits from `RuntimeException`.
* **Examples:** `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException`.

---

## 2. Code Examples

### Checked Exception (Forced Handling)
```java
import java.io.FileReader;
import java.io.FileNotFoundException;

public class CheckedDemo {
    public static void main(String[] args) {
        // FileReader throws a Checked Exception (FileNotFoundException)
        // If we don't put this in a try-catch, it will NOT COMPILE.
        
        try {
            FileReader file = new FileReader("missing_data.txt");
        } catch (FileNotFoundException e) {
            System.out.println("File was not found! Please check the path.");
        }
    }
}
```

### Unchecked Exception (Optional Handling)
```java
public class UncheckedDemo {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3};
        
        // This will throw an ArrayIndexOutOfBoundsException (Unchecked).
        // The compiler does NOT force us to put this in a try-catch.
        // It will compile perfectly, but crash at runtime.
        System.out.println(arr[5]); 
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Using Try-Catch for Unchecked Exceptions:** While you *can* catch a `NullPointerException`, it is considered bad practice. Instead of catching it, you should fix the underlying logical bug by adding an `if (object != null)` check before using it. Unchecked exceptions usually indicate your code is flawed.
* **"Swallowing" Checked Exceptions:** To get the compiler to shut up, beginners sometimes write an empty catch block: `catch(IOException e) {}`. This is a terrible idea. If the file fails to open, the program silently ignores it and continues running, likely crashing worse later on.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions will show you code that throws an `IOException` without a `try-catch` block and ask for the output. The answer is **Compile Error**. If the code throws an `ArithmeticException` without a `try-catch`, the answer is **Runtime Exception**.

* **Takeaway 1:** Checked = Compiler forces you to handle it. Unchecked = Compiler ignores it.
* **Takeaway 2:** `RuntimeException` and all of its subclasses are Unchecked. Everything else under `Exception` is Checked.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
