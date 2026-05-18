# 078 — AWT Class Hierarchy

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
**AWT (Abstract Window Toolkit)** is Java's original platform-dependent GUI framework. 
It uses the host OS's native GUI components (heavyweight components).

## 🌳 The Hierarchy

```
Object
  └── Component (Abstract class for all GUI elements)
        ├── Button, Label, Checkbox, Choice, List...
        └── Container (Can hold other components)
              ├── Window
              │     ├── Frame (Window with title bar & border)
              │     └── Dialog
              └── Panel (Used for grouping components)
                    └── Applet
```

## 💻 AWT Example

```java
import java.awt.*;
import java.awt.event.*;

public class Main {
    public static void main(String[] args) {
        // 1. Create a Frame (Window)
        Frame frame = new Frame("AWT Example");

        // 2. Create components
        Label label = new Label("Welcome to AWT");
        Button button = new Button("Click Me");

        // 3. Set layout and add components
        frame.setLayout(new FlowLayout());
        frame.add(label);
        frame.add(button);

        // 4. Handle Window Close Event (AWT requires this manually!)
        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });

        // 5. Display the frame
        frame.setSize(300, 200);
        frame.setVisible(true); // Don't block testing environments, imagine this opens a window
        System.out.println("AWT Frame launched (conceptually).");
    }
}
```

## 📝 Exam Tips
- AWT components are **heavyweight** (they map directly to OS components).
- Disadvantage: Look and feel changes depending on OS (Windows looks different from Mac).
- `Component` is the superclass of everything visible.
- `Container` is a Component that can hold other Components.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
