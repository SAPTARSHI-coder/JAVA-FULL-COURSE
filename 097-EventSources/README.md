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

## ⚔️ Java vs C++ (Key Differences)

> **In Java, standard components act as Event Sources that generate event objects. C++ UI objects also act as sources, often emitting raw OS event loops converted to framework events.**
