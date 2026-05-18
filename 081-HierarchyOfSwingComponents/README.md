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

## ⚔️ Java vs C++ (Key Differences)

> **Java's Swing provides a deeply nested inheritance hierarchy inheriting from `JComponent`. C++ GUI libraries (like Qt) have similar hierarchies, but they are third-party, not built-in.**
