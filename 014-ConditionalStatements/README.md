# Java Study Guide: 014 - Conditional Statements

## 1. Introduction to Conditional Statements
In Java, **Conditional Statements** (also known as Decision-Making Statements) allow a program to execute specific blocks of code based on whether a condition is `true` or `false`. Without these, code would simply run line-by-line from top to bottom.

In Java, conditions must always evaluate to a **boolean** value (`true` or `false`).

---

## 2. The `if` Statement
The `if` statement is the most basic control flow statement. It executes a block of code only if the specified condition is true.

### Syntax:
```java
if (condition) {
    // block of code to be executed if condition is true
}
```

### Example:
```java
int speed = 80;
if (speed > 70) {
    System.out.println("Slow down! You are speeding.");
}
```

---

## 3. The `if-else` Statement
The `if-else` statement provides an alternative path. If the `if` condition is false, the `else` block executes.

### Syntax:
```java
if (condition) {
    // executes if condition is true
} else {
    // executes if condition is false
}
```

### Example:
```java
int age = 16;
if (age >= 18) {
    System.out.println("You can vote.");
} else {
    System.out.println("You are too young to vote.");
}
```

---

## 4. The `if-else-if` Ladder
Used when you have multiple conditions to check in sequence. Once a condition is met, the remaining blocks are skipped.

### Example:
```java
int score = 85;

if (score >= 90) {
    System.out.println("Grade: A");
} else if (score >= 80) {
    System.out.println("Grade: B"); // This will execute
} else if (score >= 70) {
    System.out.println("Grade: C");
} else {
    System.out.println("Grade: F");
}
```

---

## 5. Nested `if` Statements
You can place an `if` statement inside another `if` statement. This is useful for complex logic.

### Example:
```java
int num = 10;
if (num > 0) {
    if (num % 2 == 0) {
        System.out.println("Positive Even Number");
    }
}
```

---

## 6. The Ternary Operator (`? :`)
The ternary operator is a shorthand for `if-else`. It is the only operator in Java that takes three operands.

### Syntax:
`variable = (condition) ? expressionTrue : expressionFalse;`

### Example:
```java
int time = 20;
String result = (time < 18) ? "Good day." : "Good evening.";
System.out.println(result); // Outputs "Good evening."
```

---

## 7. The `switch` Statement
The `switch` statement selects one of many code blocks to be executed. It is often more readable than a long `if-else-if` ladder.

### Supported Types:
A `switch` works with:
*   `byte`, `short`, `char`, `int` (and their Wrapper classes).
*   `String` (since Java 7).
*   `enum` types.
*   *Note: `long`, `float`, and `double` are NOT allowed.*

### Syntax:
```java
switch (expression) {
    case value1:
        // code
        break; 
    case value2:
        // code
        break;
    default:
        // code
}
```

### Key Keywords:
1.  **`break`**: Terminates the switch block. Without it, execution "falls through" to the next case.
2.  **`default`**: Executes if no case matches. It is optional but recommended.

---

## 8. Common Mistakes and Pitfalls

### 1. Using `=` instead of `==`
The assignment operator (`=`) is often confused with the equality operator (`==`).
```java
boolean b = false;
if (b = true) { // This ASSIGNS true to b, and the condition becomes true!
    System.out.println("This will print!");
}
```
*Exam Tip: If the variable inside the `if` is a boolean, the assignment is valid Java but usually a logic error.*

### 2. Missing Braces `{}`
If you omit braces, only the **immediately following line** is part of the `if` block.
```java
if (score > 50)
    System.out.println("You passed");
    System.out.println("Congratulations!"); // This line runs REGARDLESS of score
```

### 3. Switch Fall-through
Forgetting a `break` statement causes the program to execute all subsequent cases until a `break` or the end of the switch is reached.
```java
int day = 1;
switch(day) {
    case 1: System.out.print("Mon ");
    case 2: System.out.print("Tue ");
    default: System.out.print("End");
}
// Output: Mon Tue End (because breaks are missing)
```

### 4. Floating Point in Switch
You cannot switch on a `double` or `float`.
```java
double d = 1.0;
switch(d) { // COMPILE ERROR
    case 1.0: ...
}
```

---

## 9. Exam Tips and Key Takeaways

*   **Boolean Only:** In Java, `if(1)` or `if(0)` results in a compilation error. Conditions must be `boolean`.
*   **The `default` Case:** In a `switch`, the `default` block does not have to be at the end, though it is best practice. If it's in the middle and lacks a `break`, it will also fall through.
*   **Case Constants:** Values in `case` statements must be **compile-time constants** (literals or `final` variables).
*   **Dangling Else:** An `else` always belongs to the closest unclosed `if` statement unless braces are used to specify otherwise.
*   **Ternary Types:** The two expressions in a ternary operator must return compatible types that can be assigned to the target variable.

### Summary Table
| Feature | `if-else` | `switch` |
| :--- | :--- | :--- |
| **Condition Type** | Any boolean expression | Specific types (int, String, etc.) |
| **Comparison** | Relational (`>`, `<`) & Logical | Equality (`==`) only |
| **Readability** | Better for ranges | Better for multiple fixed values |
| **Fall-through** | No | Yes (if `break` is missing) |

---

## ⚔️ Java vs C++ (Key Differences)

> **Java's if statement requires a strict oolean expression. C++ allows integers or pointers in if statements (where non-zero/non-null is true).**
