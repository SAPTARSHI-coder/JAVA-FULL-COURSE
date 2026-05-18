# 088 — JLabel

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`JLabel` is used to display a short text string, an image, or both. It does not react to user input (like clicking or typing) by default.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JLabel Example");
        frame.setLayout(new FlowLayout());

        // 1. Simple text label
        JLabel label1 = new JLabel("Username:");
        
        // 2. Label with custom font and color
        JLabel label2 = new JLabel("Access Denied!");
        label2.setFont(new Font("Arial", Font.BOLD, 20));
        label2.setForeground(Color.RED);
        
        // 3. Label with an image (if file exists)
        // JLabel imgLabel = new JLabel(new ImageIcon("logo.png"));
        
        frame.add(label1);
        frame.add(label2);
        
        frame.setSize(300, 150);
        // frame.setVisible(true); // Conceptual
        System.out.println("JLabels configured.");
    }
}
```

## 📝 Exam Tips
- By default, labels are transparent. If you want to set a background color, you must first call `label.setOpaque(true)`.
- You can change text dynamically at runtime using `label.setText("New String")`.
- It is a passive component (display only).

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
