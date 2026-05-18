# 068 — Streams (I/O)

> 📦 **Phase 7 — File Handling & Streams**

## 🎯 What is it?
In Java, a **stream** is a sequence of data flowing between a source and a destination.

**Two main stream types:**

| Type | Classes | Handles |
|------|---------|---------|
| **Byte Streams** | `InputStream` / `OutputStream` | Raw binary data (images, audio, any file) |
| **Character Streams** | `Reader` / `Writer` | Text data (with proper encoding) |

**Stream hierarchy:**
```
InputStream (abstract)
    ├── FileInputStream
    ├── ByteArrayInputStream
    └── BufferedInputStream

OutputStream (abstract)
    ├── FileOutputStream
    ├── ByteArrayOutputStream
    └── BufferedOutputStream

Reader (abstract)
    ├── FileReader
    └── BufferedReader

Writer (abstract)
    ├── FileWriter
    └── BufferedWriter
```

## 💻 Concept Overview

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        // Streams are the foundation of all Java I/O

        // System.in  = InputStream  (keyboard input)
        // System.out = PrintStream  (console output — extends OutputStream)
        // System.err = PrintStream  (error output)

        System.out.println("System.in class:  " + System.in.getClass().getName());
        System.out.println("System.out class: " + System.out.getClass().getName());

        // All streams follow open → use → close pattern
        // Modern way: try-with-resources (auto-closes)
        String text = "Hello, File I/O!";

        // Writing to a byte array stream (in-memory, no actual file)
        try (ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
            byte[] bytes = text.getBytes();
            baos.write(bytes);
            System.out.println("Written bytes: " + baos.size());
            System.out.println("Content: " + baos.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**Output:**
```
System.in class:  java.io.BufferedInputStream
System.out class: java.io.PrintStream
Written bytes: 16
Content: Hello, File I/O!
```

## 📝 Exam Tips
- **Byte streams**: raw bytes — use for binary files
- **Character streams**: text with encoding — use for text files
- Always close streams! Use `try-with-resources` → auto-closes
- Buffered streams wrap others to improve performance
- `System.in`, `System.out`, `System.err` are pre-opened streams

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
