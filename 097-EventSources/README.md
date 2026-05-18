# 097 — Event Sources

> 📦 **Phase 10 — Event Handling**

## 🎯 What is it?
An **Event Source** is the object that generates an event. 
This occurs when the internal state of that object changes in some way.

## 📦 Common Event Sources

| Component | Event Generated | Trigger Action |
|-----------|-----------------|----------------|
| `JButton` | `ActionEvent` | Button is clicked |
| `JTextField` | `ActionEvent` | User presses Enter key inside the field |
| `JCheckBox` | `ItemEvent` | User checks or unchecks the box |
| `Choice` / `JComboBox` | `ItemEvent` | User selects an item from the dropdown |
| `JFrame` / `Window` | `WindowEvent` | Window is opened, closed, minimized |
| Any Component | `MouseEvent` | Mouse is clicked, pressed, released, enters, exits |
| Any Component | `KeyEvent` | Key is typed, pressed, or released |

## 📝 Exam Tips
- The Source is responsible for registering Listeners (using methods like `addActionListener()`).
- A Source can have multiple Listeners attached to it. When an event occurs, ALL attached listeners are notified.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
