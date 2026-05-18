# 005 — Scope and Lifetime of Variables

## 1. Definition and Core Concept

In Java, a variable's **scope** determines where in the code the variable is accessible (visible). Its **lifetime** refers to how long the variable exists in memory before it is destroyed by the garbage collector.

Variables in Java generally fall into three scope categories:

1. **Instance Variables (Object/Class Level Scope):**
   * Declared inside a class, but outside any method.
   * **Scope:** Visible to all non-static methods in the class.
   * **Lifetime:** Created when the object is instantiated (`new`) and destroyed when the object is destroyed.

2. **Class Variables (Static Scope):**
   * Declared inside a class with the `static` keyword.
   * **Scope:** Visible everywhere in the class.
   * **Lifetime:** Created when the program starts (class loads) and destroyed when the program ends.

3. **Local Variables (Method Scope):**
   * Declared inside a method, constructor, or code block.
   * **Scope:** Visible only within the specific method or block where they are declared.
   * **Lifetime:** Created when the method is called and immediately destroyed when the method completes execution.

---

## 2. Code Examples

```java
public class ScopeExample {
    
    // 1. Class Variable (Static)
    static int totalObjects = 0; 
    
    // 2. Instance Variable 
    String name; 

    public ScopeExample(String name) {
        this.name = name; // 'name' is in scope here
        totalObjects++;   // 'totalObjects' is in scope here
    }

    public void printInfo() {
        // 3. Local Variable
        int age = 25; 
        
        System.out.println(name + " is " + age);
    }
    
    public void anotherMethod() {
        // System.out.println(age); // ERROR: 'age' is out of scope here!
        System.out.println(name);   // Works fine, instance variable
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Shadowing:** If a local variable has the exact same name as an instance variable, the local variable "shadows" (hides) the instance variable. To access the instance variable, you must use the `this` keyword (e.g., `this.name = name`).
* **Using Local Variables Before Initialization:** Instance and static variables get default values (`0`, `null`, `false`). Local variables do NOT. Attempting to use a local variable before assigning it a value results in a compilation error.

---

## 4. Exam Tips and Key Takeaways

> [!IMPORTANT]
> **Exam Focus:** Be prepared to trace variable lifetimes. A common question involves calling a method repeatedly and asking for the output. If a variable is local, it resets every time. If it is static, it retains its value across calls.

* **Takeaway 1:** A variable's scope is strictly defined by the curly braces `{}` in which it was declared.
* **Takeaway 2:** To share data across multiple objects, use a `static` variable. To give each object its own data, use an instance variable. To do temporary calculations, use a local variable.
