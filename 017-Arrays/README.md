# 017 — Arrays

## 1. Definition and Core Concept

An **array** is a container object that holds a fixed number of values of a single type. The length of an array is established when the array is created. After creation, its length is fixed (immutable).

Arrays are heavily used to store multiple items of the same type without having to declare dozens of individual variables. 
* Elements are accessed using an **index** (a numerical position).
* Arrays in Java are **zero-indexed**, meaning the first element is at index `0`.
* In memory, arrays are allocated as a contiguous block, making data retrieval extremely fast.
* Because arrays are objects, they are created dynamically on the heap.

---

## 2. Code Examples

### 1. Declaring, Instantiating, and Initializing
```java
public class ArrayDemo {
    public static void main(String[] args) {
        
        // Method 1: Declare and specify size (filled with default values)
        int[] scores = new int[5]; // Creates an array of 5 integers, all defaulting to 0
        scores[0] = 95;
        scores[1] = 88;
        
        // Method 2: Array Literal (Declare and initialize with data instantly)
        String[] days = {"Monday", "Tuesday", "Wednesday"};
        
        // Accessing an element
        System.out.println("The first day is: " + days[0]);
        
        // Getting the size of the array
        System.out.println("The array has " + days.length + " elements.");
    }
}
```

### 2. Iterating Over an Array
The most common way to process an array is by looping through it.
```java
public class ArrayIteration {
    public static void main(String[] args) {
        double[] prices = {19.99, 5.50, 8.25};

        // Standard for loop (good when you need the index)
        for (int i = 0; i < prices.length; i++) {
            System.out.println("Item " + i + ": $" + prices[i]);
        }
        
        // Enhanced for loop (for-each) - cleaner, but no access to the index
        for (double price : prices) {
            System.out.println("Price: $" + price);
        }
    }
}
```

### 3. Multi-Dimensional Arrays
An array of arrays. Often used to represent grids or matrices.
```java
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6}
};
System.out.println(matrix[1][2]); // Accesses row 1, column 2 -> Output: 6
```

---

## 3. Common Mistakes or Pitfalls

* **`ArrayIndexOutOfBoundsException`:** The most famous array error. Occurs if you try to access an index that doesn't exist.
  ```java
  int[] nums = {10, 20, 30};
  // Valid indices are 0, 1, and 2.
  System.out.println(nums[3]); // ERROR! Throws exception and crashes program.
  ```
* **Confusing `length` with `length()`:** For arrays, `length` is a property (no parentheses). For Strings, `length()` is a method. `myArray.length()` will not compile.
* **Trying to resize an array:** You cannot add a 6th element to an array created with size 5. You must create an entirely new, larger array and copy the elements over. (To avoid this, developers usually use `ArrayList`).

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be hyper-aware of loop conditions iterating over arrays. A loop condition of `i <= array.length` will ALWAYS crash with an OutOfBounds exception on the last iteration. It must be `i < array.length`.

* **Takeaway 1:** Arrays hold primitives OR object references. If it holds objects, it actually holds pointers to those objects in memory.
* **Takeaway 2:** When an array of objects is created (e.g., `String[] words = new String[5];`), every slot is initially `null` until you explicitly instantiate an object into it.

---

## ⚔️ Java vs C++ (Key Differences)

> **Java arrays are objects, inherently know their .length, and are strictly bounds-checked. C++ raw arrays decay to pointers and have no automatic bounds checking.**
