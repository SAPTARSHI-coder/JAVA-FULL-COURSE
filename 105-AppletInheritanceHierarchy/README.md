# 105 — Applet Inheritance Hierarchy

> 📦 **Phase 8 — Applets & AWT** (Legacy)

## 🎯 What is it?
This defines exactly where the `Applet` class sits in the Java class hierarchy.

## 🌳 The Hierarchy

```
java.lang.Object
   └── java.awt.Component         (Has graphical representation)
         └── java.awt.Container   (Can hold other components)
               └── java.awt.Panel (Provides space for an application to attach)
                     └── java.applet.Applet 🌟
                           └── javax.swing.JApplet (Swing version)
```

## 📝 Exam Tips
- Because `Applet` extends `Panel`, it is a `Container` and can hold buttons, text fields, etc.
- Because it extends `Panel` rather than `Window`, it **does not have a title bar or close button**. It relies on the browser/viewer to provide the window frame.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java Applets inherit from `java.applet.Applet` (AWT) or `JApplet` (Swing). C++ has no native concept of a web "Applet" hierarchy, as it traditionally compiles to desktop executables.**
