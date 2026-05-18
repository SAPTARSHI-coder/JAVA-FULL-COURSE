# 108 — Passing Parameters to Applets

## 1. Definition and Core Concept

Because Applets do not have a `main(String[] args)` method, you cannot pass command-line arguments to them when they start. 

Instead, Applets are embedded directly into HTML web pages. If you want to configure an Applet dynamically (e.g., telling the Applet what background color to use, or what username to display), you must pass that data from the **HTML file** into the **Java code**.

This is achieved using the `<param>` tag in HTML and the `getParameter()` method in Java.

---

## 2. The HTML Configuration

In the legacy HTML syntax used to embed Applets, you use the `<applet>` tag to define the Java class, and place `<param>` tags inside it.

A parameter consists of two parts:
1. `name`: The key/identifier for the variable.
2. `value`: The actual data (always passed as a String).

### Example HTML File (`index.html`)
```html
<html>
<body>
    <!-- Define the Applet class and dimensions -->
    <applet code="GreetingApplet.class" width="400" height="200">
        
        <!-- Pass parameters into the Applet! -->
        <param name="username" value="Alice">
        <param name="fontSize" value="24">
        
    </applet>
</body>
</html>
```

---

## 3. Retrieving Parameters in Java

Inside your Java Applet code, you retrieve these values using the built-in `getParameter(String name)` method. 

**Critical Rules:**
1. You should always read parameters inside the `init()` method, as this is when the Applet is setting itself up.
2. `getParameter()` **always returns a String**. If you passed a number (like `"24"`), you must manually parse it into an integer in your Java code.
3. If the HTML file is missing the parameter, `getParameter()` will return `null`. You must always provide a fallback/default value!

### Code Example: The Java Applet
```java
import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Font;

public class GreetingApplet extends Applet {

    private String user;
    private int size;

    @Override
    public void init() {
        // 1. Retrieve the String parameter
        user = getParameter("username");
        if (user == null) {
            user = "Guest"; // Fallback if missing in HTML
        }

        // 2. Retrieve and parse the Integer parameter
        String sizeParam = getParameter("fontSize");
        if (sizeParam != null) {
            size = Integer.parseInt(sizeParam);
        } else {
            size = 12; // Default font size
        }
    }

    @Override
    public void paint(Graphics g) {
        // Use the parsed parameters to draw the UI!
        Font customFont = new Font("Arial", Font.BOLD, size);
        g.setFont(customFont);
        g.drawString("Welcome, " + user + "!", 50, 50);
    }
}
```

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** What happens if you call `Integer.parseInt(getParameter("age"))` and the HTML file forgot to include the `age` parameter?
> It will throw a `NumberFormatException` because `getParameter()` returns `null`, and `Integer.parseInt(null)` crashes! Always check for `null` first.

* **Takeaway 1:** Parameters bridge the gap between the HTML webpage and the compiled Java code.
* **Takeaway 2:** Parameters are defined in HTML using `<param name="..." value="...">`.
* **Takeaway 3:** `getParameter()` is used in the `init()` method and strictly returns `String` data.

