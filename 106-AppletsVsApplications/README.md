# 106 — Applets vs Applications

> 📦 **Phase 8 — Applets & AWT** (Legacy)

## 🎯 What is it?
A very common exam comparison question.

## ⚖️ Comparison Table

| Feature | Java Application | Java Applet |
|---------|------------------|-------------|
| **Execution** | Runs standalone via `java` command. | Runs inside a web browser or `appletviewer`. |
| **Entry Point** | Requires `public static void main(String[] args)`. | Does NOT have a `main()` method. Uses `init()`. |
| **Security** | Full access to local system (can read/write files). | Runs in a restricted "sandbox". Cannot access local files by default. |
| **Network** | Can connect to any server. | Can only connect back to the server it was downloaded from. |
| **Installation** | Must be installed/downloaded manually. | Downloaded automatically when opening a webpage. |

## 📝 Exam Tips
- The lack of a `main()` method in applets is the most critical programmatic difference.
- Security restrictions (the Sandbox model) were the primary feature of applets to protect web users from malicious code.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java Applets ran in sandboxed browser environments, while Applications ran freely on the desktop. C++ applications always run directly on the OS.**
