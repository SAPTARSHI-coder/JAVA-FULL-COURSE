# 008 — Precedence of Operators

## 1. Definition and Core Concept

When an expression contains multiple operators, Java needs a strict set of rules to determine the order in which those operations are executed. This is called **Operator Precedence**. 

If operators have the same precedence, Java uses **Associativity** (usually Left-to-Right, except for assignment and unary operators which are Right-to-Left) to break the tie.

### The General Hierarchy (Highest to Lowest)
1. **Postfix:** `expr++`, `expr--`
2. **Unary:** `++expr`, `--expr`, `+`, `-`, `~`, `!`
3. **Multiplicative:** `*`, `/`, `%`
4. **Additive:** `+`, `-`
5. **Shift:** `<<`, `>>`, `>>>`
6. **Relational:** `<`, `>`, `<=`, `>=`, `instanceof`
7. **Equality:** `==`, `!=`
8. **Bitwise AND/XOR/OR:** `&`, `^`, `|`
9. **Logical AND/OR:** `&&`, `||`
10. **Ternary:** `? :`
11. **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, etc.

---

## 2. Code Examples

```java
public class PrecedenceDemo {
    public static void main(String[] args) {
        // Multiplicative (*) has higher precedence than Additive (+)
        int a = 10 + 5 * 2; 
        System.out.println(a); // Output: 20 (NOT 30)

        // Parentheses override natural precedence
        int b = (10 + 5) * 2;
        System.out.println(b); // Output: 30

        // Associativity (Left-to-Right for division and multiplication)
        int c = 20 / 5 * 2; 
        System.out.println(c); // Output: 8 ( (20/5)*2 ), NOT 2

        // Logical Operators: && evaluates before ||
        boolean d = true || false && false;
        System.out.println(d); // Output: true ( evaluates as true || (false && false) )
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Relying on memorization instead of parentheses:** Code should be readable. Even if you know that `&` evaluates before `|`, writing `a & b | c & d` is terrible practice. Use parentheses: `(a & b) | (c & d)`.
* **String Concatenation Trap:** The `+` operator works left-to-right.
  ```java
  System.out.println("Result: " + 5 + 5);   // Outputs "Result: 55"
  System.out.println("Result: " + (5 + 5)); // Outputs "Result: 10"
  ```

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions heavily feature the pre/post increment operators mixed with arithmetic. Remember that `x++` evaluates to the current value, and THEN increments.

* **Takeaway 1:** Multiplication/Division/Modulo > Addition/Subtraction.
* **Takeaway 2:** Logical AND (`&&`) > Logical OR (`||`).
* **Takeaway 3:** When in doubt, or to ensure clear code intent, use parentheses `()`. They have the highest precedence of all.
---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
