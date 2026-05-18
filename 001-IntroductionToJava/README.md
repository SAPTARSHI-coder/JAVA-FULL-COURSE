# 001 — Introduction to Java

> 📦 **Phase 1 — Java Fundamentals**

## 🎯 What is Java?
Java is a high-level, class-based, object-oriented programming language designed to have as few implementation dependencies as possible. Originally developed by **James Gosling** at **Sun Microsystems** (released in 1995), it was initially called *Oak*. 

Java is a **compiled + interpreted** language. Your source code (`.java`) is compiled into **bytecode** (`.class`), which is then executed (interpreted) by the **JVM (Java Virtual Machine)**.  

This two-step process gives Java its famous motto: *"Write Once, Run Anywhere" (WORA)* — the JVM handles the platform-specific translation.

---

## ✨ Key Features of Java (The Buzzwords)
For exams, you must know these defining characteristics:
1. **Simple:** Easy to learn, syntax is clean and based on C++. Complicated features like pointers and operator overloading were removed.
2. **Object-Oriented:** Everything in Java is an object (except primitive data types).
3. **Platform Independent:** Code is compiled to bytecode, which can run on any OS that has a JVM.
4. **Secured:** Java has no explicit pointers, and programs run inside a virtual machine sandbox.
5. **Robust:** Strong memory management, automatic garbage collection, and strict compile-time/run-time error checking (Exception Handling).
6. **Architecture Neutral:** The size of primitive types is fixed across all platforms (e.g., an `int` is always 4 bytes, unlike in C/C++ where it varies).
7. **Multithreaded:** Built-in support to write programs that perform many tasks simultaneously.

---

## 🏗️ JDK vs JRE vs JVM

Understanding the Java ecosystem components is critical:

| Component | Full Form | What it does | Includes |
|-----------|-----------|--------------|----------|
| **JDK** | Java Development Kit | Environment used to **develop** Java apps. | JRE + Development Tools (`javac`, `java`, `javadoc`, `jdb`) |
| **JRE** | Java Runtime Environment | Environment used to **run** Java apps. | JVM + Core Library Classes (`rt.jar`, etc.) |
| **JVM** | Java Virtual Machine | The engine that **executes** bytecode. | ClassLoader, Memory Area, Execution Engine |

*(JDK contains JRE, and JRE contains JVM).*

---

## 💻 Your First Program & Detailed Breakdown

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

**What exactly is happening here?**
*   `public`: An access modifier. It means this class/method is accessible from anywhere. The JVM needs `main` to be public so it can execute it from outside the class.
*   `class Main`: Declares a class named `Main`. In Java, all code must reside inside a class.
*   `static`: This method belongs to the class itself, not to an object of the class. The JVM can invoke `main()` without needing to instantiate the `Main` class first.
*   `void`: The return type. The `main` method doesn't return any value to the JVM.
*   `main`: The name of the method. This is the exact entry point the JVM looks for.
*   `String[] args`: Command-line arguments. It accepts an array of strings passed when running the program.
*   `System.out.println()`:
    *   `System`: A built-in class in the `java.lang` package.
    *   `out`: A static member field of the `System` class (representing standard output).
    *   `println()`: A method that prints text to the console and adds a new line.

**Compile & Run Cycle:**
```bash
javac Main.java    # The Compiler creates Main.class (bytecode)
java Main          # The JVM translates bytecode to machine code and executes
```

---

## ⚔️ Java vs C++ (Common Exam Question)

| Feature | Java | C++ |
|---------|------|-----|
| **Execution** | Compiled & Interpreted | Compiled only |
| **Pointers** | No explicit pointers (for security) | Supports explicit pointers |
| **Memory Management** | Automatic Garbage Collection | Manual (`new` and `delete`) |
| **Multiple Inheritance** | Not supported for classes (uses Interfaces) | Supported for classes |
| **Platform** | Platform Independent (Bytecode) | Platform Dependent (Machine code) |
| **Structures/Unions** | Does not support `struct` or `union` | Supports `struct` and `union` |

---

## ⚠️ Common Mistakes & Exam Tips

*   **File Naming:** The file name **must** exactly match the `public class` name (e.g., `Main.java` for `public class Main`).
*   **Case Sensitivity:** Java is strictly case-sensitive (`Main` ≠ `main`).
*   **Semicolons:** Every statement must end with a semicolon `;`.
*   **Not 100% Object-Oriented:** Java relies on primitive data types (`int`, `char`, `boolean`), which are not objects. This is why it's technically not a *pure* object-oriented language.
*   **Pass by Value:** Java is strictly **pass-by-value**. (When passing objects, the *reference* to the object is passed by value).

