# 048 — Processes vs. Threads

## 1. Definition and Core Concept

Modern operating systems are capable of running many programs at once (multitasking). In Java, when we talk about multitasking, we distinguish between two fundamental units of execution: **Processes** and **Threads**.

### What is a Process?
A process is a standalone, heavy-weight execution environment. It is an independent program running on the OS.
* **Memory:** Every process has its own completely separate, dedicated block of memory.
* **Communication:** Processes cannot easily share data with each other. They must use Inter-Process Communication (IPC) like network sockets or pipes, which is slow.
* *Example:* Opening Google Chrome creates a new process. Opening MS Word creates another process.

### What is a Thread?
A thread is a lightweight sub-process. It is the smallest unit of execution within a Process. A single Process can contain hundreds of Threads.
* **Memory:** All threads *within the same process* share the same memory space (the Heap). 
* **Communication:** Because they share memory, threads can communicate with each other incredibly fast by simply reading/writing the same variables.
* *Example:* Inside the MS Word process, one thread registers your keystrokes, a second thread runs spell-check in the background, and a third thread auto-saves the document to the disk.

---

## 2. Multithreading in Java

Java was one of the first mainstream languages to have multithreading built directly into the core language. The JVM acts as a Process, and every Java application runs at least one Thread (the `main` thread).

### Why use Threads instead of multiple Processes?
1. **Speed of Creation:** Creating a new thread takes far less CPU time and memory than spinning up an entirely new OS process.
2. **Resource Sharing:** Because threads share the JVM Heap, they can easily access the same objects.
3. **Responsiveness:** In UI applications (like Android or JavaFX), putting heavy tasks (like downloading a file) on a background thread keeps the main UI thread responsive so the app doesn't freeze.

---

## 3. The Danger of Shared Memory (Concurrency)

Because threads share the same memory space, multithreading introduces a massive new category of bugs known as **Concurrency Issues**.

If Thread A is trying to read a bank balance variable at the *exact same microsecond* that Thread B is trying to update it, the data can become corrupted (a Race Condition).

*Note: This is why we have concepts like Synchronization, Locks, and Thread-Safe classes (covered in later topics).*

---

## 4. Exam Tips and Key Takeaways

> [!IMPORTANT]
> **Exam Focus:** Expect theoretical questions asking about memory isolation. Memorize this fact: **Processes have independent memory. Threads share memory.**

* **Takeaway 1:** Threads are "lightweight"; Processes are "heavyweight".
* **Takeaway 2:** A Java application terminates when all of its non-daemon threads finish executing. The `main` thread is just the first thread; it can die, and if a background thread is still running, the application stays alive.

