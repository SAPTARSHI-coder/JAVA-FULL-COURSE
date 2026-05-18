# 101 — Delegation Event Model

> 📦 **Phase 10 — Event Handling**

## 🎯 What is it?
This is the formal name for Java's event handling mechanism. 

It works on the concept of **delegating** the responsibility of handling an event from the component where the event occurs (the Source) to an external object (the Listener).

## 🔄 How it Works
1. A user interacts with a GUI component (e.g., clicks a Button).
2. The Button (Event Source) generates an Event Object.
3. The Button does NOT process the click itself. Instead, it **delegates** it to a registered Listener object.
4. The Listener object executes its `actionPerformed()` method to handle the event.

## 📝 Exam & Viva Questions
**Q: Why is it called the "Delegation" Event Model?**  
A: Because the source of the event delegates the processing of the event to a separate listener object, rather than handling it internally. This separates the UI code from the application logic.

**Q: What are the three main components of this model?**  
A: Event Source (e.g., JButton), Event Object (e.g., ActionEvent), and Event Listener (e.g., ActionListener).

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
