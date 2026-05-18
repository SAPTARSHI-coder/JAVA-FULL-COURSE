# 084 — JApplet

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
`JApplet` is the Swing version of the old AWT `Applet`. It provided a way to embed Swing components into web browsers.

**Note:** Applets (both AWT and Swing) have been completely deprecated and removed from modern Java versions. Browsers no longer support Java plugins.

## 💻 Code Example (Legacy Syntax)

```java
import javax.swing.JApplet;
import javax.swing.JLabel;

/*
  <applet code="Main.class" width="300" height="200">
  </applet>
*/
public class Main extends JApplet {
    
    // Uses init() instead of main()
    public void init() {
        JLabel label = new JLabel("Hello from JApplet!", JLabel.CENTER);
        // Note: You must add to the content pane in older Java versions, 
        // though modern Java allowed direct add()
        getContentPane().add(label);
        
        System.out.println("JApplet initialized.");
    }
}
```

## 📝 Exam Tips
- If asked, mention that `JApplet` is the Swing extension of AWT's `Applet`.
- It uses the same lifecycle methods: `init()`, `start()`, `stop()`, `destroy()`.
- It is a top-level container, so it has a `JRootPane` and a `contentPane`.
- It is obsolete technology.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
