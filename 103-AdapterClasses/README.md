# 103 — Adapter Classes

> 📦 **Phase 10 — Event Handling**

## 🎯 What is it?
Implementing an interface like `MouseListener` forces you to write 5 methods. If you only care about `mouseClicked()`, writing 4 empty methods is annoying.

**Adapter Classes** solve this. They are abstract classes that provide empty implementations for all methods in a listener interface. You simply extend the adapter and override ONLY the methods you care about.

## 💻 Code Example: Without Adapter vs With Adapter

```java
import javax.swing.*;
import java.awt.event.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        
        // --- WITHOUT ADAPTER (Must implement all 5 methods) ---
        frame.addMouseListener(new MouseListener() {
            public void mouseClicked(MouseEvent e) { System.out.println("Click"); }
            public void mousePressed(MouseEvent e) {}
            public void mouseReleased(MouseEvent e) {}
            public void mouseEntered(MouseEvent e) {}
            public void mouseExited(MouseEvent e) {}
        });

        // --- WITH ADAPTER (Only override what you need) ---
        frame.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                System.out.println("Click (using Adapter)");
            }
        });
    }
}
```

## 📝 Exam Tips
- Adapters are a huge time-saver and keep code clean.
- Available for interfaces with multiple methods: `MouseAdapter`, `KeyAdapter`, `WindowAdapter`.
- There is NO `ActionAdapter` because `ActionListener` only has ONE method anyway.

