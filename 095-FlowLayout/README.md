# 095 — FlowLayout

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`FlowLayout` places components in a row, sized at their preferred size. If there is no space left in the current row, it wraps them to the next row (like words wrapping in a text editor).

This is the default layout manager for `JPanel`.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("FlowLayout Example");
        
        // FlowLayout.LEFT, CENTER (default), or RIGHT alignment
        frame.setLayout(new FlowLayout(FlowLayout.CENTER, 10, 20)); // 10px hgap, 20px vgap
        
        for (int i = 1; i <= 5; i++) {
            frame.add(new JButton("Button " + i));
        }
        
        // If the frame is wide, all 5 buttons will be on one line.
        // If you shrink the window, Button 4 and 5 will wrap to the next line.
        frame.setSize(400, 200);
        // frame.setVisible(true);
        System.out.println("FlowLayout configured.");
    }
}
```

## 📝 Exam Tips
- Components retain their **preferred size** (they don't stretch to fill space like BorderLayout or GridLayout).
- Default alignment is `CENTER`.
- If you resize the window during runtime, FlowLayout dynamically rearranges the components.

