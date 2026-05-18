# 102 — Handling Mouse Events

> 📦 **Phase 10 — Event Handling**

## 🎯 What is it?
Mouse events occur when the user interacts with the mouse (clicking, pressing, releasing, moving).
Java splits these into two interfaces:
1. `MouseListener`: For clicks, enters, and exits.
2. `MouseMotionListener`: For drags and movements.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.event.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Mouse Event Example");
        JLabel label = new JLabel("Hover over or click me!", JLabel.CENTER);
        
        // Add MouseListener to the label
        label.addMouseListener(new MouseListener() {
            @Override
            public void mouseClicked(MouseEvent e) {
                label.setText("Mouse Clicked at X:" + e.getX() + " Y:" + e.getY());
            }

            @Override
            public void mousePressed(MouseEvent e) { } // Ignore

            @Override
            public void mouseReleased(MouseEvent e) { } // Ignore

            @Override
            public void mouseEntered(MouseEvent e) {
                label.setText("Mouse Entered bounds!");
            }

            @Override
            public void mouseExited(MouseEvent e) {
                label.setText("Mouse Exited bounds!");
            }
        });

        frame.add(label);
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // frame.setVisible(true);
    }
}
```

## 📝 Exam Tips
- `MouseEvent` provides `getX()` and `getY()` to find exact pixel coordinates of the interaction.
- If you implement `MouseListener`, you must override ALL 5 methods, even if you leave some empty.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
