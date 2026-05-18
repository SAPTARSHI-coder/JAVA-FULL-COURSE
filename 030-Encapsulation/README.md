# 030 — Encapsulation

## 1. Definition and Core Concept

**Encapsulation** is one of the four fundamental pillars of Object-Oriented Programming. It is the practice of wrapping data (variables) and the code that acts on that data (methods) together as a single unit (the class). 

More importantly, Encapsulation involves **Data Hiding**. It prevents external code from directly accessing or modifying an object's internal state. Instead, external classes must use public "Getter" and "Setter" methods to interact with the data. 

### Why Encapsulate?
1. **Control:** You can enforce validation logic in the Setter to prevent invalid data (e.g., preventing a negative age or a bank balance drop below zero).
2. **Security:** You can make a variable read-only by providing a Getter but omitting the Setter.
3. **Flexibility:** You can change the internal implementation (e.g., changing how a variable is calculated) without breaking external code that relies on your class.

---

## 2. Code Examples

### Bad Practice (No Encapsulation)
```java
public class Person {
    public int age; // Anyone can access this directly
}

public class Main {
    public static void main(String[] args) {
        Person p = new Person();
        p.age = -500; // Invalid data, but the class can't stop it!
    }
}
```

### Best Practice (Proper Encapsulation)
To achieve encapsulation, make variables `private` and provide `public` methods to access them.

```java
public class Person {
    // 1. Data is hidden
    private int age; 
    
    // 2. Public Getter (Read access)
    public int getAge() {
        return age;
    }
    
    // 3. Public Setter with Validation (Controlled Write access)
    public void setAge(int age) {
        if (age >= 0 && age <= 120) {
            this.age = age;
        } else {
            System.out.println("Error: Invalid age provided!");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Person p = new Person();
        
        // p.age = -500; // COMPILE ERROR! Cannot access private field.
        
        p.setAge(25); // Valid
        p.setAge(-5); // Rejected by validation logic
        
        System.out.println("Age is: " + p.getAge());
    }
}
```

---

## 3. Common Mistakes or Pitfalls

* **Making Fields Private, but Returning Mutable Objects:** If a getter returns a direct reference to a private mutable object (like a Date or an Array), the caller can modify the internal state of that object, bypassing encapsulation.
  ```java
  private int[] scores = {90, 80};
  
  public int[] getScores() { return scores; } // DANGEROUS!
  // External code can do: getScores()[0] = 0; changing your private data!
  ```
  **Fix:** Return a *clone* or copy of the array/object to protect the internal state.

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Encapsulation is synonymous with `private` variables and `public` getter/setter methods. If an exam asks which principle restricts direct variable access, the answer is always Encapsulation.

* **Takeaway 1:** Encapsulation = Data Hiding + Controlled Access.
* **Takeaway 2:** A fully encapsulated class forces external objects to communicate via methods, meaning the internal implementation can safely change in the future.

