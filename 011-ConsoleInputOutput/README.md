# 011 — Console Input and Output

## 1. Definition and Core Concept

Console Input and Output (I/O) is the mechanism by which a Java application communicates with the user via the terminal or command prompt.

* **Standard Output (`System.out`):** Used to print text to the console.
* **Standard Input (`System.in`):** Used to read data typed by the user. Because `System.in` reads raw bytes, it is usually wrapped in a `Scanner` object to easily parse strings, integers, and other data types.
* **Standard Error (`System.err`):** Used to print error messages (often appears in red in IDE consoles).

---

## 2. Code Examples

### Console Output
Java provides three main methods for output:
```java
public class OutputDemo {
    public static void main(String[] args) {
        // 1. print(): Prints text without adding a new line at the end
        System.out.print("Hello ");
        
        // 2. println(): Prints text and appends a newline character (\n)
        System.out.println("World!"); // Prints "Hello World!" on one line
        
        // 3. printf(): Formatted printing (covered deeper in Topic 012)
        String name = "Alice";
        int score = 100;
        System.out.printf("%s scored %d points.\n", name, score);
    }
}
```

### Console Input (Using `Scanner`)
To read input, you must import `java.util.Scanner`.
```java
import java.util.Scanner;

public class InputDemo {
    public static void main(String[] args) {
        // Create a Scanner object hooked up to standard input
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter your name: ");
        String name = scanner.nextLine(); // Reads the whole line
        
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();      // Reads an integer
        
        System.out.println(name + " is " + age + " years old.");
        
        // Always close the scanner to prevent resource leaks
        scanner.close(); 
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **The Scanner "Newline" Bug:** When you read a number using `nextInt()` or `nextDouble()`, the Scanner reads the number but *leaves the Enter key (newline `\n`)* in the input buffer. If you immediately call `nextLine()` after `nextInt()`, it will instantly read the leftover `\n` and return an empty string. 
  **Fix:** Call `scanner.nextLine();` once to consume the leftover newline before asking for string input.
  ```java
  int age = scanner.nextInt();
  scanner.nextLine(); // Consume the leftover newline
  String name = scanner.nextLine(); // Now works correctly
  ```
* **Closing `System.in`:** Calling `scanner.close()` also closes the underlying `System.in` stream. If you try to create another Scanner later in the program, it will throw an exception. Only close the Scanner when your entire program is done requiring input.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions often try to catch you on the difference between `print` and `println`. Trace the output carefully to see if items end up on the same line or different lines.

* **Takeaway 1:** `System.out` and `System.in` are static members of the `java.lang.System` class.
* **Takeaway 2:** The `Scanner` class breaks its input into tokens using whitespace (blanks, tabs, and line terminators) as the default delimiter.

---

## ⚔️ Java vs C++ (Key Differences)

> **Java uses System.out.println() and Scanner for standard I/O. C++ heavily utilizes stream operators std::cout << and std::cin >>.**
