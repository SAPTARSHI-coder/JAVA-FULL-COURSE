# 094 — GridLayout

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`GridLayout` arranges components in a rectangular grid of **equal-sized cells**. Every component takes up exactly the same amount of space.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("GridLayout Example (Keypad)");
        
        // 4 rows, 3 columns
        frame.setLayout(new GridLayout(4, 3, 5, 5)); // 5px horizontal/vertical gaps
        
        // Components are added row by row, left to right
        for (int i = 1; i <= 9; i++) {
            frame.add(new JButton(String.valueOf(i)));
        }
        
        frame.add(new JButton("*"));
        frame.add(new JButton("0"));
        frame.add(new JButton("#"));
        
        frame.setSize(300, 400);
        // frame.setVisible(true);
        System.out.println("GridLayout configured.");
    }
}
```

## 📝 Exam Tips
- Great for creating calculators, phone keypads, or chessboards.
- `new GridLayout(rows, columns)`
- If you set rows to 0 (e.g., `GridLayout(0, 3)`), it means "any number of rows, but exactly 3 columns".
- All cells are forced to be the exact same size, regardless of what's inside them.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
