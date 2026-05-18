# 056 — Generics

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
**Generics** allow you to write classes and methods that work with **any type** while maintaining **type safety** at compile time.

Without generics: store `Object`, cast manually, runtime errors possible.  
With generics: specify type, no casting needed, errors at compile time.

## 💻 Code Example

```java
import java.util.*;

public class Main {

    // Generic method
    static <T> void printArray(T[] arr) {
        for (T item : arr) System.out.print(item + " ");
        System.out.println();
    }

    // Generic class
    static class Box<T> {
        private T value;
        Box(T value) { this.value = value; }
        T getValue() { return value; }
        @Override public String toString() { return "Box[" + value + "]"; }
    }

    public static void main(String[] args) {
        // Generic method with different types
        Integer[] nums = {1, 2, 3, 4};
        String[] words = {"Java", "is", "fun"};
        printArray(nums);
        printArray(words);

        // Generic class
        Box<Integer> intBox = new Box<>(42);
        Box<String> strBox = new Box<>("Hello");
        System.out.println(intBox);
        System.out.println(strBox);

        // Collections with generics (type-safe)
        List<String> names = new ArrayList<>();
        names.add("Alice");
        names.add("Bob");
        // names.add(123);  // COMPILE ERROR — type safe!
        String name = names.get(0);  // no casting needed
        System.out.println(name.toUpperCase());
    }
}
```

**Output:**
```
1 2 3 4
Java is fun
Box[42]
Box[Hello]
ALICE
```

## 📝 Exam Tips
- `<T>` = type parameter (can be any letter, `T` by convention)
- `List<String>` → can only hold Strings (type-safe)
- **Bounded types**: `<T extends Number>` → T must be Number or subclass
- `<?>` = wildcard (any type) → `List<?>` = list of unknown type
- Generics are erased at runtime (type erasure) — all become `Object`

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
