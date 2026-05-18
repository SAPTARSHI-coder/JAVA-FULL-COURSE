# 093 — BorderLayout

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`BorderLayout` divides the container into five regions: **North, South, East, West, and Center**.
Each region can contain **only one component**.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("BorderLayout Example");
        
        // JFrame uses BorderLayout by default, but we can set it explicitly
        frame.setLayout(new BorderLayout(5, 5)); // 5px horizontal & vertical gap
        
        JButton btnNorth = new JButton("North");
        JButton btnSouth = new JButton("South");
        JButton btnEast = new JButton("East");
        JButton btnWest = new JButton("West");
        JButton btnCenter = new JButton("Center (Stretches to fill)");
        
        // You MUST specify the region when adding!
        frame.add(btnNorth, BorderLayout.NORTH);
        frame.add(btnSouth, BorderLayout.SOUTH);
        frame.add(btnEast, BorderLayout.EAST);
        frame.add(btnWest, BorderLayout.WEST);
        frame.add(btnCenter, BorderLayout.CENTER);
        
        frame.setSize(400, 300);
        // frame.setVisible(true);
        System.out.println("BorderLayout configured.");
    }
}
```

## 📝 Exam Tips
- If you don't specify a region (e.g., `frame.add(button)`), it automatically goes to the **Center**.
- The **Center** region takes up all leftover space.
- North/South components stretch horizontally to fill width.
- East/West components stretch vertically to fill height between North and South.
- If a region is left empty, the other regions expand to fill the void.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
