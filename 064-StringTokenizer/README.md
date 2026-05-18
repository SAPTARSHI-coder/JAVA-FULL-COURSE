# 064 — StringTokenizer

> 📦 **Phase 6 — Collections (Utility)**

## 🎯 What is it?
`StringTokenizer` splits a string into **tokens** (pieces) based on a delimiter. It's a **legacy class** — `String.split()` is the modern replacement.

| Feature | StringTokenizer | String.split() |
|---------|----------------|---------------|
| Returns | Tokens one by one | String array |
| Regex support | ❌ No | ✅ Yes |
| Performance | Slightly faster | Slightly slower |
| Modern? | Legacy | Preferred |

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String sentence = "Java is fun to learn";

        // Default delimiter: whitespace
        StringTokenizer st = new StringTokenizer(sentence);
        System.out.println("Token count: " + st.countTokens());
        while (st.hasMoreTokens()) {
            System.out.print("[" + st.nextToken() + "] ");
        }
        System.out.println();

        // Custom delimiter
        String csv = "Alice,25,Engineer,Mumbai";
        StringTokenizer st2 = new StringTokenizer(csv, ",");
        while (st2.hasMoreTokens()) {
            System.out.println(st2.nextToken());
        }

        // Multiple delimiters
        String data = "one:two;three:four";
        StringTokenizer st3 = new StringTokenizer(data, ":;");
        while (st3.hasMoreTokens()) {
            System.out.print(st3.nextToken() + " ");
        }
        System.out.println();

        // Modern equivalent — String.split()
        String[] parts = csv.split(",");
        System.out.println("Using split: " + Arrays.toString(parts));
    }
}
```

**Output:**
```
Token count: 5
[Java] [is] [fun] [to] [learn]
Alice
25
Engineer
Mumbai
one two three four
Using split: [Alice, 25, Engineer, Mumbai]
```

## 📝 Exam Tips
- `countTokens()` → number of tokens remaining
- `hasMoreTokens()` → check | `nextToken()` → get next
- Default delimiter: space, tab, newline, carriage return, form feed
- Prefer `String.split()` in modern code (supports regex)

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
