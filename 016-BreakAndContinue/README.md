# 016 - Break and Continue

In Java, `break` and `continue` are known as **jump statements**. They are used to alter the normal flow of control in loops (`for`, `while`, `do-while`) and branching statements (`switch`). Understanding how to manipulate loop execution is a core skill for both practical programming and Java certification exams (like the OCP).

---

## 1. The `break` Statement

The `break` statement is used to exit a loop or a `switch` block immediately. When a `break` is encountered, the program control jumps to the first line of code following the loop or block.

### A. Unlabeled Break
An unlabeled `break` only terminates the **innermost** loop or switch statement in which it appears.

```java
public class BreakExample {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            if (i == 5) {
                break; // Exit the loop when i is 5
            }
            System.out.print(i + " ");
        }
        // Output: 1 2 3 4 
        System.out.println("\nLoop finished.");
    }
}
```

### B. Labeled Break
Java allows you to define **labels** for loops. A label is an identifier followed by a colon (`:`). A labeled `break` can exit multiple nested loops at once.

```java
public class LabeledBreakExample {
    public static void main(String[] args) {
        outerLoop: // This is a label
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    break outerLoop; // Exits both loops
                }
                System.out.println("i=" + i + ", j=" + j);
            }
        }
    }
}
/* Output:
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
*/
```

---

## 2. The `continue` Statement

The `continue` statement skips the **remainder** of the current loop iteration and proceeds to the next iteration.

### A. Unlabeled Continue
In a `for` loop, `continue` jumps to the update expression. In `while` or `do-while` loops, it jumps to the boolean condition.

```java
public class ContinueExample {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            if (i == 3) {
                continue; // Skip the rest of the loop for i = 3
            }
            System.out.print(i + " ");
        }
        // Output: 1 2 4 5
    }
}
```

### B. Labeled Continue
A labeled `continue` skips the current iteration of the loop marked with that label and proceeds to the next iteration of **that specific loop**.

```java
public class LabeledContinueExample {
    public static void main(String[] args) {
        rowLoop:
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (j == 2) {
                    continue rowLoop; // Skips to the next 'i'
                }
                System.out.println("i=" + i + ", j=" + j);
            }
        }
    }
}
/* Output:
i=1, j=1
i=2, j=1
i=3, j=1
*/
```

---

## 3. Key Differences: Break vs. Continue

| Feature | `break` | `continue` |
| :--- | :--- | :--- |
| **Action** | Terminates the loop entirely. | Skips current iteration, starts next. |
| **Usage** | Loops and `switch` statements. | Loops only (cannot be used in `switch`). |
| **Next Step** | Code immediately after the loop. | Loop condition or update expression. |

---

## 4. Common Mistakes and Pitfalls

### 1. Unreachable Code
If you place code immediately after a `break` or `continue` within the same block, the compiler will throw an error.
```java
while(true) {
    break;
    System.out.println("Hello"); // Compilation Error: Unreachable code
}
```

### 2. Infinite Loops with `while`
When using `continue` in a `while` loop, ensure the counter update happens **before** the `continue` statement.
```java
int i = 0;
while (i < 5) {
    if (i == 2) {
        continue; // i will stay 2 forever, creating an infinite loop!
    }
    i++;
}
```

### 3. Using `continue` in a `switch`
You cannot use `continue` inside a `switch` statement unless that `switch` is inside a loop. Even then, the `continue` applies to the **loop**, not the `switch`.

---

## 5. Exam Tips and Key Takeaways

*   **Label Syntax:** Labels must follow Java identifier rules (cannot start with a digit) and must be followed by a colon (`:`).
*   **Label Placement:** A label must be placed immediately before the loop it refers to. You cannot label a random block of code and "jump" to it like a `goto`.
*   **Switch Context:** Remember that `break` is optional in `switch` (leading to fall-through), but it is mandatory if you want to exit the block early.
*   **Nested Logic:** In the exam, trace nested loops carefully. If you see a labeled `break` or `continue`, identify exactly which loop is being targeted.
*   **The "Update" Expression:** In a `for` loop, even if `continue` is triggered, the increment/decrement part (`i++`) **still executes**. This is a common trick question.

### Exam-Style Drill
**Question:** What is the output of the following code?
```java
int count = 0;
ROW_LOOP: for(int i=1; i<=3; i++) {
   for(int j=1; j<=3; j++) {
      if(i * j > 2) continue ROW_LOOP;
      count++;
   }
}
System.out.println(count);
```
*   *Trace:*
    *   i=1, j=1: 1*1=1 (<=2). count=1.
    *   i=1, j=2: 1*2=2 (<=2). count=2.
    *   i=1, j=3: 1*3=3 (>2). Continue ROW_LOOP (i becomes 2).
    *   i=2, j=1: 2*1=2 (<=2). count=3.
    *   i=2, j=2: 2*2=4 (>2). Continue ROW_LOOP (i becomes 3).
    *   i=3, j=1: 3*1=3 (>2). Continue ROW_LOOP (i loop ends).
*   **Answer:** 3

---

## ⚔️ Java vs C++ (Key Differences)

> **Java supports labeled reak and continue to break out of nested loops cleanly. C++ does not have labeled loops, relying on goto to escape deep nesting.**
