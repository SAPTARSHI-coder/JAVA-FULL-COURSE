# 054 — Producer Consumer Pattern

> 📦 **Phase 5 — Multithreading**

## 🎯 What is it?
Classic multithreading design pattern:
- **Producer** creates data and puts it in a shared buffer
- **Consumer** takes data from the buffer and processes it
- They run **independently** — buffer decouples them

Uses `wait()` / `notify()` or `BlockingQueue` (modern way).

## 💻 Code Example — Using BlockingQueue (recommended)

```java
import java.util.concurrent.*;

public class Main {
    static BlockingQueue<Integer> queue = new LinkedBlockingQueue<>(5); // max 5 items

    public static void main(String[] args) {
        Thread producer = new Thread(() -> {
            try {
                for (int i = 1; i <= 10; i++) {
                    queue.put(i);  // blocks if queue full
                    System.out.println("Produced: " + i + " | Queue size: " + queue.size());
                    Thread.sleep(100);
                }
            } catch (InterruptedException e) { e.printStackTrace(); }
        });

        Thread consumer = new Thread(() -> {
            try {
                for (int i = 1; i <= 10; i++) {
                    int val = queue.take();  // blocks if queue empty
                    System.out.println("  Consumed: " + val);
                    Thread.sleep(300);  // slower than producer
                }
            } catch (InterruptedException e) { e.printStackTrace(); }
        });

        producer.start();
        consumer.start();
    }
}
```

**Output (excerpt):**
```
Produced: 1 | Queue size: 1
  Consumed: 1
Produced: 2 | Queue size: 1
Produced: 3 | Queue size: 2
  Consumed: 2
Produced: 4 | Queue size: 2
...
```

## 📝 Exam Tips
- **Producer**: generates data | **Consumer**: processes data
- Buffer prevents producer from overwhelming consumer
- `BlockingQueue.put()` → blocks when full | `take()` → blocks when empty
- Classic implementation uses `wait()` + `notify()` on shared object
- Real examples: print queue, message queue, pipeline processing


---

## ⚔️ Java vs C++ (Key Differences)

> **Both implement this similarly, but Java often uses built-in collections like `BlockingQueue`, whereas C++ devs often build it manually using `std::queue`, mutexes, and condition variables.**
