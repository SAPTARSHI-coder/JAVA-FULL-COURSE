# 020 — Methods

## 1. Definition and Core Concept

A **method** is a block of code which only runs when it is called. You can pass data, known as parameters, into a method. Methods are used to perform certain actions, and they are also known as functions (though in Java, because they always belong to a class, they are exclusively called methods).

Methods are the foundation of code reusability. Instead of writing the same 20 lines of code in 5 different places, you write it once inside a method, and call that method 5 times.

### Method Signature Components
`[access_modifier] [static/non-static] returnType methodName(parameter_list) { ... }`

* **Access Modifier:** Defines who can call the method (`public`, `private`, etc.).
* **Return Type:** The data type the method gives back. Use `void` if it returns nothing.
* **Method Name:** Should be a verb, written in `camelCase`.
* **Parameters:** Variables passed into the method to act upon.

---

## 2. Code Examples

### A Method that Returns a Value
```java
public class Calculator {
    
    // Method declaration
    // public: anyone can call it
    // int: it will return an integer result
    public int addNumbers(int a, int b) {
        int sum = a + b;
        return sum; // The 'return' keyword sends data back to the caller
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        // Method invocation
        int result = calc.addNumbers(10, 25);
        System.out.println("Result: " + result); // 35
    }
}
```

### A Method that Returns Nothing (`void`)
```java
public class Printer {
    
    // Uses 'void' because it performs an action, but gives no data back
    public void printWelcomeMessage(String name) {
        System.out.println("Welcome to the system, " + name + "!");
        // No return statement is needed (though 'return;' is allowed to exit early)
    }

    public static void main(String[] args) {
        Printer p = new Printer();
        p.printWelcomeMessage("Alice"); 
        // String x = p.printWelcomeMessage("Alice"); // COMPILE ERROR! Cannot assign void.
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Missing Return Statement:** If you define a return type (e.g., `int`), you MUST return an integer under all possible execution paths. 
  ```java
  public int checkNumber(int x) {
      if (x > 0) {
          return 1;
      }
      // ERROR: What if x is less than 0? The compiler will fail here.
  }
  ```
* **Calling non-static methods from static contexts:** You cannot call an instance method directly from `public static void main` without first creating an object using `new`.

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be able to trace method calls, especially when a method calls another method. Pay close attention to what type of data is being returned, and ensure the caller is storing it in a matching variable type.

* **Takeaway 1:** A method signature consists strictly of the method's name and its parameter list (types and order). It does *not* include the return type.
* **Takeaway 2:** When a `return` statement is executed, the method instantly terminates. Any code written beneath a `return` statement in the same block is considered "unreachable code".

---

## ⚔️ Java vs C++ (Key Differences)

> **Java methods must be inside a class and are virtually dispatched by default. C++ functions can exist outside classes, and class methods are non-virtual by default.**
