# 044 — Exception Throwing (Mechanics & Best Practices)

## 1. Definition and Core Concept

While we previously covered the syntax of the `throw` keyword (Topic 041), this topic focuses on the broader architectural concepts of **Exception Throwing**—knowing *when*, *why*, and *how* to throw exceptions effectively in a real-world Java application.

When building a method, you must decide how it behaves when given invalid inputs or when encountering an unrecoverable state. Rather than returning a silent failure code (like `-1` or `null`), the Java standard is to throw an Exception.

---

## 2. Best Practices for Throwing Exceptions

### 1. Fail Fast
The "Fail Fast" principle states that if your method receives invalid arguments, it should immediately throw an exception at the very top of the method, before attempting to do any complex processing or altering any state.

```java
public void processUserData(String username, int age) {
    // Fail Fast: Validate inputs immediately
    if (username == null || username.trim().isEmpty()) {
        throw new IllegalArgumentException("Username cannot be empty");
    }
    if (age < 0) {
        throw new IllegalArgumentException("Age cannot be negative");
    }
    
    // Now, safe to do complex processing...
}
```

### 2. Throw Specific Exceptions
Never throw the generic `Exception` or `RuntimeException` class. Always use the most specific exception available, or create a custom one.
* **Bad:** `throw new Exception("File missing");`
* **Good:** `throw new FileNotFoundException("data.txt is missing from config folder");`

### 3. Provide Meaningful Messages
The string you pass into the Exception constructor is the only clue another developer will have when the program crashes at 3:00 AM.
* **Bad:** `throw new IllegalArgumentException("Invalid ID");`
* **Good:** `throw new IllegalArgumentException("User ID must be greater than 0, received: " + id);`

---

## 3. Rethrowing and Exception Translation

Sometimes, a lower-level method catches an exception (like an `SQLException` from a database) but doesn't want to expose that specific database error to the higher-level UI code. It will catch the specific error, and "translate" it into a more generic business error, throwing that instead.

```java
public void fetchUserProfile() throws UserProfileException {
    try {
        // Attempt database connection
    } catch (SQLException e) {
        // We catch the DB error, and throw a custom business error.
        // By passing 'e' into the constructor, we preserve the original "Cause" (Chained Exceptions).
        throw new UserProfileException("Unable to load profile at this time", e);
    }
}
```

---

## 4. Exam Tips and Key Takeaways

> [!WARNING]
> **Exam Trap:** Remember that you can only throw objects that inherit from `Throwable`. If you try to write `throw new String("Error");`, the compiler will reject it entirely.

* **Takeaway 1:** Throwing an exception is computationally expensive because the JVM has to build a stack trace. Do not use exceptions for standard control flow (like breaking out of a loop).
* **Takeaway 2:** Always prefer throwing Unchecked Exceptions (`IllegalArgumentException`, `IllegalStateException`) for logic errors, and Checked Exceptions for external resource failures.

---

## ? Java vs C++ (Key Differences)

| Feature | Java | C++ |
| :--- | :--- | :--- |
| **Execution** | Compiled to Bytecode, runs on JVM (Platform Independent). | Compiled directly to Machine Code (Platform Dependent). |
| **Memory Management** | Automatic Garbage Collection. No explicit pointers. | Manual memory management (
ew/delete). Uses explicit pointers. |
| **Multiple Inheritance**| Not supported for classes (uses Interfaces instead). | Supported for classes, which can lead to the Diamond Problem. |
| **Object-Oriented** | Purely Object-Oriented (everything except primitives is an object). | Multi-paradigm (supports both Procedural and Object-Oriented programming). |
