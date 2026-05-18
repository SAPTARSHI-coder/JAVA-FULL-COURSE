# 006 — Block Scope

## 1. Definition and Core Concept

In Java, a **block** is a group of zero or more statements enclosed within curly braces `{ ... }`. 
**Block Scope** is a highly specific sub-category of local scope. It dictates that any variable declared *inside* a block is completely invisible and inaccessible *outside* of that block.

Blocks are typically associated with:
* Control flow statements (`if`, `else`, `switch`)
* Loops (`for`, `while`, `do-while`)
* Standalone initialization blocks.

When the execution flow leaves the block, the memory allocated for variables declared inside it is immediately freed.

---

## 2. Code Examples

### `if` Statement Block Scope
```java
public class BlockScopeDemo {
    public static void main(String[] args) {
        int x = 10; // Accessible anywhere in main()
        
        if (x == 10) {
            int y = 20; // Block-scoped variable
            System.out.println("x and y: " + x + " " + y); // Works fine
        }
        
        // System.out.println(y); // COMPILE ERROR: 'y' is out of scope!
    }
}
```

### `for` Loop Block Scope
```java
public class LoopScope {
    public static void main(String[] args) {
        // 'i' is declared inside the loop signature, it is block-scoped
        for (int i = 0; i < 3; i++) {
            System.out.println("Iteration: " + i);
        }
        
        // System.out.println("Final i: " + i); // COMPILE ERROR!
        
        
        // To access 'i' outside, declare it BEFORE the loop:
        int j;
        for (j = 0; j < 3; j++) {
            // do something
        }
        System.out.println("Final j: " + j); // Works! Output: 3
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Variable Redeclaration:** You cannot declare a variable inside an inner block if a variable with the exact same name already exists in the outer local scope.
  ```java
  int a = 5;
  {
      // int a = 10; // ERROR: Variable 'a' is already defined in scope
  }
  ```
  *(Note: This differs from shadowing instance variables, which is allowed).*

* **Accidental Scope Restriction:** Beginners often declare a variable inside a `try` block, and then attempt to use it in a `catch` or `finally` block, which causes an out-of-scope error.
  ```java
  try {
      String fileData = readFile();
  } catch (Exception e) {
      // System.out.println(fileData); // ERROR: fileData is out of scope!
  }
  ```

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Trace the curly braces! Exam questions often feature nested blocks to trick you into accessing a variable that has already "died".

* **Takeaway 1:** Variables declared inside loops, `if` statements, or simple curly braces `{}` die the moment the closing brace `}` is reached.
* **Takeaway 2:** If you need the result of a loop or conditional block later in the method, you must declare the variable *before* opening the block.

---

## ⚔️ Java vs C++ (Key Differences)

> **In Java, you cannot shadow a local variable from an outer block in an inner block. C++ allows inner blocks to declare variables with the same name, shadowing the outer ones.**
