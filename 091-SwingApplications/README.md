# 091 — Swing Applications

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
A Swing Application is a standalone Java program with a Graphical User Interface (GUI). It requires a `main()` method to start and must have at least one top-level container (like `JFrame`) to host the UI components.

## 💻 Code Example: A Complete App

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main {
    public static void main(String[] args) {
        // Swing operations should ideally run on the Event Dispatch Thread (EDT)
        // This prevents freezing the UI while background tasks run.
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }

    private static void createAndShowGUI() {
        // 1. Create Frame
        JFrame frame = new JFrame("Simple Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        // 2. Create Components
        JTextField txtNum1 = new JTextField(5);
        JTextField txtNum2 = new JTextField(5);
        JButton btnAdd = new JButton("Add");
        JLabel lblResult = new JLabel("Result: ");

        // 3. Add Event Listener
        btnAdd.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    int n1 = Integer.parseInt(txtNum1.getText());
                    int n2 = Integer.parseInt(txtNum2.getText());
                    lblResult.setText("Result: " + (n1 + n2));
                } catch (NumberFormatException ex) {
                    lblResult.setText("Error: Enter valid numbers");
                }
            }
        });

        // 4. Add components to Frame
        frame.add(txtNum1);
        frame.add(new JLabel("+"));
        frame.add(txtNum2);
        frame.add(btnAdd);
        frame.add(lblResult);

        // 5. Pack and Show
        frame.pack(); // Adjusts window size to fit components automatically
        frame.setLocationRelativeTo(null); // Center on screen
        // frame.setVisible(true); // Uncomment to run
        System.out.println("Swing Application initialized.");
    }
}
```

## 📝 Exam Tips
- The `SwingUtilities.invokeLater()` is considered best practice. It ensures the GUI is created on the Event Dispatch Thread (EDT), making the UI thread-safe.
- `frame.pack()` is a useful method that resizes the `JFrame` so that all its contents are at or above their preferred sizes.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java Swing applications run entirely within the JVM and are styled using Pluggable Look and Feels (LAFs). C++ GUI apps compile to native binaries and natively utilize the host OS's rendering engine.**
