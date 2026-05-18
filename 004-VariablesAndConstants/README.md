# 004 — Variables and Constants

## 1. Definition and Core Concept

### Variables
A **variable** is a named memory location used to store data. Because the data stored can change during the program's execution, it is called "variable."
In Java, declaring a variable requires specifying its data type and its name.

**Syntax:** `dataType variableName = value;`

### Constants (`final` keyword)
A **constant** is a variable whose value cannot be changed once it has been assigned. In Java, constants are created using the `final` keyword. By convention, constant names are written in `ALL_CAPS` with words separated by underscores.

---

## 2. Code Examples

### Working with Variables
```java
public class VariableDemo {
    public static void main(String[] args) {
        // Declaration and initialization
        int score = 0;
        
        // The value can vary (change)
        score = 10; 
        score = score + 5; 
        
        System.out.println("Final Score: " + score); // Outputs 15
        
        // Multiple variables of the same type
        int x = 5, y = 10, z = 15;
    }
}
```

### Working with Constants
```java
public class ConstantDemo {
    public static void main(String[] args) {
        // Declaring a constant
        final double PI = 3.14159;
        final int MAX_USERS = 100;
        
        // PI = 3.14; // ERROR: Cannot assign a value to final variable PI
        
        System.out.println("Max users allowed: " + MAX_USERS);
    }
}
```

---

## 3. Variable Naming Rules (Identifiers)

To declare variables, you must follow Java's strict identifier rules:
1. Names can contain letters, digits, underscores (`_`), and dollar signs (`$`).
2. Names **must not** begin with a digit (e.g., `1stPlace` is invalid).
3. Names are case-sensitive (`myVar` and `myvar` are different).
4. Cannot use Java reserved keywords (like `class`, `int`, `public`).

**Best Practice:** Variables should use `camelCase` (e.g., `studentAge`), while constants should use `MACRO_CASE` (e.g., `MAX_SPEED`).

---

## 4. Common Mistakes or Pitfalls

* **Using uninitialized variables:** In Java, local variables (variables inside a method) are NOT given a default value. If you declare `int x;` and try to `System.out.println(x);` without assigning it first, the compiler will throw an error.
* **Trying to modify a `final` variable:** Reassigning a final variable causes a strict compile-time error.

---

## 5. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions love to show a snippet where a `final` variable is updated inside a loop or an `if` statement. Always look for the `final` keyword to spot invalid code.

* **Takeaway 1:** Use `final` whenever a variable represents a fixed configuration (like taxes, physics constants, URL paths). It improves code readability and safety.
* **Takeaway 2:** Remember that Java variables are strictly typed. You cannot assign a `"String"` to an `int` variable.
---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
