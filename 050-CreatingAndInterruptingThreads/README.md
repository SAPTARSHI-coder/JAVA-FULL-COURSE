# 050 — Creating and Interrupting Threads

## 1. Definition and Core Concept

In Java, there are two primary ways to create a new thread of execution:
1. **Extend the `Thread` class**
2. **Implement the `Runnable` interface** (This is the highly preferred and most common method).

Regardless of how you create it, the logic that the thread will execute MUST be placed inside a method named **`run()`**.

---

## 2. Creating a Thread

### Method 1: Implementing `Runnable` (Best Practice)
Why is this preferred? Because Java only supports single inheritance. If you extend `Thread`, your class cannot extend any other class. By implementing `Runnable`, your class is free to inherit from another business class.

```java
// 1. Create a class that implements Runnable
class MyTask implements Runnable {
    @Override
    public void run() {
        // The code that will execute on the new thread
        System.out.println("Background thread is running!");
    }
}

public class RunnableDemo {
    public static void main(String[] args) {
        // 2. Instantiate the task
        MyTask task = new MyTask();
        
        // 3. Create a Thread object and pass the task to it
        Thread worker = new Thread(task);
        
        // 4. Start the thread (This transitions it from NEW to RUNNABLE)
        worker.start(); 
        
        System.out.println("Main thread finishes.");
    }
}
```

### Method 2: Extending `Thread`
```java
// 1. Extend Thread
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Background thread running!");
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        // 2. Instantiate and start
        MyThread worker = new MyThread();
        worker.start(); 
    }
}
```

---

## 3. Interrupting a Thread

In the old days of Java, there was a `stop()` method to instantly kill a thread. It was deprecated because killing a thread mid-process often left data corrupted. 

Today, we use a polite mechanism called **Interruption**. You "interrupt" a thread to ask it nicely to stop what it's doing and shut down.

```java
class SleeperTask implements Runnable {
    public void run() {
        try {
            System.out.println("Going to sleep for 10 seconds...");
            Thread.sleep(10000); // Thread enters TIMED_WAITING
            System.out.println("Woke up naturally.");
        } catch (InterruptedException e) {
            // The sleep was interrupted! Time to clean up and exit.
            System.out.println("I was rudely interrupted! Shutting down.");
        }
    }
}

public class InterruptDemo {
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(new SleeperTask());
        t.start();
        
        Thread.sleep(2000); // Main thread waits 2 seconds
        
        System.out.println("Interrupting the background thread...");
        t.interrupt(); // Sets the interrupt flag on 't'. 
                       // Because 't' is sleeping, this triggers an InterruptedException.
    }
}
```

---

## 4. Common Mistakes or Pitfalls

* **Calling `run()` instead of `start()`:** This is a classic beginner mistake. If you call `worker.run()`, the code will execute, but it will execute sequentially on the *main* thread. The OS will NOT create a new background thread. You must call `worker.start()` to spin up a new thread.

---

## 5. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be absolutely certain you know the difference between `start()` and `run()`. `start()` spins up a new thread and then internally calls `run()`.

* **Takeaway 1:** Prefer implementing `Runnable` over extending `Thread`.
* **Takeaway 2:** A thread will not stop just because you call `interrupt()`. If the thread is running heavy calculation loops and never checks its interrupt status (or never goes to sleep), it will completely ignore the interruption and keep running forever.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
