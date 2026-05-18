# 073 — RandomAccessFile Operations

> 📦 **Phase 7 — File Handling & Streams**

## 🎯 What is it?
Streams (`InputStream`, `OutputStream`) are **sequential** — you read/write from start to finish.
`RandomAccessFile` allows you to jump to **any position** in a file to read or write, like an array of bytes on a disk.

## 💻 Code Example

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        String file = "random_access.dat";

        try (RandomAccessFile raf = new RandomAccessFile(file, "rw")) { // "rw" = read & write
            // Write some integers (4 bytes each)
            raf.writeInt(10); // bytes 0-3
            raf.writeInt(20); // bytes 4-7
            raf.writeInt(30); // bytes 8-11
            
            // Get current file pointer position
            System.out.println("Current position: " + raf.getFilePointer()); // 12
            
            // Seek (jump) back to the second integer (byte offset 4)
            raf.seek(4);
            System.out.println("Read at offset 4: " + raf.readInt()); // reads 20
            
            // Modify the third integer (jump to offset 8)
            raf.seek(8);
            raf.writeInt(99); // replaces 30 with 99
            
            // Verify the change
            raf.seek(8);
            System.out.println("Read modified at offset 8: " + raf.readInt()); // reads 99
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**Output:**
```
Current position: 12
Read at offset 4: 20
Read modified at offset 8: 99
```

## 📝 Exam Tips
- Implements both `DataInput` and `DataOutput` interfaces.
- `getFilePointer()` gets current byte position.
- `seek(long pos)` moves the pointer to a specific byte index.
- Requires a mode string: `"r"` (read-only) or `"rw"` (read-write).

