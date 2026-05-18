# 074 — File Management

> 📦 **Phase 7 — File Handling & Streams**

## 🎯 What is it?
The `java.io.File` class represents a file or directory path. It doesn't read/write contents, but manages the filesystem metadata (create, delete, check size, list directories).

## 💻 Code Example

```java
import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        File file = new File("test_management.txt");
        
        try {
            if (file.createNewFile()) {
                System.out.println("File created.");
            }
            
            System.out.println("Exists? " + file.exists());
            System.out.println("Size: " + file.length() + " bytes");
            System.out.println("Is File? " + file.isFile());
            System.out.println("Is Directory? " + file.isDirectory());
            System.out.println("Absolute Path: " + file.getAbsolutePath());
            
            // Directory management
            File dir = new File("my_app_dir");
            dir.mkdir(); // create directory
            System.out.println("Directory created? " + dir.exists());
            
            // Cleanup
            file.delete();
            dir.delete();
            System.out.println("Cleanup completed.");
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**Output:**
```
File created.
Exists? true
Size: 0 bytes
Is File? true
Is Directory? false
Absolute Path: .../test_management.txt
Directory created? true
Cleanup completed.
```

## 📝 Exam Tips
- `createNewFile()` creates an empty file.
- `mkdir()` creates a directory; `mkdirs()` creates a directory and missing parent directories.
- `list()` returns an array of file/folder names inside a directory.
- `length()` returns size in bytes.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
