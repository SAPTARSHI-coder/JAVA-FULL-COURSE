# 023 — Recursion

## 1. Definition and Core Concept

**Recursion** is a programming technique where a method calls itself in order to solve a problem. 

Recursive solutions are often used to solve complex problems by breaking them down into smaller, simpler, and identical sub-problems (like traversing file directories, or sorting algorithms like Merge Sort).

Every properly written recursive method must have two parts:
1. **The Base Case:** The condition that stops the recursion. Without it, the method will call itself forever.
2. **The Recursive Step:** The part where the method calls itself, progressing closer and closer to the base case.

---

## 2. Code Examples

### Classic Example: Factorial
Factorial of 5 (written as `5!`) is `5 * 4 * 3 * 2 * 1`.
Notice that `5! = 5 * 4!`. This identical sub-problem makes it perfect for recursion.

```java
public class RecursionDemo {
    
    public static int factorial(int n) {
        // 1. Base Case (stops the loop)
        if (n == 0 || n == 1) {
            return 1;
        } 
        // 2. Recursive Step (calls itself with n-1)
        else {
            return n * factorial(n - 1); 
        }
    }

    public static void main(String[] args) {
        int result = factorial(5);
        System.out.println("Factorial of 5 is: " + result); // 120
    }
}
```

### Behind the Scenes (The Call Stack)
When `factorial(3)` is called:
1. Returns `3 * factorial(2)` -> Pauses and waits.
2. `factorial(2)` returns `2 * factorial(1)` -> Pauses and waits.
3. `factorial(1)` hits the base case and returns `1`.
4. Step 2 finishes (`2 * 1 = 2`).
5. Step 1 finishes (`3 * 2 = 6`).

---

## 3. Common Mistakes or Pitfalls

* **Missing or Incorrect Base Case:** This is the most dangerous error in recursion. If the base case is missing, or if the recursive step doesn't move toward the base case, the method will loop infinitely.
* **StackOverflowError:** In Java, every method call adds a "frame" to the memory Stack. If a recursive method calls itself too many times (e.g., thousands of times), the Stack runs out of memory, causing the JVM to crash with a `StackOverflowError`.
* **Inefficiency:** Some recursive algorithms (like calculating Fibonacci numbers recursively without caching) recalculate the same values repeatedly, making them exceptionally slow compared to standard `for` loops.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions often ask you to trace the output of a recursive method where a `System.out.println()` statement occurs *after* the recursive call. Remember that code placed after a recursive call executes in reverse order as the stack unwinds!

* **Takeaway 1:** Anything that can be solved with recursion can also be solved with a standard loop (iteration). Recursion is just cleaner for certain mathematical and tree-traversal problems.
* **Takeaway 2:** To avoid `StackOverflowError`, always ensure the input approaches the base case with every call.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
