# 099 — Event Listeners

> 📦 **Phase 10 — Event Handling**

## 🎯 What is it?
An **Event Listener** is an interface. A class must implement this interface to "listen" for and handle specific events.

## 📦 Common Listener Interfaces & Methods

| Listener Interface | Event Handled | Methods You Must Implement |
|--------------------|---------------|-----------------------------|
| `ActionListener` | `ActionEvent` | `actionPerformed(ActionEvent e)` |
| `ItemListener` | `ItemEvent` | `itemStateChanged(ItemEvent e)` |
| `KeyListener` | `KeyEvent` | `keyPressed()`, `keyReleased()`, `keyTyped()` |
| `MouseListener` | `MouseEvent` | `mouseClicked()`, `mouseEntered()`, `mouseExited()`, `mousePressed()`, `mouseReleased()` |
| `WindowListener` | `WindowEvent` | `windowClosing()`, `windowOpened()`, etc. (7 methods) |

## 💻 Code Example (Implementing a Listener)

```java
import javax.swing.*;
import java.awt.event.*;

// 1. Implement the interface
public class Main implements ActionListener {
    
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        JButton btn = new JButton("Click Me");
        
        // 2. Instantiate the listener class and register it
        Main listener = new Main();
        btn.addActionListener(listener); 
        
        frame.add(btn);
        frame.setSize(200, 200);
        // frame.setVisible(true);
    }

    // 3. Override the interface method to define the behavior
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("Button clicked!");
    }
}
```

## 📝 Exam Tips
- Because listeners are **interfaces**, if you implement `MouseListener`, you **MUST** provide a body for all 5 of its methods, even if you leave them empty. (This leads us to Adapter Classes later).

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
