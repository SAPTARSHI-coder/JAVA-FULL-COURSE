# 031 — Data Abstraction

## 1. Definition and Core Concept

**Abstraction** is one of the four pillars of OOP. It is the process of hiding the complex, underlying implementation details of a system and exposing only the essential, high-level features to the user.

*Analogy:* When you drive a car, you use the steering wheel and pedals (the abstract interface). You don't need to know how the fuel injector works or the complex thermodynamics of the engine (the implementation details) to drive the car.

### Abstraction vs Encapsulation
* **Encapsulation:** "Information Hiding" — hiding the *data* and restricting direct access to it.
* **Abstraction:** "Implementation Hiding" — hiding the *complexity* of how the code actually works, focusing on *what* the object does instead of *how* it does it.

In Java, Abstraction is achieved using **Abstract Classes** and **Interfaces**.

---

## 2. Achieving Abstraction with Abstract Classes

An `abstract` class is a restricted class that cannot be used to create objects. It exists solely to be inherited by other classes. An `abstract` method is a method that is declared without an implementation (without a body). The subclass MUST provide the implementation.

```java
// Abstract class (Cannot be instantiated with 'new')
abstract class Animal {
    // Abstract method (No body) - hides the complex implementation
    public abstract void makeSound();
    
    // Regular method
    public void sleep() {
        System.out.println("Zzz...");
    }
}

// Subclass provides the specific implementation
class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark! Bark!"); // The implementation detail
    }
}

public class AbstractionDemo {
    public static void main(String[] args) {
        // Animal a = new Animal(); // ERROR! Cannot instantiate an abstract class.
        
        Animal myDog = new Dog(); // Valid!
        myDog.makeSound(); // The user just knows it makes a sound, not how.
        myDog.sleep();
    }
}
```

---

## 3. Interfaces (100% Abstraction)

An `interface` is a completely abstract class that is used to group related methods with empty bodies. (Prior to Java 8, all methods in an interface were purely abstract).

```java
interface Engine {
    void start(); // Implicitly public abstract
    void stop();
}

class SportsCar implements Engine {
    public void start() {
        System.out.println("VROOM! Fuel injected, sparks fired.");
    }
    public void stop() {
        System.out.println("Brakes applied, engine cut.");
    }
}
```

---

## 4. Common Mistakes or Pitfalls

* **Instantiating an Abstract Class:** Trying to write `new AbstractClassName()`. The compiler will strictly prevent this. You must instantiate a concrete subclass.
* **Forgetting to override Abstract Methods:** If a class inherits from an abstract class or implements an interface, it MUST provide an implementation for every single abstract method. If it fails to do so, the subclass itself must also be declared `abstract`.

---

## 5. Exam Tips and Key Takeaways

> [!IMPORTANT]
> **Exam Focus:** Know that an abstract class can have constructors, even though it cannot be instantiated. These constructors are called when a subclass is instantiated (via `super()`). Interfaces cannot have constructors.

* **Takeaway 1:** Abstraction focuses on the design level (interfaces/abstract classes). Encapsulation focuses on the implementation level (private fields).
* **Takeaway 2:** A class can implement multiple interfaces, but it can only inherit from one abstract class.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
