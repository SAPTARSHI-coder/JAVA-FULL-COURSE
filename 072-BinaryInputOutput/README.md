# 072 — Binary Input Output

> 📦 **Phase 7 — File Handling & Streams**

## 🎯 What is it?
Binary I/O handles **raw bytes**. It is used for images, audio files, or serialized objects. 
Java provides `DataInputStream` and `DataOutputStream` to write primitive Java data types (int, float, double) directly in a machine-independent way.

## 💻 Code Example

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        String file = "data.bin";

        // Writing primitive data in binary format
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(file))) {
            dos.writeInt(100);
            dos.writeDouble(99.99);
            dos.writeBoolean(true);
            dos.writeUTF("Hello Binary!"); // writes a string
            System.out.println("Binary data written.");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Reading primitive data back
        // MUST read in the exact same order it was written!
        try (DataInputStream dis = new DataInputStream(new FileInputStream(file))) {
            int i = dis.readInt();
            double d = dis.readDouble();
            boolean b = dis.readBoolean();
            String s = dis.readUTF();

            System.out.println("Read Int: " + i);
            System.out.println("Read Double: " + d);
            System.out.println("Read Boolean: " + b);
            System.out.println("Read String: " + s);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**Output:**
```
Binary data written.
Read Int: 100
Read Double: 99.99
Read Boolean: true
Read String: Hello Binary!
```

## ⚠️ Common Mistakes
- Reading data in a different order than it was written will result in corrupt data or `EOFException`.

## 📝 Exam Tips
- `DataInputStream` / `DataOutputStream` handle primitive types (`readInt()`, `writeDouble()`, etc.).
- Binary I/O is more efficient than Text I/O for numerical data (no string parsing needed).


---

## ⚔️ Java vs C++ (Key Differences)

> **Java provides `DataInputStream` to read platform-independent primitive types (`readInt()`, `readDouble()`). C++ uses `read()` and `write()` with raw memory blocks (`char*`), which can lead to platform-dependent endianness issues.**
