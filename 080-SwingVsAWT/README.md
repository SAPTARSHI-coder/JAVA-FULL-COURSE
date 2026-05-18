# 080 — Swing vs AWT

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
One of the most frequently asked exam questions is comparing AWT and Swing.

## ⚖️ Comparison Table

| Feature | AWT | Swing |
|---------|-----|-------|
| **Weight** | Heavyweight (relies on OS) | Lightweight (written in pure Java) |
| **Speed** | Faster execution (native code) | Slower execution (draws itself) |
| **Look & Feel** | Platform-dependent (changes per OS) | Pluggable (same across OS, or customizable) |
| **MVC Pattern** | Doesn't follow MVC | Follows Model-View-Controller (MVC) internally |
| **Package** | `java.awt` | `javax.swing` |
| **Prefix** | `Button`, `Label`, `TextField` | `JButton`, `JLabel`, `JTextField` |
| **Features** | Basic components | Advanced components (Tables, Trees, TabbedPanes) |

## 📝 Exam Tips
- Always define heavyweight vs lightweight.
- **Heavyweight**: OS manages the component (creates a native OS window/button).
- **Lightweight**: Java manages the component (draws pixels onto a blank canvas).
- Swing uses AWT internally for event handling and top-level containers (`JFrame` inherits from AWT's `Frame`).

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
