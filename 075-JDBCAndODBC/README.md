# 075 — JDBC and ODBC

> 📦 **Phase 8 — Database Connectivity (JDBC)**

## 🎯 What is it?
- **JDBC (Java Database Connectivity)**: A Java API used to connect and execute queries with a database. It uses JDBC drivers.
- **ODBC (Open Database Connectivity)**: A standard C programming API for accessing DBMS. Developed by Microsoft.

**Why JDBC instead of ODBC in Java?**
ODBC uses C/C++ native code. If Java uses ODBC directly, it loses its platform independence. JDBC allows Java to connect to databases using Java interfaces, keeping it platform-independent.

## 🔌 JDBC Architecture
JDBC Architecture consists of two layers:
1. **JDBC API**: Provides application-to-JDBC Manager connection (Classes like `Connection`, `Statement`, `ResultSet`).
2. **JDBC Driver API**: Provides JDBC Manager-to-Driver Connection.

## 📝 Exam & Viva Questions
**Q: What is JDBC?**  
A: Java API to connect and execute queries on a relational database.

**Q: Why was JDBC needed if ODBC already existed?**  
A: ODBC is platform-dependent (native C code) and not suitable for Java's "write once, run anywhere" philosophy. JDBC is pure Java.

**Q: What are the main components of JDBC?**  
A: `DriverManager`, `Connection`, `Statement`, `PreparedStatement`, `ResultSet`.


---

## ⚔️ Java vs C++ (Key Differences)

> **Java natively uses JDBC, a standard API explicitly designed to bridge Java with databases. C++ historically relied on ODBC (C-based API), lacking a built-in standard OOP database connector equivalent to JDBC.**
