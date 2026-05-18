# 007 — Expressions

## 1. Definition and Core Concept

In Java, an **expression** is a construct made up of variables, operators, and method invocations, which are constructed according to the syntax of the language, that evaluates to a single value. 

Think of an expression as a piece of code that answers a question and produces a result.

### Statements vs. Expressions
* **Expression:** Evaluates to a value. (e.g., `5 + 3`, `Math.max(a, b)`, `x == 10`)
* **Statement:** Forms a complete unit of execution, representing an action. An expression becomes a statement when it is terminated with a semicolon `;`. (e.g., `int y = 5 + 3;`)

---

## 2. Code Examples

### Types of Expressions

```java
public class ExpressionDemo {
    public static void main(String[] args) {
        
        // 1. Arithmetic Expression (evaluates to a numeric value)
        int sum = 5 + 10 * 2; // The expression is "5 + 10 * 2", which evaluates to 25
        
        // 2. Relational / Boolean Expression (evaluates to true or false)
        int age = 20;
        boolean isAdult = age >= 18; // The expression "age >= 18" evaluates to true
        
        // 3. String Expression (evaluates to a String object)
        String firstName = "Tech";
        String fullName = firstName + "tonics"; // Evaluates to "Techtonics"
        
        // 4. Method Invocation Expression
        int max = Math.max(10, 20); // Evaluates to 20
        
        // 5. Assignment Expression
        // Assignment itself is an expression that evaluates to the assigned value
        int x, y;
        x = (y = 5); // (y = 5) evaluates to 5, which is then assigned to x. Both equal 5.
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Side Effects in Expressions:** Using increment (`++`) or decrement (`--`) operators inside complex expressions can lead to highly unreadable code and unexpected results due to the difference between pre-increment and post-increment.
  ```java
  int x = 5;
  int result = x++ + ++x; // AVOID THIS! It is terrible practice and leads to bugs.
  ```
* **Confusing Assignment (`=`) with Equality (`==`):**
  ```java
  boolean isReady = false;
  // Mistake: This actually assigns true to isReady, and evaluates to true!
  if (isReady = true) { 
      System.out.println("Ready!");
  }
  ```

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be prepared to evaluate complex arithmetic and boolean expressions by hand. Always remember that assignments evaluate to the assigned value, which is why chained assignments like `a = b = c = 0;` work perfectly in Java.

* **Takeaway 1:** Every expression evaluates to exactly one value of a specific data type.
* **Takeaway 2:** A method call is only an expression if it has a return type. If a method returns `void`, it cannot be used as an expression (e.g., `int x = printMessage();` is invalid).
