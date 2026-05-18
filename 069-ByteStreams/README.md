# 069 — Byte Streams

> 📦 **Phase 7 — File Handling & Streams**

## 🎯 What is it?
Byte streams read/write **raw bytes** (0-255). Used for binary files (images, audio, zip, etc.) and any file.

Key classes:
- `FileInputStream` — read bytes from file
- `FileOutputStream` — write bytes to file
- `BufferedInputStream` / `BufferedOutputStream` — buffered versions (faster)

## 💻 Code Example

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        String filename = "test.txt";

        // WRITE bytes to file
        try (FileOutputStream fos = new FileOutputStream(filename)) {
            String data = "Hello, Byte Stream!";
            fos.write(data.getBytes());  // convert String to bytes
            System.out.println("Written to file: " + filename);
        } catch (IOException e) {
            System.out.println("Write error: " + e.getMessage());
        }

        // READ bytes from file
        try (FileInputStream fis = new FileInputStream(filename)) {
            int byteData;
            System.out.print("Read from file: ");
            while ((byteData = fis.read()) != -1) {  // -1 = end of file
                System.out.print((char) byteData);
            }
            System.out.println();
        } catch (IOException e) {
            System.out.println("Read error: " + e.getMessage());
        }

        // Buffered — faster for large files
        try (BufferedInputStream bis = new BufferedInputStream(
                new FileInputStream(filename))) {
            byte[] buffer = new byte[1024];
            int bytesRead = bis.read(buffer);
            System.out.println("Buffered read (" + bytesRead + " bytes): "
                + new String(buffer, 0, bytesRead));
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

**Output:**
```
Written to file: test.txt
Read from file: Hello, Byte Stream!
Buffered read (19 bytes): Hello, Byte Stream!
```

## 📝 Exam Tips
- `read()` returns `-1` at end of file
- `fos.write(bytes)` — write entire byte array at once
- Buffered streams reduce disk access → much faster for large files
- `try-with-resources` → automatically closes streams (no finally needed)
- `FileOutputStream(file, true)` → append mode (default overwrites)


---

## ⚔️ Java vs C++ (Key Differences)

> **Java requires you to explicitly use `FileInputStream` or `FileOutputStream` to handle raw 8-bit bytes. C++ uses standard file streams (`std::ifstream`) opened with the `std::ios::binary` flag.**
