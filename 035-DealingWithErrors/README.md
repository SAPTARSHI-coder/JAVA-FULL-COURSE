# 035 — Dealing with Errors

## 1. Definition and Core Concept

In software development, things inevitably go wrong. Files get deleted, servers go offline, users input letters instead of numbers, and arrays run out of bounds.

Broadly speaking, issues in Java fall into three categories:
1. **Compile-time Errors (Syntax Errors):** Mistakes in grammar (missing semicolons, mismatched types). The program refuses to compile. You must fix these before the code can run.
2. **Logical Errors (Bugs):** The code compiles and runs, but produces the wrong result (e.g., using `+` instead of `-`). The compiler cannot catch these.
3. **Runtime Errors (Exceptions/Errors):** The code is grammatically correct and compiles fine, but an abnormal event occurs during execution that disrupts the normal flow of instructions.

### The Java Solution: Exception Handling
To deal with Runtime Errors, Java uses a powerful mechanism called **Exception Handling**. Instead of letting the program instantly crash when a runtime error occurs, Java generates an "Exception Object" and throws it. The developer can write code to "catch" this object and resolve the issue gracefully.

---

## 2. Code Examples (The Problem)

### Without Exception Handling (Crash)
```java
import java.util.Scanner;

public class ErrorDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number to divide 100 by: ");
        int divisor = scanner.nextInt();
        
        // If the user types '0', this triggers an ArithmeticException.
        // Because we don't "catch" the error, the program instantly crashes here.
        int result = 100 / divisor; 
        
        // This line will never print if divisor is 0
        System.out.println("Result: " + result); 
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Ignoring Runtime Risks:** Assuming the user will always type valid input, or assuming a file will always exist on the hard drive. Robust code anticipates failures.
* **Using traditional `if-else` for error handling:** In older languages like C, developers had to check error codes after every single operation. 
  ```c
  int fileStatus = openFile("data.txt");
  if (fileStatus == -1) { /* handle error */ }
  ```
  This cluttered the "happy path" code with endless error-checking logic. Java Exceptions separate the normal code from the error-handling code.

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be able to differentiate between a compile-time error and a runtime exception. `String s = 5;` is a compile error. `int[] a = new int[2]; a[5] = 10;` is a runtime exception.

* **Takeaway 1:** Exceptions are objects in Java that represent an abnormal event.
* **Takeaway 2:** If an exception is "thrown" and not "caught", the JVM halts execution and prints a stack trace to the console.

