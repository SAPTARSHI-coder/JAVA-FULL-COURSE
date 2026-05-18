# 067 — Calendars & Properties

> 📦 **Phase 6 — Collections (Utility)**

## 🎯 What is it?

**Calendar**: `java.util.Calendar` is used to work with dates and times (older API — `java.time` is modern but Calendar is still exam-relevant).

**Properties**: `java.util.Properties` is a key-value store (like HashMap) for `String` keys and values. Commonly used for config files.

## 💻 Calendar Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Calendar cal = Calendar.getInstance(); // current date/time

        int year  = cal.get(Calendar.YEAR);
        int month = cal.get(Calendar.MONTH) + 1; // 0-based! Jan=0
        int day   = cal.get(Calendar.DAY_OF_MONTH);
        int hour  = cal.get(Calendar.HOUR_OF_DAY);
        int min   = cal.get(Calendar.MINUTE);

        System.out.printf("Today: %02d/%02d/%d%n", day, month, year);
        System.out.printf("Time: %02d:%02d%n", hour, min);

        // Set a specific date
        cal.set(2025, Calendar.JANUARY, 1); // Jan 1, 2025
        System.out.println("Set date: " + cal.getTime());

        // Add days
        cal.add(Calendar.DAY_OF_MONTH, 10);
        System.out.println("+ 10 days: " + cal.getTime());
    }
}
```

## 💻 Properties Example

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Properties props = new Properties();

        // Set properties (like config file)
        props.setProperty("db.host", "localhost");
        props.setProperty("db.port", "5432");
        props.setProperty("db.name", "myapp");

        // Get properties
        System.out.println(props.getProperty("db.host"));  // localhost
        System.out.println(props.getProperty("db.port"));  // 5432
        System.out.println(props.getProperty("db.user", "admin")); // default value

        // List all
        props.list(System.out);
    }
}
```

**Output (Calendar varies by date):**
```
Today: 18/05/2025
Time: 01:07
localhost
5432
admin
-- listing properties --
db.port=5432
db.name=myapp
db.host=localhost
```

## 📝 Exam Tips
- `Calendar.MONTH` is **0-based** (0 = January) — add 1 when displaying!
- `Calendar.getInstance()` returns current date/time
- `Properties` extends `Hashtable<Object,Object>` — only String keys/values
- `Properties` is used to read `.properties` config files in real apps


---

## ⚔️ Java vs C++ (Key Differences)

> **Java handles dates using `Calendar` (legacy) or `java.time` (modern). C++ utilizes the `<chrono>` library (since C++11) for high-precision time and date management, which operates differently from Java's object-heavy approach.**
