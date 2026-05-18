# 077 — Connection and Handling DB with JDBC

> 📦 **Phase 8 — Database Connectivity (JDBC)**

## 🎯 What is it?
The standard 5 steps to connect to a database and execute a query in Java:
1. **Register the Driver** (`Class.forName()`)
2. **Get Connection** (`DriverManager.getConnection()`)
3. **Create Statement** (`conn.createStatement()`)
4. **Execute Query** (`stmt.executeQuery()`)
5. **Close Connection** (`conn.close()`)

## 💻 Code Example (Conceptual)

*(Note: Requires a DB driver JAR like mysql-connector-java.jar to actually run)*

```java
import java.sql.*;

public class Main {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydb";
        String user = "root";
        String pass = "password";

        // Modern JDBC uses try-with-resources to auto-close connections
        try (Connection conn = DriverManager.getConnection(url, user, pass);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT id, name FROM users")) {

            System.out.println("Connected successfully!");

            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                System.out.println("ID: " + id + ", Name: " + name);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

## 📝 Exam Tips
- **`Statement` vs `PreparedStatement`**: Always prefer `PreparedStatement` for dynamic queries to prevent SQL Injection attacks.
- **`executeQuery()`**: Used for SELECT statements (returns `ResultSet`).
- **`executeUpdate()`**: Used for INSERT, UPDATE, DELETE (returns `int` row count).
- `Class.forName("com.mysql.cj.jdbc.Driver")` was historically required to load the driver, but is optional in JDBC 4.0+.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java database connections are strictly managed via `Connection`, `Statement`, and `ResultSet` interfaces. C++ database querying depends entirely on the specific third-party library being used, with no standard API comparable to JDBC.**
