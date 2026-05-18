# 090 — JTextArea

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`JTextArea` provides an area to type and display **multiple lines** of text.
It is commonly used for comments, addresses, or displaying logs.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JTextArea Example");
        frame.setLayout(new BorderLayout());

        // Create text area with 10 rows and 30 columns
        JTextArea textArea = new JTextArea(10, 30);
        
        // Make text wrap to the next line when reaching the edge
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true); // Wrap at word boundaries, not middle of words
        
        // Add default text
        textArea.setText("Welcome to the text editor.\nType your notes here.\n");
        
        // JTextArea does NOT have scrollbars automatically!
        // You MUST wrap it in a JScrollPane.
        JScrollPane scrollPane = new JScrollPane(textArea);
        
        frame.add(scrollPane, BorderLayout.CENTER);
        
        frame.setSize(400, 300);
        // frame.setVisible(true); // Conceptual
        System.out.println("JTextArea configured with JScrollPane.");
    }
}
```

## ⚠️ Common Mistakes
- Putting a `JTextArea` directly into a `JFrame` without a `JScrollPane`. If the text goes beyond the screen, the user won't be able to scroll to see it!

## 📝 Exam Tips
- `append("string")` adds text to the end of the existing text.
- `setEditable(false)` turns it into a read-only multi-line display box.
- Inherits from `JTextComponent` (just like `JTextField`).

