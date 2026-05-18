# 009 — Type Casting

## 1. Definition and Core Concept

**Type Casting** is the process of converting a value from one data type to another. In Java, casting falls into two main categories:

### 1. Widening Casting (Implicit)
Happens automatically when you convert a smaller primitive type to a larger primitive type. Because there is no risk of data loss, the Java compiler handles it for you.
* **Order:** `byte` -> `short` -> `char` -> `int` -> `long` -> `float` -> `double`

### 2. Narrowing Casting (Explicit)
Happens when you convert a larger primitive type to a smaller one. Because this can result in data loss (e.g., losing decimal points or overflowing), Java forces you to do it manually by placing the target type in parentheses `()`.
* **Order:** `double` -> `float` -> `long` -> `int` -> `char` -> `short` -> `byte`

---

## 2. Code Examples

### Widening (Automatic)
```java
public class WideningDemo {
    public static void main(String[] args) {
        int myInt = 9;
        // Automatic casting: int to double
        double myDouble = myInt; 

        System.out.println(myInt);      // Outputs 9
        System.out.println(myDouble);   // Outputs 9.0
    }
}
```

### Narrowing (Manual)
```java
public class NarrowingDemo {
    public static void main(String[] args) {
        double myDouble = 9.78d;
        // Manual casting: double to int
        int myInt = (int) myDouble; 

        System.out.println(myDouble);   // Outputs 9.78
        System.out.println(myInt);      // Outputs 9 (Decimal portion is truncated, NOT rounded)
    }
}
```

### Char to Int
```java
public class CharCast {
    public static void main(String[] args) {
        char letter = 'A';
        int asciiValue = letter; // Widening (char to int)
        System.out.println(asciiValue); // Outputs 65
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Assuming truncation rounds the number:** Narrowing from `double` to `int` strictly chops off the decimal. `(int) 9.99` becomes `9`, not `10`. To round, use `Math.round()`.
* **Data Overflow during Narrowing:** If you cast an `int` that is larger than 127 into a `byte`, the value wraps around into negative numbers due to binary overflow.
  ```java
  int bigNum = 130;
  byte smallNum = (byte) bigNum; // Results in -126
  ```
* **Dividing Integers:** Integer division ignores decimals *before* you can cast it.
  ```java
  double result = 5 / 2;       // result is 2.0
  double fixed = (double) 5 / 2; // fixed is 2.5
  ```

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be very careful with math operations involving `byte` and `short`. Java automatically promotes `byte` and `short` operands to `int` when performing arithmetic! 

* **Takeaway 1:** `byte a = 10; byte b = 20; byte c = (byte)(a + b);` The manual cast is required because `a + b` evaluates to an `int`.
* **Takeaway 2:** Booleans cannot be cast to any other primitive type in Java, and no primitive type can be cast to boolean.
