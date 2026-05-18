# 042 — The `throws` Keyword

## 1. Definition and Core Concept

The **`throws`** keyword is used in a method signature to declare that the method *might* throw one or more exceptions during its execution. 

It is primarily used for **Checked Exceptions**. By adding `throws ExceptionName` to a method signature, you are telling the Java Compiler: 
*"Hey, this method is dangerous. It might crash. I am not going to handle the error here using a try-catch block. I am passing the responsibility of handling it up to whatever method calls me."*

This is also known as "Duck and Pass" or propagating the exception up the call stack.

---

## 2. Code Examples

### Without `throws` (The compiler complains)
```java
import java.io.FileReader;

public class ThrowsDemo {
    // This will NOT compile. FileReader throws a Checked Exception (FileNotFoundException).
    public void readFile() {
        FileReader fr = new FileReader("data.txt"); // Compile Error!
    }
}
```

### With `throws` (Passing the buck)
```java
import java.io.FileReader;
import java.io.FileNotFoundException;

public class ThrowsDemo {
    
    // 1. We declare that this method MIGHT throw the exception.
    // The compiler allows the code inside to compile without a try-catch.
    public void readFile() throws FileNotFoundException {
        FileReader fr = new FileReader("data.txt");
    }

    // 2. The caller method MUST now handle it!
    public static void main(String[] args) {
        ThrowsDemo demo = new ThrowsDemo();
        
        // demo.readFile(); // COMPILE ERROR! main() must now handle it!
        
        try {
            demo.readFile();
        } catch (FileNotFoundException e) {
            System.out.println("The file is missing!");
        }
    }
}
```

### Multiple Exceptions
You can declare multiple exceptions by separating them with commas.
```java
public void connectAndRead() throws IOException, SQLException {
    // Risky DB and File code here
}
```

---

## 3. Common Mistakes or Pitfalls

* **Using `throws` on `main()`:** Beginners sometimes add `throws Exception` to the `public static void main` method signature to avoid writing try-catch blocks entirely. 
  ```java
  public static void main(String[] args) throws Exception { ... }
  ```
  If an exception occurs here, it is passed to the JVM, which immediately crashes the application and prints a stack trace. This defeats the entire purpose of Exception Handling.
* **Confusing `throw` and `throws`:** 
  * `throw` (action verb) is used inside the method body to literally create and launch an exception object.
  * `throws` (descriptive verb) is used in the method signature to warn callers about potential risks.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** An exam might show a method that overrides a parent method. If the parent method does not declare `throws IOException`, the overriding child method **cannot** declare `throws IOException`. You cannot add new Checked Exceptions to an overridden method!

* **Takeaway 1:** `throws` is a warning label for methods.
* **Takeaway 2:** It is only strictly necessary to use `throws` for Checked Exceptions, though you are legally allowed to declare Unchecked Exceptions (like `RuntimeException`) for documentation purposes.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java enforces exception specifications via `throws` for checked exceptions. C++ deprecated its dynamic exception specifications (`throw()`) in C++11 in favor of `noexcept`.**
