# 071 — Text Input Output

> 📦 **Phase 7 — File Handling & Streams**

## 🎯 What is it?
Text Input/Output deals with reading and writing characters to files. Java handles this through **Character Streams** (`Reader` and `Writer`), ensuring characters are correctly encoded and decoded.

## 💻 Code Example

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        String file = "text_io_demo.txt";

        // Writing text using PrintWriter (most convenient)
        try (PrintWriter out = new PrintWriter(new FileWriter(file))) {
            out.println("Line 1: Text I/O is easy.");
            out.printf("Line 2: You can format strings! Age: %d%n", 25);
            System.out.println("File written successfully.");
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("-------------------------");

        // Reading text using BufferedReader
        try (BufferedReader in = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = in.readLine()) != null) {
                System.out.println("Read: " + line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**Output:**
```
File written successfully.
-------------------------
Read: Line 1: Text I/O is easy.
Read: Line 2: You can format strings! Age: 25
```

## 📝 Exam Tips
- `FileReader` / `FileWriter` are the raw character streams.
- Wrapping in `BufferedReader` gives you `readLine()`.
- Wrapping in `PrintWriter` gives you `print()`, `println()`, and `printf()`.
- Text I/O operates on 16-bit Unicode characters.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
