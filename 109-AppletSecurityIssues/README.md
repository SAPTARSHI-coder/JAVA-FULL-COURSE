# 109 — Applet Security Issues

## 1. Definition and Core Concept

Applets were designed to be downloaded from the internet and executed immediately on a user's local machine inside their web browser. 

Imagine visiting a random website and it automatically downloads and runs an executable program on your computer. That is a massive security risk! A malicious applet could easily format your hard drive, steal your personal files, or launch network attacks.

To prevent this, Java forces all Applets to run inside a highly restricted environment known as the **Applet Sandbox**.

---

## 2. The Sandbox Restrictions

The Sandbox is a strict security manager that completely isolates the Applet from the underlying Operating System. By default, an untrusted (unsigned) Applet is blocked from doing almost everything except drawing to the screen.

### What an Applet CANNOT do:
1. **File System Access:** It cannot read, write, delete, or modify any files on the user's local hard drive.
2. **Network Restrictions:** It cannot make network connections to *any* server except the exact host server it was downloaded from. (e.g., If the applet came from `google.com`, it cannot open a socket to `yahoo.com`).
3. **Execution Limits:** It cannot start local executable programs (like opening `cmd.exe` or the Calculator).
4. **System Properties:** It cannot read sensitive system properties like the user's username or the `user.dir` file path.
5. **Native Code:** It cannot load native libraries (like C/C++ `.dll` files).

### What an Applet CAN do:
1. Draw UI components to the browser screen.
2. Play audio files.
3. Communicate back to the server it originated from.
4. Read public system properties (like the Java version or OS name).

---

## 3. Escaping the Sandbox: Signed Applets

What if you *want* to build a legitimate web application (like a browser-based word processor) that needs to save files to the user's hard drive?

To escape the Sandbox, the Applet must be **Digitally Signed**.
1. The developer purchases a Digital Certificate from a trusted authority (like VeriSign).
2. The developer signs the `.jar` file containing the Applet.
3. When the user visits the webpage, the browser displays a dramatic warning popup: *"Do you want to run this application? Publisher: Trusted Corp."*
4. If the user clicks **"Accept/Run"**, the Sandbox restrictions are completely lifted, and the Applet is granted full access to the user's computer, just like a normal desktop application.

---

## 4. The Death of Applets

Over time, hackers continuously found loopholes to break out of the Java Sandbox without the user clicking "Accept." Because Java plugins were integrated so deeply into browsers, a single vulnerability allowed hackers to take over millions of computers just by tricking users into visiting a webpage.

Due to these severe, recurring security issues, major browsers (Chrome, Firefox, Edge) permanently killed support for the Java Plugin starting around 2015. Applets are now entirely obsolete in modern web development, replaced by JavaScript, HTML5, and WebAssembly.

---

## 5. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be prepared to identify which operations will throw a `SecurityException`. If an exam question shows an Applet trying to use `FileInputStream` to read `C:\passwords.txt`, the answer is always "A SecurityException is thrown at runtime."

* **Takeaway 1:** Untrusted Applets run in a strict **Sandbox** to protect the user's local machine.
* **Takeaway 2:** Sandboxed applets cannot access the local file system or connect to third-party networks.
* **Takeaway 3:** Digitally signing an applet and getting user permission lifts the sandbox restrictions.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
