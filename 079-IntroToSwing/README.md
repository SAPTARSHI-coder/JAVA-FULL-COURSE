# 079 — Intro to Swing

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
**Swing** was introduced to fix AWT's problems. It is built **on top of AWT** but provides completely new, **lightweight** components written entirely in Java.

Because Swing paints its own components, a Swing app looks exactly the same on Windows, Mac, and Linux.

## 💻 Swing Example

```java
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // 1. Create JFrame
        JFrame frame = new JFrame("Swing Example");

        // 2. Create components (Notice the 'J' prefix!)
        JLabel label = new JLabel("Welcome to Swing");
        JButton button = new JButton("Click Me");

        // 3. Add to frame
        frame.setLayout(new java.awt.FlowLayout());
        frame.add(label);
        frame.add(button);

        // 4. Easy Window Closing (Unlike AWT!)
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 5. Display
        frame.setSize(300, 200);
        // frame.setVisible(true); // Conceptual display
        System.out.println("Swing Frame prepared.");
    }
}
```

## 📝 Exam Tips
- Swing components start with a **J** (`JFrame`, `JButton`, `JLabel`).
- Built in the `javax.swing` package.
- They are **lightweight** (not dependent on OS native GUI).
- They support **Pluggable Look and Feel** (you can make it look like Windows or Mac or custom via code).

