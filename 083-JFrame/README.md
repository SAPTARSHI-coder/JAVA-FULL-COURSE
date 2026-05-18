# 083 — JFrame

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`JFrame` is the most common top-level container in Swing. It creates a standard application window with a title bar, borders, and window controls (minimize, maximize, close).

## 💻 Code Example

```java
import javax.swing.JFrame;
import javax.swing.JLabel;

public class Main {
    public static void main(String[] args) {
        // 1. Create the frame
        JFrame frame = new JFrame("My First JFrame App");

        // 2. Configure what happens when 'X' is clicked
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 3. Set the size (width, height in pixels)
        frame.setSize(400, 300);

        // 4. Center the window on the screen
        frame.setLocationRelativeTo(null);

        // 5. Add a simple component
        JLabel label = new JLabel("Hello, JFrame!", JLabel.CENTER);
        frame.add(label);

        // 6. Make the frame visible
        // frame.setVisible(true); // Conceptual: uncomment to see the window
        System.out.println("JFrame configured and ready to display.");
    }
}
```

## ⚠️ Common Mistakes
- Forgetting `frame.setVisible(true)`. The window exists in memory but won't show on screen!
- Forgetting `setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)`. If you don't do this, clicking 'X' hides the window, but the Java process keeps running in the background.

## 📝 Exam Tips
- `JFrame` is a heavyweight component.
- By default, it uses `BorderLayout` (more on layouts later).
- To add elements, use `frame.add(component)`.

