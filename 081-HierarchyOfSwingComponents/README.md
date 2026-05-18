# 081 — Hierarchy of Swing Components

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
Swing components inherit heavily from AWT classes. The true base class for all Swing GUI elements is `JComponent`.

## 🌳 The Hierarchy

```
Object (java.lang)
  └── Component (java.awt)  [Abstract]
        ├── Container (java.awt)
        │     ├── Window (java.awt)
        │     │     ├── Frame (java.awt)  →  JFrame (javax.swing)
        │     │     └── Dialog (java.awt) →  JDialog (javax.swing)
        │     │
        │     └── JComponent (javax.swing)  [Abstract] 🌟 Heart of Swing
        │           ├── AbstractButton
        │           │     ├── JButton
        │           │     ├── JToggleButton (JCheckBox, JRadioButton)
        │           │     └── JMenuItem
        │           ├── JTextComponent
        │           │     ├── JTextField
        │           │     └── JTextArea
        │           ├── JLabel
        │           ├── JPanel
        │           └── (Many more like JTable, JTree, JComboBox)
```

## 📝 Exam Tips
- Top-level containers like `JFrame` and `JDialog` inherit directly from AWT `Window` / `Frame`. They are heavyweight containers.
- All other Swing components (buttons, labels, text fields) inherit from `JComponent`. They are lightweight.
- `JComponent` inherits from AWT's `Container`.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
