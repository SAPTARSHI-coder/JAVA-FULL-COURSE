# 065 — Random Class

> 📦 **Phase 6 — Collections (Utility)**

## 🎯 What is it?
`java.util.Random` generates **pseudo-random numbers**. Useful for games, simulations, testing.

Also available: `Math.random()` (simpler, returns `double` 0.0 to 1.0).

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Random rand = new Random();

        // Random int (any range)
        System.out.println("Random int: " + rand.nextInt());

        // Random int 0 to 9 (0 inclusive, 10 exclusive)
        System.out.println("0-9: " + rand.nextInt(10));

        // Random int in custom range [min, max]
        int min = 50, max = 100;
        int value = rand.nextInt(max - min + 1) + min;
        System.out.println("50-100: " + value);

        // Random double 0.0 to 1.0
        System.out.println("Double: " + rand.nextDouble());

        // Random boolean
        System.out.println("Boolean: " + rand.nextBoolean());

        // Seeded random (same seed = same sequence, useful for testing)
        Random seeded = new Random(42);
        System.out.print("Seeded: ");
        for (int i = 0; i < 5; i++) {
            System.out.print(seeded.nextInt(10) + " ");
        }
        System.out.println();

        // Math.random() — simple way (returns 0.0 to 1.0)
        int dice = (int)(Math.random() * 6) + 1;  // 1 to 6
        System.out.println("Dice roll: " + dice);
    }
}
```

**Output (example — random values differ each run):**
```
Random int: -1324857234
0-9: 7
50-100: 73
Double: 0.4821637...
Boolean: true
Seeded: 0 7 0 2 4
Dice roll: 4
```

## 📝 Exam Tips
- `nextInt(n)` → 0 to n-1
- Range `[a, b]`: `rand.nextInt(b - a + 1) + a`
- Same seed → always same sequence (deterministic)
- `Math.random()` → double [0.0, 1.0) — quick and simple
- `SecureRandom` → cryptographically secure (use for passwords, tokens)

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
