# 087 — JButton

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`JButton` creates a push-button that the user can click to trigger an action.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.event.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JButton Example");
        frame.setLayout(null); // Absolute positioning for demo
        
        // Create button with text
        JButton button = new JButton("Click Me!");
        button.setBounds(100, 50, 150, 40); // x, y, width, height
        
        // Optional: add an icon (assuming icon.png exists)
        // button.setIcon(new ImageIcon("icon.png"));
        
        // Add an ActionListener to make the button DO something
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.println("Button was clicked!");
                button.setText("Clicked!");
            }
        });
        
        frame.add(button);
        frame.setSize(400, 200);
        // frame.setVisible(true); // Conceptual
        System.out.println("JButton configured.");
    }
}
```

## 📝 Exam Tips
- Inherits from `AbstractButton`.
- Uses `addActionListener()` to handle click events.
- Can display text, an image icon, or both simultaneously.
- Constructor can take a String: `new JButton("Submit")`.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
