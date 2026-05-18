# 104 — Event Handling Examples

> 📦 **Phase 10 — Event Handling**

## 🎯 What is it?
Let's combine multiple concepts: Text fields, Buttons, and ActionListeners.

## 💻 Code Example: A Simple Login Form

```java
import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Login");
        frame.setLayout(new GridLayout(3, 2, 5, 5));

        JLabel lblUser = new JLabel("Username:");
        JTextField txtUser = new JTextField();
        
        JLabel lblPass = new JLabel("Password:");
        JPasswordField txtPass = new JPasswordField(); // Hides text with *
        
        JButton btnLogin = new JButton("Login");
        JLabel lblStatus = new JLabel("");

        btnLogin.addActionListener(e -> {
            String user = txtUser.getText();
            // getPassword returns char[], so convert to String
            String pass = new String(txtPass.getPassword());
            
            if (user.equals("admin") && pass.equals("1234")) {
                lblStatus.setText("Success!");
                lblStatus.setForeground(Color.GREEN);
            } else {
                lblStatus.setText("Failed!");
                lblStatus.setForeground(Color.RED);
            }
        });

        frame.add(lblUser);
        frame.add(txtUser);
        frame.add(lblPass);
        frame.add(txtPass);
        frame.add(new JLabel("")); // Empty cell
        frame.add(btnLogin);
        
        frame.add(lblStatus);

        frame.setSize(300, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // frame.setVisible(true);
    }
}
```

## 📝 Exam Tips
- Use `JPasswordField` instead of `JTextField` for passwords.
- Understand how to retrieve data from a component (`getText()`) inside an `ActionListener` to perform logic.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
