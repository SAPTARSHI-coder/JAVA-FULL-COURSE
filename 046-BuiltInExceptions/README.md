# 046 — Common Built-in Exceptions

## 1. Definition and Core Concept

The Java standard library provides dozens of pre-defined exceptions that cover almost every standard error scenario you will encounter in day-to-day programming. Familiarizing yourself with these built-in exceptions is critical so you can read stack traces effectively and debug your code quickly.

We classify them into **Unchecked (Runtime)** and **Checked (Compile-time)**.

---

## 2. Common Unchecked Exceptions (`RuntimeException`)
These usually indicate a flaw in your program's logic.

| Exception Name | When it Occurs | Example Scenario |
| :--- | :--- | :--- |
| **`NullPointerException`** | You attempt to use an object reference that currently points to `null`. | Calling `name.length()` when `name` is null. |
| **`ArithmeticException`** | An exceptional arithmetic condition occurs. | Dividing an integer by zero: `10 / 0`. |
| **`ArrayIndexOutOfBoundsException`** | Trying to access an array index that is negative, or greater than/equal to the array's length. | Accessing `arr[5]` in an array of size 3. |
| **`StringIndexOutOfBoundsException`** | Same as above, but for strings. | Calling `text.charAt(10)` on a 5-letter word. |
| **`ClassCastException`** | You attempt to cast an object to a subclass of which it is not an instance. | Casting an `Animal` to a `Dog`, when it is actually a `Cat`. |
| **`IllegalArgumentException`** | A method receives an argument that is formatted incorrectly or logically invalid. | Passing a negative number to a method expecting a positive age. |
| **`NumberFormatException`** | You attempt to convert a String to a number, but the string doesn't contain valid numbers. | Calling `Integer.parseInt("Hello")`. |

---

## 3. Common Checked Exceptions
These indicate environmental or external resource failures that you *must* handle.

| Exception Name | When it Occurs | Example Scenario |
| :--- | :--- | :--- |
| **`IOException`** | General Input/Output failure. Parent of many other exceptions. | Network connection drops while reading data. |
| **`FileNotFoundException`** | You attempt to open a file that does not exist on the hard drive. | Reading `C:/config.txt` when it was deleted. |
| **`SQLException`** | A database access error occurs. | Bad credentials, or the SQL query has a syntax error. |
| **`ClassNotFoundException`** | The JVM tries to load a class at runtime but cannot find the `.class` file. | Usually occurs when dynamically loading classes via reflection. |
| **`InterruptedException`** | A thread is sleeping or waiting, and another thread interrupts it. | Calling `Thread.sleep(1000)`. |

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** You must be able to visually identify whether a standard exception is Checked or Unchecked based on its name. As a general rule of thumb, if it ends in `Error` or inherits from `RuntimeException` (like `NullPointerException`), it's unchecked. If it relates to I/O or Databases, it's checked.

* **Takeaway 1:** Never catch `NullPointerException`. Fix the code that caused the object to be null!
* **Takeaway 2:** When writing your own code, try to throw these built-in exceptions (like `IllegalArgumentException`) rather than building your own, as other Java developers already understand exactly what they mean.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
