# 070 — Character Streams

> 📦 **Phase 7 — File Handling & Streams**

## 🎯 What is it?
Character streams handle **text data** with proper character encoding (Unicode, UTF-8, etc.).  
They automatically handle character encoding/decoding — use for text files.

Key classes:
- `FileReader` — read characters from file
- `FileWriter` — write characters to file
- `BufferedReader` — buffered reading (line by line)
- `BufferedWriter` — buffered writing

## 💻 Code Example

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        String filename = "notes.txt";

        // WRITE characters
        try (FileWriter fw = new FileWriter(filename);
             BufferedWriter bw = new BufferedWriter(fw)) {

            bw.write("Line 1: Java Character Streams");
            bw.newLine();  // platform-independent newline
            bw.write("Line 2: Easy to read text");
            bw.newLine();
            bw.write("Line 3: Works with Unicode too!");
            System.out.println("File written.");
        } catch (IOException e) {
            System.out.println("Write error: " + e.getMessage());
        }

        // READ characters — line by line
        try (FileReader fr = new FileReader(filename);
             BufferedReader br = new BufferedReader(fr)) {

            String line;
            int lineNum = 1;
            while ((line = br.readLine()) != null) {
                System.out.println(lineNum++ + ": " + line);
            }
        } catch (IOException e) {
            System.out.println("Read error: " + e.getMessage());
        }

        // PrintWriter — most convenient for text writing
        try (PrintWriter pw = new PrintWriter(new FileWriter("log.txt", true))) {
            pw.println("Log entry: app started");
            pw.printf("Value: %d%n", 42);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Log written.");
    }
}
```

**Output:**
```
File written.
1: Line 1: Java Character Streams
2: Line 2: Easy to read text
3: Line 3: Works with Unicode too!
Log written.
```

## 📝 Exam Tips
- Use **Byte streams** for binary files | **Character streams** for text files
- `BufferedReader.readLine()` returns `null` at end of file
- `FileWriter(file, true)` → append mode
- `PrintWriter` wraps FileWriter for easy `println()` / `printf()` support
- `BufferedReader` + `FileReader` = the standard combo for reading text files


---

## ⚔️ Java vs C++ (Key Differences)

> **Java natively reads/writes 16-bit Unicode characters using `Reader` and `Writer`. C++ standard streams operate on 8-bit `char`s by default, requiring `std::wifstream` or specialized libraries for proper wide character (Unicode) handling.**
