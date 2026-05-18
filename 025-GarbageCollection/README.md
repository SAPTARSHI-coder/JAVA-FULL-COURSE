# 025 — Garbage Collection

## 1. Definition and Core Concept

In older languages like C or C++, developers are forced to manually allocate memory when creating objects, and explicitly free (destroy) that memory when they are done using it. Forgetting to free memory causes "Memory Leaks" which crash applications.

Java removes this burden through **Garbage Collection (GC)**. 
Garbage Collection is an automated background process (a daemon thread) managed by the Java Virtual Machine (JVM) that automatically reclaims memory by destroying objects that are no longer being used by the program.

### How Does it Know What to Destroy?
An object becomes eligible for Garbage Collection when it becomes **unreachable**. An object is unreachable if there are no longer any active references pointing to it in the code.

---

## 2. Ways an Object Becomes Unreachable

```java
public class GCDemo {
    public static void main(String[] args) {
        
        // Scenario 1: Nullifying a reference
        Student s1 = new Student("Alice");
        s1 = null; // The Alice object is now unreachable. GC will destroy it.
        
        // Scenario 2: Reassigning a reference
        Student s2 = new Student("Bob");
        Student s3 = new Student("Charlie");
        s2 = s3; // s2 now points to Charlie. The Bob object is now unreachable!
        
        // Scenario 3: Anonymous Objects
        // We create an object, call a method, and never store a reference to it.
        // It becomes unreachable instantly after the line executes.
        new Student("Dave").doHomework();
        
        // Scenario 4: Local Scope dies
        createStudent(); 
    }
    
    public static void createStudent() {
        Student local = new Student("Eve");
        // When this method ends, 'local' goes out of scope. The Eve object is stranded and dies.
    }
}
```

---

## 3. Important Concepts and Pitfalls

* **You cannot force the GC to run:** You can politely request the JVM to run the Garbage Collector by calling `System.gc()`, but it is strictly a *request*. The JVM guarantees nothing and runs the GC on its own optimized schedule.
* **The `finalize()` Method (Deprecated):** Previously, developers could write a `finalize()` method inside their class, which the GC would call right before destroying the object. Due to unpredictability and performance issues, it was heavily discouraged and is officially deprecated in modern Java. Use `try-with-resources` instead for cleanup.
* **Memory Leaks in Java:** Yes, memory leaks still exist in Java! If you put objects into a `static List` and forget to remove them when you're done, the List holds a valid reference to them forever. The GC will never clean them up, eventually causing an `OutOfMemoryError`.

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Exam questions often show you a snippet of code and ask "How many objects are eligible for Garbage Collection at line X?". Trace the references carefully. If an object has no variable pointing to it, it counts as eligible.

* **Takeaway 1:** Garbage Collection happens automatically on the Heap memory area.
* **Takeaway 2:** GC prevents standard memory leaks, but it cannot prevent logical memory leaks caused by sloppy list management.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
