# 047 — Creating Exception Subclasses (Custom Exceptions)

## 1. Definition and Core Concept

While Java provides dozens of built-in exceptions (like `IllegalArgumentException`), these are general-purpose. Sometimes, your application has highly specific business rules that require highly specific errors. 

For example, if you are building banking software, throwing a generic `Exception` when a user tries to withdraw too much money isn't very helpful. Instead, you should create a **Custom Exception** called `InsufficientFundsException`.

To create a custom exception, you simply create a new Java class and have it `extend` an existing Exception class.

---

## 2. Checked vs. Unchecked Custom Exceptions

The parent class you choose determines how the compiler treats your custom exception:
1. **Extend `Exception`:** Creates a **Checked Exception**. The compiler will *force* any method that uses this to write a `try-catch` block. Use this for recoverable business errors.
2. **Extend `RuntimeException`:** Creates an **Unchecked Exception**. The compiler will *ignore* it. Use this for programming errors or catastrophic logic failures.

---

## 3. Code Examples

### 1. Creating a Custom Exception Class
```java
// 1. Extend the appropriate parent class
public class InsufficientFundsException extends Exception {
    
    private double shortfallAmount;

    // 2. Provide a default constructor
    public InsufficientFundsException() {
        super("Insufficient funds in account.");
    }

    // 3. Provide a constructor that accepts a custom message
    public InsufficientFundsException(String message) {
        super(message); // Passes the message up to the parent Exception class
    }
    
    // 4. (Optional) Provide custom fields and methods for more context!
    public InsufficientFundsException(String message, double shortfallAmount) {
        super(message);
        this.shortfallAmount = shortfallAmount;
    }
    
    public double getShortfallAmount() {
        return shortfallAmount;
    }
}
```

### 2. Throwing and Catching the Custom Exception
```java
public class BankAccount {
    private double balance = 100.0;
    
    // We must declare 'throws' because it is a Checked Exception
    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            double shortfall = amount - balance;
            // Throwing our custom exception!
            throw new InsufficientFundsException("Withdrawal failed.", shortfall);
        }
        balance -= amount;
        System.out.println("Withdrawal successful. New balance: $" + balance);
    }
    
    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        
        try {
            account.withdraw(150.0);
        } catch (InsufficientFundsException e) {
            System.out.println(e.getMessage());
            System.out.println("You are short by: $" + e.getShortfallAmount());
        }
    }
}
```

---

## 4. Common Mistakes or Pitfalls

* **Forgetting `super(message)`:** If you write a custom exception with a string constructor but forget to call `super(message)`, the `getMessage()` method will return `null` when someone catches your exception, making debugging very difficult.
* **Extending `Throwable`:** Technically, you can create a custom exception by extending `Throwable` or `Error`. However, by convention and best practice, you should only ever extend `Exception` or `RuntimeException`.

---

## 5. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Be prepared to identify whether a custom exception is Checked or Unchecked based *solely* on what class it `extends` in the `class Custom extends ???` declaration.

* **Takeaway 1:** Custom exceptions make stack traces infinitely easier to read because the class name itself describes the exact business logic failure.
* **Takeaway 2:** You can add custom fields to exceptions (like `shortfallAmount`) to pass valuable diagnostic data back to the `catch` block!

