# 028 — Classes and Objects

## 1. Definition and Core Concept

Object-Oriented Programming (OOP) revolves around two fundamental concepts: **Classes** and **Objects**.

* **Class:** A class is a blueprint or template for creating objects. It defines the state (attributes/variables) and behaviors (methods) that the objects created from it will have. A class itself does not consume memory for data until an object is created.
* **Object:** An object is a concrete, physical instance of a class that exists in the computer's memory. It contains actual data. You can create multiple unique objects from a single class blueprint.

*Analogy:* The Class is the architectural blueprint for a house. The Object is the actual house built from that blueprint.

---

## 2. Code Examples

### 1. Defining a Class
```java
// The Blueprint
public class Car {
    
    // Attributes (State)
    String make;
    String color;
    int currentSpeed;
    
    // Methods (Behavior)
    public void accelerate(int amount) {
        currentSpeed += amount;
        System.out.println("The " + color + " " + make + " accelerates to " + currentSpeed + " mph.");
    }
    
    public void brake() {
        currentSpeed = 0;
        System.out.println("The " + make + " has stopped.");
    }
}
```

### 2. Creating and Using Objects
```java
public class Main {
    public static void main(String[] args) {
        
        // 1. Instantiating (creating) the first object
        Car car1 = new Car();
        car1.make = "Toyota"; // Giving data to the object's attributes
        car1.color = "Red";
        
        // 2. Instantiating a second, completely unique object
        Car car2 = new Car();
        car2.make = "Honda";
        car2.color = "Blue";
        
        // 3. Invoking behaviors
        car1.accelerate(50); // Output: The Red Toyota accelerates to 50 mph.
        car2.accelerate(30); // Output: The Blue Honda accelerates to 30 mph.
    }
}
```

---

## 3. How Objects Work in Memory

When you write `Car myCar = new Car();`, two things happen:
1. `new Car()`: The `new` keyword dynamically allocates a block of memory on the **Heap** for the object's data, initializes default values, and returns the memory address.
2. `Car myCar`: A reference variable named `myCar` is created on the **Stack**. This variable holds the memory address pointing to the object on the Heap.

If you write `Car car3 = car1;`, you are NOT creating a third car. You are creating a second reference variable that points to the exact same Red Toyota in memory.

---

## 4. Common Mistakes or Pitfalls

* **NullPointerException:** If you declare a reference variable but forget to use `new` to instantiate the object, the reference points to `null`. Attempting to call a method or access an attribute on `null` crashes the program.
  ```java
  Car ghostCar; // Points to null
  // ghostCar.accelerate(10); // CRASH! NullPointerException
  ```
* **Confusing Class Variables with Instance Variables:** If you make an attribute `static`, it belongs to the Class blueprint itself, not the objects. If `currentSpeed` was static, all cars in the world would share the exact same speed!

---

## 5. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be comfortable tracing object references. If an exam shows `objA = objB;`, remember that modifying `objA` will now also modify `objB` because they point to the identical object in the heap.

* **Takeaway 1:** A Class is a logical construct; an Object is a physical reality in memory.
* **Takeaway 2:** You use the dot operator (`.`) to access an object's fields and methods.

