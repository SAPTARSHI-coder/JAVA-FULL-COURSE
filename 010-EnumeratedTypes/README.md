# 010 — Enumerated Types (Enums)

## 1. Definition and Core Concept

An **enum** (short for enumeration) is a special "class" in Java that represents a group of fixed, unchangeable constants. 

When you have a variable that should only ever be one of a small set of predefined values (like days of the week, compass directions, or order statuses), you should use an enum rather than simple Strings or Integers. This provides **type safety** and prevents invalid values from being assigned.

Under the hood, Java enums are full-fledged classes. They can have attributes, methods, and constructors!

---

## 2. Code Examples

### Basic Enum Usage
```java
// Define the enum outside or inside a class
enum Level {
    LOW,
    MEDIUM,
    HIGH
}

public class EnumDemo {
    public static void main(String[] args) {
        // Assigning an enum value
        Level myVar = Level.MEDIUM; 
        
        // Enums work perfectly with Switch statements
        switch(myVar) {
            case LOW:
                System.out.println("Low level");
                break;
            case MEDIUM:
                System.out.println("Medium level");
                break;
            case HIGH:
                System.out.println("High level");
                break;
        }
    }
}
```

### Advanced Enum (With Fields and Methods)
```java
enum Size {
    SMALL("S"), 
    MEDIUM("M"), 
    LARGE("L"); // Semicolon required if methods/fields follow

    private final String abbreviation; // Field

    // Enum constructor (MUST be private or package-private)
    Size(String abbreviation) {
        this.abbreviation = abbreviation;
    }

    // Method
    public String getAbbreviation() {
        return this.abbreviation;
    }
}

public class AdvancedEnumDemo {
    public static void main(String[] args) {
        Size mySize = Size.LARGE;
        System.out.println("Size is: " + mySize + ", Abbr: " + mySize.getAbbreviation());
        
        // Loop through all enum values using .values()
        for (Size s : Size.values()) {
            System.out.println(s);
        }
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Comparing Enums with `.equals()`:** While you *can* use `.equals()`, it is safer and cleaner to compare enums using the `==` operator. Enums are singletons, meaning there is only one instance of `Level.LOW` in the entire JVM, so memory reference equality (`==`) works perfectly and avoids `NullPointerException`.
* **Public Constructors:** Trying to make an enum constructor `public` will cause a compile error. Enum constants are created internally when the class is loaded.

---

## 4. Exam Tips and Key Takeaways

> [!IMPORTANT]
> **Exam Focus:** Know the two highly tested built-in enum methods: `values()` which returns an array of all enum constants, and `valueOf(String)` which converts a string to an enum constant.

* **Takeaway 1:** Use enums when you know all possible values at compile time.
* **Takeaway 2:** Enums implicitly extend `java.lang.Enum`, meaning they cannot extend any other class (since Java doesn't support multiple inheritance), but they *can* implement interfaces.
---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
