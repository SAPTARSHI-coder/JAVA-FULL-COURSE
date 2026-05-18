# 066 — Scanner Class

> 📦 **Phase 6 — Collections (Utility)**

## 🎯 What is it?
`Scanner` (in `java.util`) is used to **read input** from keyboard, files, or strings. You've used it in topic 011 — this covers it more deeply.

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Reading different types
        System.out.print("Name: ");
        String name = sc.nextLine();         // full line

        System.out.print("Age: ");
        int age = sc.nextInt();              // integer

        System.out.print("GPA: ");
        double gpa = sc.nextDouble();        // double

        sc.nextLine(); // consume leftover newline after nextInt/nextDouble!

        System.out.print("City: ");
        String city = sc.nextLine();         // reads next full line

        System.out.println("\n--- Summary ---");
        System.out.printf("%s, Age %d, GPA %.2f, from %s%n", name, age, gpa, city);

        // Scanner from String (great for parsing)
        String data = "10 20 30 40 50";
        Scanner strScan = new Scanner(data);
        int sum = 0;
        while (strScan.hasNextInt()) {
            sum += strScan.nextInt();
        }
        System.out.println("Sum: " + sum);

        sc.close();
        strScan.close();
    }
}
```

**Output (example input: Alice, 20, 3.8, Delhi):**
```
Name: Alice
Age: 20
GPA: 3.8
City: Delhi

--- Summary ---
Alice, Age 20, GPA 3.80, from Delhi
Sum: 150
```

## ⚠️ Common Mistakes
- After `nextInt()` / `nextDouble()`, call `nextLine()` to consume the leftover newline — otherwise next `nextLine()` reads an empty string
- Not closing Scanner → resource leak warning

## 📝 Exam Tips
- `next()` → reads one word (stops at whitespace)
- `nextLine()` → reads entire line including spaces
- `hasNext()`, `hasNextInt()`, `hasNextDouble()` → check before reading
- Can read from: `System.in`, `File`, `String`


---

## ⚔️ Java vs C++ (Key Differences)

> **Java's `Scanner` provides rich, token-based text parsing natively. C++ typically parses standard input using `std::cin` with extraction operators (`>>`), which is fast but less feature-rich out-of-the-box for complex tokenizing.**
