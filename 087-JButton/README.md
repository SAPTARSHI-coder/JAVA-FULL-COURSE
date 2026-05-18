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

## ⚔️ Java vs C++ (Key Differences)

> **Java's `JButton` fires an `ActionEvent` when clicked. C++ buttons (e.g., `QPushButton`) fire signals, often using the powerful Signal/Slot mechanism or standard callback functions.**
