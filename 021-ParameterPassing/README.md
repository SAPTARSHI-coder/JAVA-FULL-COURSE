# 021 — Parameter Passing (Pass-by-Value)

## 1. Definition and Core Concept

In Java, when you pass a variable to a method, you are passing its **value**. Java is strictly **Pass-by-Value**. It never passes the actual variable itself (Pass-by-Reference), though the behavior can seem confusing when passing objects.

### 1. Passing Primitives
When you pass a primitive (like `int` or `double`), Java creates a brand new copy of that value and hands it to the method. Changes made inside the method do **not** affect the original variable.

### 2. Passing Objects (References)
When you pass an object (like an array or a class instance), you are passing a copy of the *reference* (the memory address). 
* Because the copy points to the exact same object in the heap, modifying the object's properties inside the method *will* affect the original object.
* However, if you try to reassign the reference to a completely new object, the original reference remains unchanged.

---

## 2. Code Examples

### Passing Primitives (Copy of the Data)
```java
public class PassPrimitive {
    public static void modifyNumber(int x) {
        x = x * 2; // Modifying the local copy
        System.out.println("Inside method: " + x); // 20
    }

    public static void main(String[] args) {
        int myNum = 10;
        modifyNumber(myNum);
        
        // The original variable remains completely unchanged
        System.out.println("In main: " + myNum); // 10
    }
}
```

### Passing Objects (Copy of the Reference)
```java
class Student {
    String name;
}

public class PassObject {
    public static void modifyStudent(Student s) {
        // This modifies the object that both references point to!
        s.name = "Alice"; 
        
        // This attempts to overwrite the copied reference (Fails to affect main)
        s = new Student();
        s.name = "Bob"; 
    }

    public static void main(String[] args) {
        Student myStudent = new Student();
        myStudent.name = "John";
        
        modifyStudent(myStudent);
        
        // The object's data was changed by the method!
        System.out.println("In main: " + myStudent.name); // Outputs: Alice
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Believing Java is Pass-by-Reference:** C++ and C# allow true pass-by-reference (using pointers or `ref` keywords). Java does not. You cannot write a swap method `swap(int a, int b)` in Java that permanently swaps two primitive variables passed into it.
* **Assuming Strings will mutate:** Because Strings are objects, beginners assume passing a String to a method allows the method to change it. But because Strings are *immutable*, any change creates a new object and points the local reference to it, leaving the original String unchanged.

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions heavily test object modification vs. object reassignment. If a method does `param.field = 5;`, the original changes. If the method does `param = new Object();`, the original does NOT change.

* **Takeaway 1:** "Pass-by-value" literally means "Pass-by-copy". 
* **Takeaway 2:** When passing arrays, since an array is an object, modifying `array[0]` inside a method will modify the original array back in `main()`.

---

## ⚔️ Java vs C++ (Key Differences)

> **Java uses pass-by-value strictly (passing object references by value), whereas C++ allows pass-by-value, pass-by-reference (`&`), and pass-by-pointer (`*`).**
