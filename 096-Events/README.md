# 096 — Events

> 📦 **Phase 10 — Event Handling**

## 🎯 What is it?
An **Event** is a change in the state of an object. In GUI programming, an event is generated when the user interacts with a graphical component.

**Examples of Events:**
- Clicking a button
- Typing in a text field
- Moving the mouse
- Closing a window

## 🔄 The Delegation Event Model
Java handles events using the **Delegation Event Model**. It has three key players:
1. **Event Source**: The UI component that generates the event (e.g., a `JButton`).
2. **Event Object**: An object containing information about the event (e.g., `ActionEvent`).
3. **Event Listener**: The code that waits for the event to happen and processes it (e.g., `ActionListener`).

## 📝 Exam & Viva Questions
**Q: What is an Event?**  
A: An event represents a change in state or a user action on a component.

**Q: What is the Delegation Event Model?**  
A: A model where an Event Source generates an Event Object, and passes it to one or more registered Event Listeners to handle it.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java Events are strongly-typed objects derived from `java.util.EventObject`. C++ events are typically handled via pointers to event objects, callback functions (`std::function`), or the publisher-subscriber pattern.**
