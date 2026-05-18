# 032 — Inheritance

## 1. Definition and Core Concept

**Inheritance** is one of the four pillars of Object-Oriented Programming (OOP). It is a mechanism by which one class (the Subclass / Child Class) acquires the properties (fields) and behaviors (methods) of another class (the Superclass / Parent Class).

Inheritance represents an **"IS-A" relationship**. 
*Example:* A `Car` **IS-A** `Vehicle`. Therefore, `Car` should inherit from `Vehicle`.

In Java, inheritance is implemented using the **`extends`** keyword.

### Key Rules of Java Inheritance
1. **Single Inheritance Only:** A Java class can only `extends` ONE parent class. Java does not support multiple inheritance of classes (to avoid the "Diamond Problem" of ambiguity).
2. **The Root Class:** Every class in Java automatically inherits from `java.lang.Object`, even if you don't explicitly type `extends Object`.
3. **What is NOT Inherited:** Constructors are not inherited. Private members (fields/methods) are not inherited (though they still exist in the parent part of the object, they are just inaccessible to the child).

---

## 2. Code Examples

### Basic Inheritance
```java
// Parent Class (Superclass)
public class Animal {
    String name;
    
    public void eat() {
        System.out.println(name + " is eating.");
    }
}

// Child Class (Subclass)
public class Dog extends Animal {
    // Dog inherits 'name' and 'eat()' from Animal!
    
    // It can also have its own unique methods
    public void bark() {
        System.out.println("Woof!");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.name = "Rex"; // Inherited property
        myDog.eat();        // Inherited method (Output: Rex is eating.)
        myDog.bark();       // Unique method (Output: Woof!)
    }
}
```

### The `super` Keyword
The `super` keyword is a reference variable used to refer to the immediate parent class object. It is most commonly used to call the parent's constructor or parent's overridden methods.
```java
public class Employee {
    double salary;
    
    public Employee(double salary) {
        this.salary = salary;
    }
}

public class Manager extends Employee {
    int bonus;
    
    public Manager(double salary, int bonus) {
        super(salary); // Calls the Employee constructor! Must be the first line.
        this.bonus = bonus;
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Forgetting `super()` in constructors:** If a parent class does not have a default (no-argument) constructor, the child class constructor will fail to compile unless you explicitly call `super(args)` on the very first line of the child constructor.
* **Attempting Multiple Inheritance:** Writing `class Child extends Parent1, Parent2` causes a strict compile error in Java. (Use Interfaces if you need multiple inheritance of behaviors).

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions often feature a subclass trying to access a `private` variable in the superclass. Remember, `private` means private to the class it was declared in! The subclass cannot access it directly.

* **Takeaway 1:** Inheritance establishes an "IS-A" relationship.
* **Takeaway 2:** Constructors are NEVER inherited. They are *invoked* via `super()`.

