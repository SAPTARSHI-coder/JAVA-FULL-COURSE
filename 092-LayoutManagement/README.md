# 092 — Layout Management

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
In Swing (and AWT), you usually don't give components specific X and Y pixel coordinates. If you do, the app will break when resized or opened on a different OS/screen resolution.

Instead, we use **Layout Managers**. These are algorithms that automatically position and resize components within a container based on rules.

## 📦 Common Layout Managers
1. **FlowLayout**: Arranges components in a line, one after another (left to right). If it runs out of space, it drops to the next line. (Default for `JPanel`).
2. **BorderLayout**: Arranges components in 5 regions: North, South, East, West, and Center. (Default for `JFrame`).
3. **GridLayout**: Arranges components in a grid of equally sized cells (rows and columns).
4. **BoxLayout**: Arranges components in a single row OR a single column.
5. **null Layout (Absolute positioning)**: No layout manager. You must use `setBounds(x, y, w, h)`. Highly discouraged!

## 💻 Concept Example

```java
import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        
        // Setting a layout manager
        frame.setLayout(new FlowLayout()); 
        
        // Setting absolute layout (NO layout manager)
        // frame.setLayout(null);
        // button.setBounds(50, 50, 100, 30); // You must do this if layout is null!
    }
}
```

## 📝 Exam Tips
- Every container has a default layout manager.
- `JFrame` default: `BorderLayout`
- `JPanel` default: `FlowLayout`
- Calling `setLayout(null)` disables layout management.

