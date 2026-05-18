# 086 — JPanel

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`JPanel` is the most commonly used **lightweight container**. It has no title bar or borders by default.
It is used to group other components together. You put components in panels, and put panels in the `JFrame`.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JPanel Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);

        // Create Panel 1 (Red background)
        JPanel panel1 = new JPanel();
        panel1.setBackground(Color.RED);
        panel1.add(new JLabel("I am in Panel 1"));
        panel1.add(new JButton("Button 1"));

        // Create Panel 2 (Blue background)
        JPanel panel2 = new JPanel();
        panel2.setBackground(Color.CYAN);
        panel2.add(new JLabel("I am in Panel 2"));
        panel2.add(new JButton("Button 2"));

        // Add panels to the frame (using GridLayout to split evenly)
        frame.setLayout(new GridLayout(1, 2)); // 1 row, 2 columns
        frame.add(panel1);
        frame.add(panel2);

        // frame.setVisible(true); // Conceptual
        System.out.println("JPanels created and added to Frame.");
    }
}
```

## 📝 Exam Tips
- `JPanel` is your main tool for building complex UI layouts.
- By default, `JPanel` uses the `FlowLayout` manager (components line up left to right).
- You can nest panels (put a `JPanel` inside another `JPanel`) infinitely to create complex grids and forms.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java uses `JPanel` as a lightweight invisible container to group components. C++ UI libraries have similar concepts (like Qt's `QFrame` or raw layout managers).**
