# 111 — Case Study: Employee Management System (EMS)

## 1. Overview and Core Concept

As we reach the final topics of the syllabus, the focus shifts from learning individual syntax rules to integrating everything you've learned into full-scale system architecture.

An **Employee Management System (EMS)** is a classic capstone project. It tests your ability to combine Object-Oriented Programming, Data Structures, File I/O (or Databases), and GUI Design into a single, cohesive application.

The core goal of an EMS is to perform **CRUD operations**:
* **C**reate new employee records.
* **R**ead/View existing employee details.
* **U**pdate salaries or roles.
* **D**elete former employees.

---

## 2. System Architecture (Applying MVC)

To build a professional EMS, you must apply the Model-View-Controller (MVC) pattern discussed in Topic 110.

### 1. The Model Layer (Data & Logic)
This layer defines the blueprints and the data storage mechanisms.
* **The Entities:** You create an abstract `Employee` class. Then, you use Inheritance to create `FullTimeEmployee` (salary based) and `Contractor` (hourly based). 
* **The Repository:** A class named `EmployeeRepository` handles saving and loading data. For a basic project, this utilizes Java File I/O (`ObjectOutputStream` or writing to a `.csv` file). For an advanced project, it uses JDBC to connect to a MySQL database.

### 2. The View Layer (The GUI)
Using Java Swing or JavaFX, you build the visual interfaces:
* **Dashboard:** A main screen showing a `JTable` containing all current employees.
* **Add Form:** A pop-up dialog with `JTextFields` for entering the Name, ID, Role, and Salary, along with a "Save" button.

### 3. The Controller Layer (The Bridge)
The controller listens to the View.
* When the user clicks "Save" on the form, the `EmployeeController` intercepts the click.
* It grabs the text from the text fields.
* It instantiates a `new FullTimeEmployee()`.
* It passes that object to the `EmployeeRepository.save()` method.
* Finally, it tells the View's `JTable` to refresh so the new employee appears on the screen.

---

## 3. Applying Core Java Concepts

A good EMS demonstrates mastery of the entire syllabus:

1. **Encapsulation & Validation:** The `Employee` class makes salaries `private`. The `setSalary()` method throws an `IllegalArgumentException` if the user tries to input a negative number.
2. **Collections:** When loading the data from the database, the records are stored in an `ArrayList<Employee>` or a `HashMap<Integer, Employee>` (using the Employee ID as the key for lightning-fast lookups!).
3. **Streams & Lambdas:** If the manager clicks a button to "View Only High Earners", the controller uses the Stream API: `employeeList.stream().filter(e -> e.getSalary() > 100000).toList()` to instantly filter the table.
4. **Exception Handling:** If the database goes offline, the Repository catches the `SQLException` and bubbles it up so the Controller can display a nice error pop-up to the user, rather than crashing the program.

---

## 4. Exam Tips and Key Takeaways

> [!TIP]
> **Exam Focus:** Case studies in exams often ask architecture questions. If asked "Which data structure is best for an EMS where you constantly need to look up employees by their unique Employee ID?", the correct answer is a `HashMap` (O(1) lookup time), not an `ArrayList` (O(N) lookup time).

* **Takeaway 1:** An EMS requires combining OOP, Collections, File I/O, and GUI patterns.
* **Takeaway 2:** Separation of Concerns (MVC) is critical to ensure the system is maintainable.
* **Takeaway 3:** Use appropriate data structures (like Maps for ID lookups) to optimize performance.

