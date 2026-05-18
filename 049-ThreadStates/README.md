# 049 — Thread States (The Thread Lifecycle)

## 1. Definition and Core Concept

From the moment a Thread object is created until the moment it finishes executing, it transitions through several distinct "States". The Java Virtual Machine (JVM) and the OS Thread Scheduler manage these transitions.

In Java, a thread can only be in one of **six specific states** at any given time, defined by the `Thread.State` enum.

---

## 2. The Six Thread States

### 1. NEW
The thread object has been created using the `new` keyword (e.g., `Thread t = new Thread();`), but the `t.start()` method has **not** been called yet. The thread exists in memory, but the OS hasn't allocated CPU resources for it.

### 2. RUNNABLE
The `start()` method has been called. The thread is now either actively running on the CPU, *or* it is sitting in a queue waiting for the OS Thread Scheduler to give it a fraction of a second of CPU time. (Java groups both "Running" and "Ready-to-Run" into this single state).

### 3. BLOCKED
The thread is trying to enter a `synchronized` block of code, but another thread is currently holding the lock for that block. The thread is frozen here until the lock becomes available.

### 4. WAITING
The thread is waiting indefinitely for another thread to perform a specific action. It enters this state by calling methods like `Object.wait()` or `Thread.join()` (with no timeout parameter). It will remain frozen until another thread explicitly wakes it up (e.g., via `notify()`).

### 5. TIMED_WAITING
Similar to WAITING, but it has a maximum time limit. It will wake up either when the time expires, or when it is notified. It enters this state by calling methods like `Thread.sleep(1000)` or `Object.wait(1000)`.

### 6. TERMINATED (Dead)
The thread has successfully completed the execution of its `run()` method, or it was terminated abruptly by an unhandled exception. Once a thread is TERMINATED, it can **never** be restarted.

---

## 3. The Lifecycle Diagram

```text
                  [NEW]
                    |  (start() called)
                    v
    +--------> [RUNNABLE] <----------+
    |               |                |
    |               | (sleep/wait)   | (notify/timeout)
    |               v                |
(lock acquired)  [WAITING / TIMED_WAITING / BLOCKED]
    |               
    | (run() ends)
    v
[TERMINATED]
```

---

## 4. Common Mistakes or Pitfalls

* **Trying to restart a Dead Thread:** If a thread is in the `TERMINATED` state, calling `start()` on it again will result in an `IllegalThreadStateException`. A Thread object is strictly single-use.
* **Confusing `sleep()` and `wait()`:** 
  * `sleep()` puts the thread into `TIMED_WAITING` but *keeps* any locks it holds.
  * `wait()` puts the thread into `WAITING` and *releases* any locks it holds so other threads can work.

---

## 5. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions often ask about the "RUNNING" state. Note carefully that in the official `Thread.State` enum, there is no "RUNNING" state. It is officially called `RUNNABLE`, which encompasses both actively running and waiting for CPU time.

* **Takeaway 1:** You can check the current state of any thread by calling `myThread.getState()`.
* **Takeaway 2:** A thread in the `NEW` state is just a standard Java object. It doesn't become an actual OS-level execution thread until `start()` is invoked.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
