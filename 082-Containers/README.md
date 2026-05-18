# 082 — Containers

> 📦 **Phase 9 — GUI Programming (AWT & Swing)**

## 🎯 What is it?
A **Container** is a special type of component that can hold and group other components (like buttons and text fields).
Components must be added to a container to be displayed.

## 📦 Types of Containers in Swing

1. **Top-Level Containers**: The main windows. They exist independently. They are heavyweight.
   - `JFrame`: Standard window with title, border, min/max/close buttons.
   - `JDialog`: Popup window (like an alert or settings dialog).
   - `JApplet`: Embedded in a browser (legacy).

2. **Lightweight Containers**: Placed inside top-level containers to organize layout.
   - `JPanel`: A blank area used to group other components together.
   - `JScrollPane`: Adds scrollbars to components that are too large (like text areas or tables).
   - `JTabbedPane`: Allows multiple panels to share the same space using tabs.

## 💻 Concept Example

```java
// Conceptual flow, not a full running app
JFrame frame = new JFrame();      // Top-level container
JPanel panel = new JPanel();      // Lightweight container

JButton btn = new JButton("OK");  // Component

panel.add(btn);                   // Put button inside panel
frame.add(panel);                 // Put panel inside frame
```

## 📝 Exam Tips
- You cannot place a top-level container (like `JFrame`) inside another top-level container.
- You *must* have at least one top-level container to display anything on the screen.
- Every top-level container has a `contentPane`. When you call `frame.add(button)`, you are actually adding it to the `contentPane`.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java heavily relies on explicitly adding components to `Container` objects. C++ GUI frameworks use similar parenting, but often manage memory automatically when a parent container is destroyed.**
