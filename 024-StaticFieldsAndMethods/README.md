# 024 — Static Fields and Methods

## 1. Definition and Core Concept

In Java, the `static` keyword means that a field or method belongs to the **Class itself**, rather than to any specific *instance* (object) of that class.

* **Static Fields (Class Variables):** There is only ONE copy of a static variable in memory, regardless of how many objects of the class are created. It is shared across all instances.
* **Static Methods:** A method that can be called without creating an object of the class. Utility methods (like `Math.pow()`) are typically static.

---

## 2. Code Examples

### Static Variables
```java
class Employee {
    String name;          // Instance variable (Unique to each employee)
    static String companyName = "Techtonics"; // Shared by all employees

    public Employee(String name) {
        this.name = name;
    }
}

public class StaticFieldDemo {
    public static void main(String[] args) {
        Employee e1 = new Employee("Alice");
        Employee e2 = new Employee("Bob");
        
        System.out.println(e1.companyName); // Outputs: Techtonics
        
        // Changing it using the class name (Best Practice)
        Employee.companyName = "GlobalCorp";
        
        // Both objects see the new value because it's shared in memory
        System.out.println(e1.companyName); // GlobalCorp
        System.out.println(e2.companyName); // GlobalCorp
    }
}
```

### Static Methods
```java
class Calculator {
    // A static method
    public static int add(int a, int b) {
        return a + b;
    }
}

public class StaticMethodDemo {
    public static void main(String[] args) {
        // We do NOT need to write: Calculator calc = new Calculator();
        // We call it directly using the Class name:
        int sum = Calculator.add(10, 20);
        System.out.println(sum);
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Calling Instance variables from a Static Method:** A static method has no idea which object it belongs to (since it belongs to the class). Therefore, it cannot access non-static variables or non-static methods directly.
  ```java
  class Test {
      int count = 0;
      
      public static void printCount() {
          // System.out.println(count); // COMPILE ERROR! Cannot make a static reference to the non-static field count.
      }
  }
  ```
* **Overusing Static:** Creating "God Classes" full of static variables and methods turns your Java code into Procedural code, ruining the benefits of Object-Oriented design, encapsulation, and testing.

---

## 4. Exam Tips and Key Takeaways

> [!IMPORTANT]
> **Exam Focus:** Know the rules of static contexts perfectly: 
> 1. Static methods CANNOT use the `this` or `super` keywords.
> 2. Static methods CAN access other static members directly.
> 3. Instance (non-static) methods CAN access both static and non-static members.

* **Takeaway 1:** `public static void main` is static because the JVM needs to run it immediately when the program starts, before any objects have been created.
* **Takeaway 2:** Access static fields via the Class name (e.g., `Math.PI`), not via an object instance (e.g., `myMath.PI`), though the latter technically compiles with a warning.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java accesses static members via `ClassName.member`, whereas C++ uses the scope resolution operator `ClassName::member`.**
