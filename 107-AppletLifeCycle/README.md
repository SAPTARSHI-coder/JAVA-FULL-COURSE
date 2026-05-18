# 107 — Applet Life Cycle

## 1. Definition and Core Concept

Historically, Java Applets were small Java applications designed to be transmitted over the internet and executed directly inside a user's web browser. While they are officially deprecated and no longer supported in modern browsers, understanding their life cycle remains a core topic in legacy Java exams.

Unlike a standard Java application that begins execution at `public static void main(String[] args)`, an Applet is controlled entirely by the web browser (or an AppletViewer). The browser dictates when the applet starts, pauses, and dies by calling specific methods in a strict sequence.

This sequence of events is known as the **Applet Life Cycle**.

---

## 2. The Four Stages of the Life Cycle

Every Applet extends the `java.applet.Applet` class, which provides four primary life cycle methods. You override these methods to execute your code at the correct time.

### 1. `init()` (Initialization)
* **When it runs:** Called exactly **once** when the applet is first loaded into memory by the browser.
* **Purpose:** This is where you put your setup code. You initialize variables, load images or audio files, and set up your GUI components (buttons, text fields). It acts as the replacement for a standard constructor.

### 2. `start()` (Execution)
* **When it runs:** Called immediately after `init()`. It is also called every time the user maximizes the browser window or returns to the webpage after leaving it. This method can be called **multiple times**.
* **Purpose:** Used to start or resume core operations, such as starting animations or background threads.

### 3. `stop()` (Pausing)
* **When it runs:** Called when the user leaves the webpage, minimizes the browser, or switches to a different tab. It can be called **multiple times**.
* **Purpose:** Used to suspend operations. If the user isn't looking at the applet, you should stop heavy animations or pause audio to save CPU power.

### 4. `destroy()` (Termination)
* **When it runs:** Called exactly **once** when the browser is completely closed or the applet is being permanently unloaded from RAM.
* **Purpose:** Used for final cleanup. You close network connections, terminate persistent threads, and free up heavy resources before the Garbage Collector takes over.

---

## 3. The `paint()` Method

While not technically one of the four core life cycle states, the `paint()` method is fundamentally tied to the applet's execution.

* **Signature:** `public void paint(Graphics g)`
* **When it runs:** Called automatically immediately after `start()`, and repeatedly called whenever the applet needs to be redrawn (e.g., if another window overlaps the browser, or the browser is resized).
* **Purpose:** This is where you actually draw your shapes, text, and images onto the screen using the `Graphics` object.

---

## 4. Code Example: Tracing the Cycle

If you run this code and minimize/maximize the window, you will see exactly how the browser controls the flow.

```java
import java.applet.Applet;
import java.awt.Graphics;

public class LifeCycleDemo extends Applet {

    @Override
    public void init() {
        System.out.println("1. init() called - Setting up!");
    }

    @Override
    public void start() {
        System.out.println("2. start() called - Applet is visible!");
    }

    @Override
    public void paint(Graphics g) {
        System.out.println("3. paint() called - Drawing to screen!");
        g.drawString("Welcome to the Applet!", 20, 20);
    }

    @Override
    public void stop() {
        System.out.println("4. stop() called - Applet hidden/minimized!");
    }

    @Override
    public void destroy() {
        System.out.println("5. destroy() called - Shutting down forever.");
    }
}
```

---

## 5. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** "Does an Applet use a `main()` method?" 
> **No!** Applets do not have a `main()` method. The execution flow is entirely managed by the browser container calling `init()`, `start()`, and `paint()`.

* **Takeaway 1:** `init()` and `destroy()` are guaranteed to run exactly **once**.
* **Takeaway 2:** `start()` and `stop()` can run **multiple times** as the user navigates away and returns to the page.
* **Takeaway 3:** Standard applets are a legacy technology and are highly restricted due to security concerns.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java strictly defined the Applet lifecycle (`init()`, `start()`, `stop()`, `destroy()`). C++ desktop applications merely have a `main()` function serving as the entry and exit point.**
