# 034 — Polymorphism

## 1. Definition and Core Concept

**Polymorphism** (from Greek, meaning "many forms") is one of the four pillars of OOP. It describes the ability of a single interface or method to represent different underlying forms (data types or objects).

In Java, polymorphism allows us to perform a single action in different ways. It fundamentally relies on **Inheritance**.

### Two Types of Polymorphism:
1. **Compile-time Polymorphism (Static Binding):** Achieved via **Method Overloading** (Topic 022). The compiler decides which method runs based on parameters.
2. **Runtime Polymorphism (Dynamic Binding):** Achieved via **Method Overriding**. The JVM decides which method to run *while the program is running*, based on the actual object created in memory, not the reference variable type.

---

## 2. Code Examples (Runtime Polymorphism)

To achieve runtime polymorphism, you need three things:
1. Inheritance (A parent and child class).
2. Method Overriding (The child overrides a parent's method).
3. **Upcasting** (A parent reference variable holding a child object).

```java
// 1. Inheritance Setup
class Animal {
    public void makeSound() {
        System.out.println("Generic animal sound");
    }
}

class Dog extends Animal {
    // 2. Method Overriding
    @Override
    public void makeSound() {
        System.out.println("Woof");
    }
}

class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class PolymorphismDemo {
    public static void main(String[] args) {
        // 3. Upcasting (Parent reference, Child object)
        Animal myAnimal1 = new Dog();
        Animal myAnimal2 = new Cat();
        
        // Runtime Polymorphism in action!
        // The compiler sees 'Animal', but at runtime, the JVM looks at the heap 
        // and sees a Dog and a Cat, executing their specific overridden methods.
        myAnimal1.makeSound(); // Outputs: Woof
        myAnimal2.makeSound(); // Outputs: Meow
    }
}
```

### Why is this powerful?
Because you can write a method that handles *any* Animal, without knowing what specific animal it is!
```java
public void makeThemSpeak(Animal[] animals) {
    for(Animal a : animals) {
        a.makeSound(); // Will dynamically output woof, meow, moo, etc.
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Variable Hiding vs Method Overriding:** Only instance methods are polymorphic (dynamically bound). Variables and `static` methods are statically bound by the compiler based on the reference type.
  ```java
  class Parent { String name = "Parent"; }
  class Child extends Parent { String name = "Child"; }
  
  Parent p = new Child();
  System.out.println(p.name); // Outputs: "Parent". Variables DO NOT override!
  ```
* **Forgetting `@Override`:** If you misspell the method name in the child class (e.g., `makesound()` instead of `makeSound()`), you are creating a new method, not overriding. The `@Override` annotation forces the compiler to check for this error.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** An exam will give you `Animal a = new Dog();` and ask if you can call `a.fetch()`. If `fetch()` is only defined in `Dog` and NOT in `Animal`, this will cause a COMPILE ERROR. The compiler only knows about the reference type (`Animal`).

* **Takeaway 1:** Runtime polymorphism allows the same code to behave differently based on the actual object in memory.
* **Takeaway 2:** Fields (variables) cannot be overridden in Java, only methods can.

