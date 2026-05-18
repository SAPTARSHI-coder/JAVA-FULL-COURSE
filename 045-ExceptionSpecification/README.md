# 045 — Exception Specification (Method Signatures)

## 1. Definition and Core Concept

**Exception Specification** refers to the contract a method makes with the rest of the application regarding the exceptions it might throw. In Java, this is formally defined in the method signature using the `throws` keyword.

When a developer looks at your method signature, the exception specification tells them exactly what risks they are taking by calling your method, and what Checked Exceptions the compiler will force them to handle.

### The Contract of Overriding (Crucial Rule)
When a subclass overrides a method from a parent class (or implements an interface method), the subclass must adhere to the Exception Specification of the parent. It cannot suddenly declare that it throws *new, broader* checked exceptions.

---

## 2. Rules of Exception Specification in Overriding

If Parent Class method declares: `public void doWork() throws IOException`

The Child Class overriding method **CAN**:
1. Throw the exact same exception: `throws IOException`
2. Throw a *Subclass* of the exception: `throws FileNotFoundException`
3. Throw NO checked exceptions at all (it handled them internally).
4. Throw any Unchecked Exception (`RuntimeException`).

The Child Class overriding method **CANNOT**:
1. Throw a broader, more general checked exception (e.g., `throws Exception`).
2. Throw a completely new, unrelated checked exception (e.g., `throws SQLException`).

### Why? (The Logic)
Because of Polymorphism, external code might do this:
`Parent p = new Child();`
`p.doWork();`
The external code only prepared to catch `IOException` (because that's what `Parent` specified). If the `Child` was secretly allowed to throw a `SQLException`, the external code wouldn't be prepared to catch it, and the application would crash!

---

## 3. Code Examples

```java
import java.io.IOException;
import java.io.FileNotFoundException;
import java.sql.SQLException;

class Parent {
    public void processData() throws IOException {
        // Implementation
    }
}

class Child extends Parent {
    
    // VALID: FileNotFoundException is a narrower subclass of IOException
    @Override
    public void processData() throws FileNotFoundException { 
        // Implementation
    }
    
    /* 
    // INVALID: Cannot throw a broader exception than the parent
    @Override
    public void processData() throws Exception { } 
    */

    /*
    // INVALID: Cannot throw an unrelated checked exception
    @Override
    public void processData() throws SQLException { }
    */
    
    /*
    // VALID: You can always throw Unchecked Exceptions freely
    @Override
    public void processData() throws NullPointerException { }
    */
}
```

---

## 4. Exam Tips and Key Takeaways

> [!IMPORTANT]
> **Exam Focus:** Exception Specification rules during method overriding are heavily tested on Java certification exams. Memorize the rule: **"The overriding method can throw narrower exceptions, or no exceptions, but never broader or new checked exceptions."**

* **Takeaway 1:** The exception specification is your method's safety warning label.
* **Takeaway 2:** Unchecked exceptions (`RuntimeExceptions`) are entirely exempt from these overriding rules. You can add them or remove them at will.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java mandates declaring checked exceptions in the method signature (`throws ExceptionName`). C++ relies heavily on `noexcept` to simply indicate if a function will *not* throw.**
