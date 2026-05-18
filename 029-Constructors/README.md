# 029 — Constructors

## 1. Definition and Core Concept

A **Constructor** is a special block of code that is automatically called when an object is instantiated (created) using the `new` keyword.

Its primary purpose is to initialize the state (attributes) of the newly created object. For example, if you create a `BankAccount` object, you use the constructor to ensure it starts with an initial balance and an account holder's name before any other code can use it.

### Rules of Constructors
1. A constructor **MUST have the exact same name as the class**.
2. A constructor **CANNOT have a return type** (not even `void`). If you add `void`, Java treats it as a standard method, not a constructor.
3. Constructors can be overloaded (having multiple constructors with different parameters).

---

## 2. Code Examples

### 1. Default Constructor
If you do not write *any* constructor in your class, the Java compiler automatically inserts a hidden, no-argument "default constructor".
```java
public class User {
    String username;
    
    // We didn't write a constructor, but this is still valid:
    // User u = new User();
}
```

### 2. Parameterized Constructor
```java
public class BankAccount {
    String owner;
    double balance;
    
    // Parameterized Constructor
    public BankAccount(String ownerName, double initialBalance) {
        owner = ownerName;
        balance = initialBalance;
        System.out.println("Account created for " + owner);
    }
    
    public static void main(String[] args) {
        // The constructor is called instantly upon object creation
        BankAccount acc = new BankAccount("Alice", 500.0); 
    }
}
```

### 3. Constructor Overloading
```java
public class Box {
    int width, height, depth;
    
    // Constructor 1: A standard box
    public Box(int w, int h, int d) {
        width = w; height = h; depth = d;
    }
    
    // Constructor 2: A perfect cube
    public Box(int sideLength) {
        width = sideLength; 
        height = sideLength; 
        depth = sideLength;
    }
    
    public static void main(String[] args) {
        Box standard = new Box(10, 20, 30);
        Box cube = new Box(5); // Automatically calls Constructor 2
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **The "Lost" Default Constructor:** If you write *any* constructor yourself (e.g., a parameterized one), Java assumes you are taking full control and **removes** the free default constructor.
  ```java
  public class Dog {
      public Dog(String name) { } // We wrote a constructor
  }
  
  // Dog d = new Dog(); // COMPILE ERROR! The no-arg constructor no longer exists.
  ```
  **Fix:** If you still want to be able to create an object without arguments, you must explicitly write a no-argument constructor: `public Dog() { }`.
* **Adding a Return Type:** `public void Box()` is just a method named Box, it is NOT a constructor.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions often feature a class with a parameterized constructor, and then a line of code trying to instantiate the class using `new MyClass()`. This will fail to compile because the default constructor is gone.

* **Takeaway 1:** Constructors are invoked via the `new` keyword. You cannot call a constructor explicitly on an already-existing object.
* **Takeaway 2:** Constructors are not inherited by subclasses.

