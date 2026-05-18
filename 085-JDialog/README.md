# 085 — JDialog

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`JDialog` is a top-level container used to create popup windows (dialog boxes). 
It is usually attached to a parent `JFrame`.

**Modal vs Non-Modal:**
- **Modal Dialog**: Blocks input to all other windows in the app until the dialog is closed (e.g., a "Do you want to save?" prompt).
- **Non-Modal Dialog**: Allows the user to interact with the main window while the dialog is open (e.g., a floating "Find and Replace" tool).

## 💻 Code Example

```java
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // Parent frame
        JFrame frame = new JFrame("Main Window");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Create a Dialog attached to the frame
        // true = Modal (blocks main window)
        JDialog dialog = new JDialog(frame, "Alert", true); 
        dialog.setSize(200, 100);
        dialog.setLayout(new java.awt.FlowLayout());
        
        dialog.add(new JLabel("This is a modal dialog."));
        JButton okBtn = new JButton("OK");
        okBtn.addActionListener(e -> dialog.dispose()); // Close dialog on click
        dialog.add(okBtn);
        
        // Center dialog relative to the frame
        dialog.setLocationRelativeTo(frame);
        
        // display (Conceptual)
        // frame.setVisible(true);
        // dialog.setVisible(true); // Program execution pauses here until dialog closes
        
        System.out.println("JDialog configured.");
    }
}
```

## 📝 Exam Tips
- `JOptionPane` is a utility class that uses `JDialog` internally to quickly show simple alerts, prompts, and confirmation boxes.
- `dispose()` is the method used to close and destroy a dialog window.

