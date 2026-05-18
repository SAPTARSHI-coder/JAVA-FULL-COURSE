# 061 — Stack

> 📦 **Phase 6 — Collections**

## 🎯 What is it?
`Stack` is a **LIFO** (Last In, First Out) collection — like a stack of plates. The last item added is the first to be removed.

`Stack` extends `Vector` (legacy, thread-safe). For modern use, prefer `Deque` (`ArrayDeque`).

## 💻 Code Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        // push — add to top
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Stack: " + stack);      // [10, 20, 30]

        // peek — view top without removing
        System.out.println("Peek: " + stack.peek()); // 30

        // pop — remove from top
        System.out.println("Pop: " + stack.pop());   // 30
        System.out.println("Pop: " + stack.pop());   // 20
        System.out.println("Stack: " + stack);       // [10]

        // search — 1-based position from top
        stack.push(20);
        stack.push(30);
        System.out.println("Search 20: " + stack.search(20)); // 2 (2nd from top)
        System.out.println("Is empty: " + stack.isEmpty());   // false

        // Real use: check balanced parentheses
        System.out.println("Balanced: " + isBalanced("({[]})"));
        System.out.println("Balanced: " + isBalanced("({[})"));
    }

    static boolean isBalanced(String s) {
        Stack<Character> st = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') st.push(c);
            else {
                if (st.isEmpty()) return false;
                char top = st.pop();
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        return st.isEmpty();
    }
}
```

**Output:**
```
Stack: [10, 20, 30]
Peek: 30
Pop: 30
Pop: 20
Stack: [10]
Search 20: 2
Is empty: false
Balanced: true
Balanced: false
```

## 📝 Exam Tips
- LIFO = Last In First Out
- `push()` → add | `pop()` → remove top | `peek()` → view top
- `search()` returns 1-based position from top (-1 if not found)
- Classic use: undo operations, expression evaluation, balanced brackets

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
