# Java Control Flow: A Comprehensive Guide

Control flow statements allow you to break up the execution flow by employing decision-making, looping, and branching, enabling your program to conditionally execute particular blocks of code.

---

## 1. Selection Statements

Selection statements allow your program to choose different paths of execution based on the outcome of an expression.

### A. The `if-else` Statement
The `if` statement is the most basic control flow statement. It executes a block of code only if a specified `boolean` condition is true.

```java
int score = 85;

if (score >= 90) {
    System.out.println("Grade: A");
} else if (score >= 80) {
    System.out.println("Grade: B"); // This will execute
} else {
    System.out.println("Grade: C");
}
```

**Key Rule:** If you omit the curly braces `{ }`, only the **one immediate statement** following the `if` is considered part of the block.
```java
if (false) 
    System.out.println("This won't print");
    System.out.println("This WILL print!"); // This is outside the if
```

### B. The `switch` Statement
The `switch` statement compares a single variable against multiple possible values (cases).

**Supported Types:**
*   Primitive types: `byte`, `short`, `char`, `int`.
*   Wrapper classes: `Byte`, `Short`, `Character`, `Integer`.
*   `String` (since Java 7).
*   `Enums`.
*   *Note:* `long`, `float`, `double`, and `boolean` are **not** allowed.

```java
int day = 2;
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break; // Prevents fall-through
    default:
        System.out.println("Invalid day");
}
```

---

## 2. Iteration Statements (Loops)

Loops repeatedly execute a block of code as long as a condition remains true.

### A. `while` Loop
A "pre-test" loop. It checks the condition **before** executing the body.
```java
int count = 0;
while (count < 3) {
    System.out.println("Count: " + count);
    count++;
}
```

### B. `do-while` Loop
A "post-test" loop. It executes the body **at least once**, then checks the condition.
```java
int count = 5;
do {
    System.out.println("This prints once");
} while (count < 3);
```

### C. `for` Loop
Used when the number of iterations is known. It consists of three parts: initialization, condition, and update.
```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
// i is not accessible here (out of scope)
```

### D. Enhanced `for` Loop (For-Each)
Used exclusively to iterate through arrays or `Iterable` objects (like Lists).
```java
String[] names = {"Java", "Python", "C++"};
for (String name : names) {
    System.out.println(name);
}
```

---

## 3. Transfer Statements

Transfer statements redirect the flow of control to another part of your program.

### A. `break`
Exits the innermost loop or `switch` statement immediately.

### B. `continue`
Skips the current iteration of a loop and proceeds to the next one (re-evaluates the condition).

### C. Labeled Statements
You can label a loop to specify which loop a `break` or `continue` should apply to. This is common in nested loops.
```java
outerLoop: 
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        if (i == 2 && j == 2) {
            break outerLoop; // Exits both loops
        }
        System.out.println(i + " " + j);
    }
}
```

---

## 4. Common Mistakes and Pitfalls

1.  **Assignment vs. Comparison:**
    ```java
    boolean b = false;
    if (b = true) { // Trap: This is an assignment, not a comparison!
        // This block WILL execute because (b = true) evaluates to true.
    }
    ```
2.  **Switch Fall-through:**
    Forgetting the `break` statement in a `switch` block causes the code to execute all subsequent cases until a `break` or the end of the block is reached.
3.  **Unreachable Code:**
    The compiler will throw an error if it detects code that can never be executed.
    ```java
    while (false) {
        System.out.println("Error!"); // Compiler Error: Unreachable code
    }
    ```
4.  **Infinite Loops:**
    Ensure your loop condition eventually becomes `false`.
    `for(;;){ }` is a valid syntax for an infinite loop.

---

## 5. Exam Tips and Key Takeaways

*   **Switch Types:** Memorize the types allowed in a `switch`. If you see a `long` or `double` in a switch header on the exam, it's a compiler error.
*   **Initialization Scope:** Variables declared inside a `for` loop header (`for(int i=0;...)`) are local to that loop.
*   **The `default` Case:** In a `switch`, the `default` block does not have to be at the end, though it is best practice. If no cases match and no `default` exists, the `switch` simply does nothing.
*   **Boolean Requirement:** Unlike C++, Java `if` and `while` statements **must** receive a `boolean`. `if(1)` is a compiler error in Java.
*   **Dangling Else:** An `else` always associates with the nearest preceding `if` that doesn't have an `else`, unless braces are used to specify otherwise.
*   **Labels:** Labels can be placed before any statement, but they are only useful with `break` and `continue` on loops or `switch` blocks. Labels must follow Java identifier rules (cannot start with a number).
---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
