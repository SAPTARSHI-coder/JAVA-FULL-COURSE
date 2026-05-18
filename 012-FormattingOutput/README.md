# Java Study Guide: Formatting Output (Topic 012)

In Java, displaying data to the console is one of the first things you learn. However, controlling *how* that data looks—aligning columns, rounding decimals, or adding padding—is crucial for professional applications and a frequent topic on Java certification exams (like the OCA/OCP).

---

## 1. Introduction to Output Methods

Java provides three primary methods within the `System.out` object to send text to the console:

1.  **`print()`**: Outputs text without a newline. The next output starts exactly where the previous one ended.
2.  **`println()`**: Outputs text and then moves the cursor to a new line.
3.  **`printf()`**: (Formatted Print) Allows you to use "format specifiers" to control the exact appearance of the data.

### `printf` vs `String.format`
*   `System.out.printf(...)` prints the formatted string directly to the console.
*   `String.format(...)` returns a formatted `String` object but does not print it. They use the exact same syntax.

---

## 2. The Anatomy of `printf`

The syntax for `printf` is:
`System.out.printf("format string", argument1, argument2, ...);`

The "format string" contains plain text mixed with **Format Specifiers**. A specifier always starts with a percent sign (`%`).

### Common Format Specifiers

| Specifier | Data Type | Description |
| :--- | :--- | :--- |
| `%s` | String | Formats a string. |
| `%d` | Integer | Formats decimal integers (byte, short, int, long). |
| `%f` | Floating-point | Formats decimal numbers (float, double). |
| `%c` | Character | Formats a single character (Unicode). |
| `%b` | Boolean | Formats a boolean. (Note: Non-null objects return `true`). |
| `%n` | Newline | Platform-independent line separator (Recommended over `\n`). |

---

## 3. Advanced Formatting: Flags, Width, and Precision

A format specifier can be expanded to include more control:
`% [flags] [width] [.precision] conversion-character`

### A. Width
The **width** is the minimum number of characters to be written to the output. If the value is shorter than the width, it will be padded with spaces.

```java
System.out.printf("'%5d'%n", 10);   // Output: '   10' (Right-aligned by default)
System.out.printf("'%5s'%n", "Hi"); // Output: '   Hi'
```

### B. Precision
Used with floating-point numbers (`%f`) to define the number of decimal places.

```java
double pi = 3.14159265;
System.out.printf("%.2f%n", pi);    // Output: 3.14
System.out.printf("%.4f%n", pi);    // Output: 3.1416 (Rounds automatically!)
```

### C. Flags
Flags modify the output style:
*   `-` : **Left-justify** (default is right-justify).
*   `0` : **Zero-padding** (pads numbers with zeros instead of spaces).
*   `,` : **Comma separator** (adds grouping separators for large numbers).
*   `+` : **Sign** (always show `+` or `-` for numbers).

```java
System.out.printf("%-10s %d%n", "Total:", 100); // Left-aligned string
System.out.printf("%05d%n", 42);                // Output: 00042
System.out.printf("%,d%n", 1000000);            // Output: 1,000,000
```

---

## 4. Argument Indexing

Sometimes you want to refer to the same argument multiple times or print them in a different order. You use `n$` where `n` is the position of the argument.

```java
// %1$ refers to the first argument, %2$ to the second
System.out.printf("%2$s %1$s %2$s", "A", "B"); 
// Output: B A B
```

---

## 5. Code Example: Putting it all together

```java
public class FormattingDemo {
    public static void main(String[] args) {
        String item = "Widget";
        int quantity = 5;
        double price = 19.99;
        double total = quantity * price;

        System.out.printf("%-15s %5s %10s%n", "Item", "Qty", "Price");
        System.out.println("---------------------------------------");
        
        // %-15s : String, left-justified, 15 chars wide
        // %5d   : Integer, right-justified, 5 chars wide
        // %10.2f: Float, 10 chars wide, 2 decimal places
        System.out.printf("%-15s %5d %10.2f%n", item, quantity, price);
        System.out.printf("%-15s %5s %10.2f%n", "TOTAL", "", total);
    }
}
```

---

## 6. Common Mistakes & Pitfalls

1.  **Type Mismatch**: Using `%d` for a `double` or `%f` for an `int` will throw an `IllegalFormatConversionException` at runtime.
    *   *Wrong:* `System.out.printf("%d", 5.5);`
2.  **Missing Arguments**: If you have three `%` specifiers but only provide two variables, Java throws a `MissingFormatArgumentException`.
3.  **The `%n` vs `\n`**: While `\n` works on most systems, `%n` is the official "platform-independent" newline for `printf`. Use `%n` to ensure your code works perfectly on Windows, Linux, and macOS.
4.  **Boolean `%b` Trick**: If you pass a non-boolean object to `%b`, it returns `true` as long as the object is not null. It returns `false` only if the object is null or the boolean is `false`.

---

## 7. Exam Tips & Key Takeaways

*   **Memory Aid**: Remember the order: `[flags] [width] [.precision] [type]`.
*   **Rounding**: Remember that `%f` **rounds** the value; it doesn't just truncate it.
*   **String.format**: On the exam, you might see `String.format()` used to build a string that is then passed to `System.out.println()`. It behaves exactly like `printf`.
*   **Width is Minimum**: If the number is larger than the width provided (e.g., printing `1000` with `%2d`), Java will **not** truncate the number. It will expand the width to fit the data.
*   **Default Alignment**: By default, everything is **Right-Aligned**. Use the `-` flag to switch to **Left-Aligned**.
