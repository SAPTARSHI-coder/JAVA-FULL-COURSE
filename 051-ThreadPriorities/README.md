# 051 — Thread Priorities

## 1. Definition and Core Concept

In a multithreaded environment, multiple threads compete for limited CPU time. The OS uses a component called the **Thread Scheduler** to decide which thread gets to run next.

While Java cannot strictly control the OS Thread Scheduler, it allows developers to provide "hints" about which threads are more important by setting a **Thread Priority**.

### The Priority Range
In Java, thread priorities are represented by integer values ranging from `1` to `10`.
* **`Thread.MIN_PRIORITY` (1):** The lowest priority.
* **`Thread.NORM_PRIORITY` (5):** The default priority assigned to all newly created threads.
* **`Thread.MAX_PRIORITY` (10):** The highest priority.

---

## 2. Code Examples

### Setting and Getting Priority
```java
class CountingTask implements Runnable {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(Thread.currentThread().getName() + " is counting: " + i);
        }
    }
}

public class PriorityDemo {
    public static void main(String[] args) {
        Thread lowThread = new Thread(new CountingTask(), "Low-Priority-Thread");
        Thread highThread = new Thread(new CountingTask(), "High-Priority-Thread");
        
        // Changing priorities before starting the threads
        lowThread.setPriority(Thread.MIN_PRIORITY); // Sets to 1
        highThread.setPriority(Thread.MAX_PRIORITY); // Sets to 10
        
        // Note: Even though we start lowThread first, highThread will likely finish faster.
        lowThread.start();
        highThread.start();
    }
}
```

---

## 3. How Priorities Actually Work (The Pitfall)

The most important concept to understand about Java Thread Priorities is that **they are merely suggestions, not guarantees.**

Java delegates thread scheduling to the underlying Operating System (Windows, macOS, Linux). 
* Some OS schedulers might completely ignore the priority hints provided by Java. 
* Some OS schedulers use a time-slicing algorithm (Round Robin) where even priority 1 threads get equal CPU time, they just get picked slightly less often.
* Because priorities map differently on Windows (which has 7 priority levels) vs Linux, relying on `setPriority()` can make your application behave completely differently depending on the operating system it runs on!

**Best Practice:** Never design your program's core logic to depend on Thread Priorities. If Thread A *must* finish before Thread B starts, use `Thread.join()` or `CountDownLatch`, do NOT just set Thread A to priority 10.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions often feature an `IllegalArgumentException` trap. If you attempt to call `t.setPriority(11)` or `t.setPriority(0)`, Java will throw an exception. The value MUST be between 1 and 10 inclusive.

* **Takeaway 1:** Default priority is 5.
* **Takeaway 2:** A newly created thread automatically inherits the priority of the thread that created it. (e.g., If the main thread is priority 8, any threads created inside `main` will start at priority 8).
* **Takeaway 3:** Priorities are platform-dependent suggestions. They do not guarantee execution order.

