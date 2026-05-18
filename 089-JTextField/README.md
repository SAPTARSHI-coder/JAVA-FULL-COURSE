# 089 — JTextField

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`JTextField` is a component that allows the editing of a **single line** of text. 
It is commonly used for user inputs like usernames, ages, or search bars.

## 💻 Code Example

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JTextField Example");
        frame.setLayout(new FlowLayout());

        JLabel label = new JLabel("Enter Name:");
        
        // Create a text field with 15 columns width
        JTextField textField = new JTextField(15);
        
        JButton button = new JButton("Submit");
        
        // Action: Get text from field when button is clicked
        button.addActionListener(e -> {
            String input = textField.getText();
            System.out.println("User typed: " + input);
            
            // Clear the field
            textField.setText("");
        });
        
        frame.add(label);
        frame.add(textField);
        frame.add(button);
        
        frame.setSize(300, 150);
        // frame.setVisible(true); // Conceptual
        System.out.println("JTextField configured.");
    }
}
```

## 📝 Exam Tips
- `getText()` retrieves the text as a String.
- `setText("...")` changes the text.
- Inherits from `JTextComponent`.
- For passwords, use `JPasswordField` instead (it hides characters with '*').

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
