# 053 — Inter-Thread Communication (`wait`, `notify`, `notifyAll`)

## 1. Definition and Core Concept

Sometimes, synchronization isn't enough. You don't just need threads to stay out of each other's way; you need them to actively talk to each other. 

A classic example is the **Producer-Consumer problem**. 
* Thread A (Producer) generates data and puts it in a queue.
* Thread B (Consumer) reads data from the queue.
If the queue is empty, the Consumer needs to *wait* until data is available. If the queue is full, the Producer needs to *wait* until the Consumer clears some space.

Java handles this communication using three methods built into the root `java.lang.Object` class: **`wait()`**, **`notify()`**, and **`notifyAll()`**.

---

## 2. The Three Methods

Because these methods control the Monitor lock of an object, they **MUST** be called from inside a `synchronized` context. If you call them outside a synchronized block, Java throws an `IllegalMonitorStateException`.

1. **`wait()`:** The thread immediately releases the lock on the object and goes to sleep (enters the `WAITING` state). It sits in the object's "waiting room" until another thread wakes it up.
2. **`notify()`:** Wakes up ONE random thread that is currently waiting on this object.
3. **`notifyAll()`:** Wakes up ALL threads currently waiting on this object. (This is generally safer and preferred over `notify()`).

---

## 3. Code Example: Producer and Consumer

```java
class MessageQueue {
    private String message;
    private boolean hasMessage = false;

    // CONSUMER CALLS THIS
    public synchronized String read() {
        while (!hasMessage) {
            try {
                wait(); // Queue is empty! Release the lock and sleep.
            } catch (InterruptedException e) { }
        }
        hasMessage = false; // We read the message, queue is empty again.
        notifyAll(); // Wake up the Producer to make more!
        return message;
    }

    // PRODUCER CALLS THIS
    public synchronized void write(String msg) {
        while (hasMessage) {
            try {
                wait(); // Queue is full! Release the lock and sleep.
            } catch (InterruptedException e) { }
        }
        this.message = msg;
        hasMessage = true; // Message is ready!
        notifyAll(); // Wake up the Consumer to read it!
    }
}
```

---

## 4. Common Mistakes or Pitfalls

* **Using `if` instead of `while` for `wait()`:** Notice in the code above we used `while (!hasMessage)`. Why a while loop? Because of "Spurious Wakeups". Sometimes the OS wakes up a thread for no reason, or `notifyAll()` wakes up a thread, but before it can grab the lock, a *third* thread swoops in and steals the message. The thread must re-check the condition immediately upon waking up. **Always wrap `wait()` in a while loop.**
* **Calling `wait()` on `Thread`:** `wait()` and `notify()` are methods of `Object`, not `Thread`. You call them on the shared resource (like the `MessageQueue`), not on the thread object itself.

---

## 5. Exam Tips and Key Takeaways

> [!IMPORTANT]
> **Exam Focus:** Be absolutely sure you know that `wait()`, `notify()`, and `notifyAll()` belong to `Object`, not `Thread`. This is a classic trick question. 

* **Takeaway 1:** You can only call these methods if your thread currently owns the Monitor lock (meaning you are inside a `synchronized` block).
* **Takeaway 2:** When a thread calls `wait()`, it temporarily gives up the lock so other threads can use the object. When it wakes up, it has to re-acquire the lock before continuing.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java uses `wait()`, `notify()`, and `notifyAll()` directly on objects (Object monitors). C++ achieves this using `std::condition_variable` combined with a `std::mutex`.**
