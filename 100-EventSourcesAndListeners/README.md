# 100 — Event Sources and Listeners (Connecting them)

> 📦 **Phase 10 — Event Handling**

## 🎯 What is it?
This is a summary of how the Delegation Event Model connects the **Source** to the **Listener**.

1. Create the **Source** (e.g., `JButton`).
2. Create an instance of a **Listener** (a class implementing `ActionListener`).
3. **Register** the Listener with the Source (e.g., `button.addActionListener(listener)`).
4. When the user clicks the button, the Source creates an **Event Object** (`ActionEvent`) and passes it to the Listener's method (`actionPerformed`).

## 💻 Code Example: 3 Ways to Connect

```java
import javax.swing.*;
import java.awt.event.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setLayout(new java.awt.FlowLayout());
        
        JButton btn1 = new JButton("Method 1");
        JButton btn2 = new JButton("Method 2");

        // METHOD 1: Anonymous Inner Class (Very common in older Java)
        btn1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Anonymous inner class clicked!");
            }
        });

        // METHOD 2: Lambda Expression (Modern Java 8+, preferred for functional interfaces)
        btn2.addActionListener(e -> {
            System.out.println("Lambda expression clicked!");
        });

        frame.add(btn1);
        frame.add(btn2);
        frame.setSize(300, 200);
        // frame.setVisible(true);
    }
}
```

## 📝 Exam Tips
- **Registration Methods**: `addActionListener()`, `addMouseListener()`, `addKeyListener()`.
- Modern Java heavily uses **Lambdas** for `ActionListener` because it has only one method (`actionPerformed`). You cannot use a lambda for `MouseListener` because it has 5 methods.

