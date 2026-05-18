# 022 — Method Overloading

## 1. Definition and Core Concept

**Method Overloading** is a feature in Java that allows a class to have more than one method with the exact same name, as long as their parameter lists are different.

It is a form of compile-time (static) polymorphism. Java determines which method to execute by matching the method call to the method signature based on the number, type, and order of the arguments passed.

### Rules for Overloading
To overload a method, the parameter list MUST differ in at least one of these ways:
1. **Number of parameters** (e.g., `add(int a)` vs `add(int a, int b)`)
2. **Data type of parameters** (e.g., `add(int a)` vs `add(double a)`)
3. **Order of parameters** (e.g., `print(int a, String b)` vs `print(String a, int b)`)

*Note: Changing ONLY the return type is NOT enough to overload a method. It will cause a compile error.*

---

## 2. Code Examples

### Basic Overloading
```java
public class OverloadDemo {
    
    // Method 1: Two integer parameters
    public int multiply(int a, int b) {
        System.out.println("Executing int multiplication");
        return a * b;
    }

    // Method 2: Three integer parameters (Different number)
    public int multiply(int a, int b, int c) {
        return a * b * c;
    }

    // Method 3: Two double parameters (Different data types)
    public double multiply(double a, double b) {
        System.out.println("Executing double multiplication");
        return a * b;
    }

    public static void main(String[] args) {
        OverloadDemo demo = new OverloadDemo();
        
        System.out.println(demo.multiply(5, 5));       // Calls Method 1
        System.out.println(demo.multiply(5.5, 2.0));   // Calls Method 3
    }
}
```

### Type Promotion in Overloading
If Java cannot find an exact match for the parameters passed, it will try to "widen" (promote) the arguments to the next largest type.
```java
public class PromotionDemo {
    public void printNumber(double num) {
        System.out.println("Double: " + num);
    }
    
    public static void main(String[] args) {
        PromotionDemo p = new PromotionDemo();
        p.printNumber(5); // We pass an int (5), but it promotes to double (5.0) and works!
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Changing only the Return Type:** 
  ```java
  public int calculate() { return 1; }
  // public double calculate() { return 1.0; } // ERROR! Method calculate() is already defined!
  ```
  Java ignores the return type when checking for duplicates. The method signature must be unique.
* **Ambiguity Errors:** Occurs when Java cannot decide which overloaded method to pick because multiple methods match the arguments equally well after type promotion.
  ```java
  public void test(int a, double b) {}
  public void test(double a, int b) {}
  
  // test(5, 5); // ERROR: Ambiguous method call! Both methods are equally valid.
  ```

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** A very common exam question involves `System.out.println()`. The `println` method is heavily overloaded in the Java API so it can accept ints, doubles, strings, objects, etc., using the same method name.

* **Takeaway 1:** Overloading increases code readability (e.g., using `Math.abs()` instead of `Math.absInt()`, `Math.absDouble()`, etc.).
* **Takeaway 2:** Overloading happens at **compile-time**. The compiler decides exactly which method will run before the program even starts.
