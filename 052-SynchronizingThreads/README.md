# 052 — Synchronizing Threads

> 📦 **Phase 5 — Multithreading**

## 🎯 What is it?
When multiple threads access **shared data** simultaneously, they can corrupt it. This is called a **race condition**.

**`synchronized`** keyword ensures only **one thread at a time** executes a block of code (mutual exclusion using a lock/monitor).

## 💻 Code Example

```java
class Counter {
    private int count = 0;

    // WITHOUT synchronized — race condition!
    void incrementUnsafe() {
        count++;  // not atomic: read → add → write
    }

    // WITH synchronized — thread-safe
    synchronized void increment() {
        count++;
    }

    int getCount() { return count; }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter c = new Counter();

        // 1000 threads each increment 1000 times = should be 1,000,000
        Thread[] threads = new Thread[1000];
        for (int i = 0; i < 1000; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 1000; j++) {
                    c.increment();  // thread-safe
                }
            });
            threads[i].start();
        }

        // Wait for all threads to finish
        for (Thread t : threads) t.join();

        System.out.println("Expected: 1000000");
        System.out.println("Actual:   " + c.getCount());
    }
}
```

**Output:**
```
Expected: 1000000
Actual:   1000000
```
*(Without `synchronized`, actual would be less than 1000000 — race condition)*

## 💻 Synchronized Block (more granular)

```java
synchronized (this) {
    // only this block is locked, not the whole method
    count++;
}
```

## 📝 Exam Tips
- `synchronized` → acquires **intrinsic lock (monitor)** on the object
- Only one thread holds the lock at a time — others wait (BLOCKED state)
- `synchronized` method = locks on `this` object
- `static synchronized` method = locks on the **class** object
- **Deadlock**: two threads waiting for each other's lock forever

