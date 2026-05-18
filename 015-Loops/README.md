# Java Study Guide: 015 - Loops

In Java, **loops** are control flow statements that allow a block of code to be executed repeatedly as long as a specified condition remains true. Mastering loops is essential for handling arrays, collections, and repetitive logic—all of which are heavily tested in Java certification exams.

---

## 1. The `while` Loop
The `while` loop is a **pre-test loop**. It evaluates the boolean expression *before* executing the loop body. If the condition is `false` initially, the body never executes.

### Syntax
```java
while (boolean_expression) {
    // Body of loop
}
```

### Example
```java
int count = 0;
while (count < 3) {
    System.out.println("Count is: " + count);
    count++;
}
// Output: 
// Count is: 0
// Count is: 1
// Count is: 2
```

---

## 2. The `do-while` Loop
The `do-while` loop is a **post-test loop**. It executes the body first and *then* checks the condition. This guarantees that the code block runs **at least once**.

### Syntax
```java
do {
    // Body of loop
} while (boolean_expression); // Note the semicolon!
```

### Example
```java
int count = 5;
do {
    System.out.println("Executing at least once");
    count++;
} while (count < 3); 
// Output: Executing at least once
```

---

## 3. The Standard `for` Loop
The `for` loop is used when you know exactly how many times you want to iterate. It consists of three parts: **Initialization**, **Condition**, and **Update**.

### Syntax
```java
for (initialization; condition; update) {
    // Body
}
```

### Key Rules
1. **Initialization**: Runs only once at the start.
2. **Condition**: Checked before every iteration.
3. **Update**: Runs at the end of every iteration, before the next condition check.

### Example
```java
for (int i = 0; i < 3; i++) {
    System.out.print(i + " ");
}
// Output: 0 1 2
```

---

## 4. The Enhanced `for` Loop (For-Each)
Introduced in Java 5, this is used specifically to iterate through arrays or `Iterable` objects (like Lists).

### Syntax
```java
for (declaration : iterable_object) {
    // Body
}
```

### Example
```java
String[] names = {"Java", "Python", "C++"};
for (String name : names) {
    System.out.println(name);
}
```

---

## 5. Loop Control: `break` and `continue`

### `break`
Immediately terminates the innermost loop and transfers control to the statement following the loop.

### `continue`
Skips the current iteration and jumps to the next evaluation of the loop condition (or the update expression in a `for` loop).

### Example
```java
for (int i = 1; i <= 5; i++) {
    if (i == 2) continue; // Skip 2
    if (i == 4) break;    // Stop loop at 4
    System.out.print(i + " ");
}
// Output: 1 3 
```

---

## 6. Labeled Statements
Java allows you to "label" a loop. This is extremely useful when dealing with **nested loops** to specify which loop a `break` or `continue` should apply to.

### Example
```java
OUTER_LOOP: for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        if (i == 2 && j == 2) break OUTER_LOOP; 
        System.out.println("i=" + i + ", j=" + j);
    }
}
```

---

## 7. Common Mistakes & Pitfalls

1.  **Infinite Loops**: Forgetting to update the loop variable (e.g., forgetting `i++`).
    ```java
    for (int i = 0; i < 10; ) { // Missing update, will run forever if i starts < 10
    }
    ```
2.  **Off-by-One Errors**: Using `<` when you should use `<=` or vice versa, often leading to `ArrayIndexOutOfBoundsException`.
3.  **Missing Semicolon in `do-while`**: The `while(condition)` in a `do-while` loop **must** end with a semicolon.
4.  **Unreachable Code**: 
    ```java
    while(false) {
        System.out.println("Hello"); // Compilation Error: Unreachable code
    }
    ```
5.  **Scope Issues**: Variables declared in the `for` loop initialization are not accessible outside the loop.
    ```java
    for (int i = 0; i < 5; i++) {}
    System.out.println(i); // Compilation Error: i is out of scope
    ```

---

## 8. Exam Tips & Key Takeaways

*   **The `for` loop parts are optional**: `for(;;)` is a valid infinite loop.
*   **Multiple Variables**: You can initialize multiple variables of the **same type** in a `for` loop: `for(int i=0, j=10; i<j; i++, j--)`.
*   **For-Each Limitations**: You cannot use the enhanced `for` loop to modify the array's structure or remove elements from a collection while iterating.
*   **Condition Type**: The loop condition must always evaluate to a `boolean` or `Boolean`. In Java, `while(1)` is a compilation error (unlike C++).
*   **Labels**: Labels can be any valid identifier followed by a colon (`:`). They are usually placed immediately before the loop.
*   **The "Empty" Loop**: A semicolon right after the `for` or `while` header is valid but usually a logic error.
    ```java
    while (x < 10); // This loop has an empty body and might run forever!
    {
        x++;
    }
    ```

### Summary Table for Comparison

| Loop Type | Minimum Iterations | Best Used For... |
| :--- | :--- | :--- |
| `while` | 0 | When the number of iterations is unknown. |
| `do-while` | 1 | When the code must run at least once (e.g., Menus). |
| `for` | 0 | When the number of iterations is known. |
| `for-each` | 0 | Iterating through every element in an array/collection. |
