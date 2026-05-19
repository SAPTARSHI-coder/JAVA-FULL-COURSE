                                                                                                                    # 027 — Access Control (Modifiers)

## 1. Definition and Core Concept

In Object-Oriented Programming, not every class, variable, or method should be visible or modifiable by the rest of the application. **Access Control** is the mechanism used to restrict the visibility of class members.

Java provides four levels of access control using three explicit access modifiers and one default (implicit) modifier.

### The Four Access Levels (From strictest to most lenient)
1. **`private`**: The member is accessible *only* within the exact same class. It is completely invisible to all other classes, even subclasses.
2. **Default (Package-Private)**: If you don't write an access modifier, the member is accessible to all classes within the *same package*.
3. **`protected`**: The member is accessible to all classes within the *same package*, AND accessible to subclasses (via inheritance) even if they are in different packages.
4. **`public`**: The member is universally accessible from any other class in any package.

---

## 2. Access Control Matrix

| Modifier | Same Class | Same Package | Subclass (Diff Package) | World (Diff Package) |
| :--- | :---: | :---: | :---: | :---: |
| `private` | **YES** | NO | NO | NO |
| *Default* | **YES** | **YES** | NO | NO |
| `protected` | **YES** | **YES** | **YES** | NO |
| `public` | **YES** | **YES** | **YES** | **YES** |

---

## 3. Code Examples

```java
// File: com/company/hr/Employee.java
package com.company.hr;

public class Employee {
    public String name;       // Visible to anyone
    protected double salary;  // Visible to package & subclasses
    int departmentId;         // Visible only to this package (default)
    private String ssn;       // Visible ONLY inside this Employee class
    
    public void printDetails() {
        // Because we are inside the Employee class, we can access EVERYTHING.
        System.out.println(name + ", " + salary + ", " + departmentId + ", " + ssn);
    }
}
```

```java
// File: com/company/main/MainApp.java (Different Package!)
package com.company.main;
import com.company.hr.Employee;

public class MainApp {
    public static void main(String[] args) {
        Employee emp = new Employee();
        
        emp.name = "Alice"; // Works! It is public.
        
        // emp.salary = 50000; // ERROR! Protected, and we are not in the same package or a subclass.
        // emp.departmentId = 2; // ERROR! Default, and we are not in the same package.
        // emp.ssn = "123-456"; // ERROR! Private, completely invisible.
    }
}
```

---

## 4. Common Mistakes or Pitfalls

* **Putting `private` on a top-level Class:** A top-level class (a class not nested inside another class) can only be `public` or `default`. If you make a top-level class `private`, it would be completely useless because no other code could ever use it to create an object.
* **Assuming `protected` means "subclasses only":** `protected` actually means "subclasses OR same package". It is strictly more lenient than the default modifier.

---

## 5. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Exam questions often feature two classes in the *same package* where Class A tries to access a `protected` variable in Class B, without inheriting from it. This is perfectly legal! `protected` allows package access.

* **Takeaway 1:** Always make instance variables `private` by default. This forces external code to use public getters and setters, maintaining encapsulation.
* **Takeaway 2:** When overriding a method in a subclass, the access level cannot be made *more restrictive* than the parent method (e.g., you cannot override a `public` method and make it `protected`).


---

## ⚔️ Java vs C++ (Key Differences)

> **Java applies access modifiers per-member and has a `default` (package-private) level. C++ applies modifiers to blocks of members and has no concept of packages.**
