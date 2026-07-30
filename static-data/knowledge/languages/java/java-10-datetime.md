---
{
  "title": "Date and Time API (Java 8+)",
  "description": "Use LocalDate, LocalTime, LocalDateTime",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use LocalDate, LocalTime, LocalDateTime",
    "Handle time zones with ZonedDateTime",
    "Format/parse dates with DateTimeFormatter",
    "Calculate durations and periods"
  ],
  "knowledge_refs": [
    "java/java-10-datetime"
  ],
  "prerequisites": [
    "JV-01"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Date/Time",
      "url": "https://docs.oracle.com/javase/tutorial/datetime/iso/index.html"
    },
    {
      "title": "Oracle Docs — DateTimeFormatter",
      "url": "https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/time/format/DateTimeFormatter.html"
    },
    {
      "title": "Baeldung — Java Date/Time",
      "url": "https://www.baeldung.com/java-8-date-time-intro"
    }
  ]
}
---

# JAVA-10-DATETIME: Date and Time API (Java 8+)

## Introduction

The java.time package (Java 8+) replaces the flawed Date and Calendar classes. It provides immutable, thread-safe date/time objects: LocalDate, LocalTime, LocalDateTime, ZonedDateTime, Duration, Period.

## Key Concepts

### 1. LocalDate, LocalTime, LocalDateTime

LocalDate (date only), LocalTime (time only), LocalDateTime (both). All are immutable — create new instances with methods. now() for current, of() for specific, parse() for strings.

```java
// Create dates/times
LocalDate today = LocalDate.now();
LocalDate specific = LocalDate.of(2024, Month.JULY, 28);
LocalTime lunch = LocalTime.of(12, 30);
LocalDateTime meeting = LocalDateTime.of(2024, 7, 28, 14, 0);

// Date manipulation (returns new instances)
LocalDate nextWeek = today.plusWeeks(1);
LocalDate firstOfMonth = today.withDayOfMonth(1);
LocalDate lastYear = today.minusYears(1);

// Queries
DayOfWeek dayOfWeek = today.getDayOfWeek();
int dayOfMonth = today.getDayOfMonth();
boolean leapYear = today.isLeapYear();
```

### 2. ZonedDateTime and OffsetDateTime

ZonedDateTime handles full time zone with DST rules. ZoneId identifies time zones (America/New_York). OffsetDateTime stores fixed offset from UTC. Use ZonedDateTime for user display, Instant for storage.

```java
// Zone handling
ZoneId nyZone = ZoneId.of("America/New_York");
ZonedDateTime nyTime = ZonedDateTime.now(nyZone);

// Convert between zones
ZonedDateTime utc = nyTime.withZoneSameInstant(ZoneOffset.UTC);

// Instant — machine time (UTC)
Instant now = Instant.now();  // always UTC
Instant parsed = Instant.parse("2024-07-28T10:30:00Z");

// Convert Instant to ZonedDateTime
ZonedDateTime localInstant = now.atZone(ZoneId.systemDefault());
```

### 3. Formatting with DateTimeFormatter

DateTimeFormatter for parsing and formatting. Predefined formatters, pattern-based, or locale-specific. Formatter is thread-safe and immutable.

```java
// Predefined formatters
LocalDate today = LocalDate.now();
today.format(DateTimeFormatter.ISO_DATE);       // 2024-07-28
today.format(DateTimeFormatter.ISO_LOCAL_DATE);

// Custom patterns
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
LocalDateTime dt = LocalDateTime.now();
String formatted = dt.format(formatter);  // "2024-07-28 14:30:00"

// Parsing back
LocalDate parsed = LocalDate.parse("2024-07-28");
LocalDateTime parsedDt = LocalDateTime.parse("2024-07-28 14:30", formatter);
```

### 4. Duration and Period

Duration measures time-based amounts (hours, minutes). Period measures date-based amounts (years, months, days). between() to measure between two temporal values.

```java
// Duration — for time-based
Duration workHours = Duration.ofHours(8);
Duration taskTime = Duration.between(startTime, endTime);
long minutes = taskTime.toMinutes();

// Period — for date-based
Period age = Period.between(birthDate, today);
System.out.printf("%d years, %d months%n", age.getYears(), age.getMonths());

// ChronoUnit for single-unit differences
long daysBetween = ChronoUnit.DAYS.between(start, end);
long weeks = ChronoUnit.WEEKS.between(start, end);
```

### 5. Legacy Conversion and TemporalAdjusters

Date.toInstant() converts legacy Date to Instant. Calendar to Instant via toInstant(). TemporalAdjusters provide date calculations: next Monday, first day of month, etc.

```java
// Legacy conversion
Date legacyDate = new Date();
Instant instant = legacyDate.toInstant();
LocalDateTime newDate = LocalDateTime.ofInstant(instant, ZoneId.systemDefault());

// Convert back
Date convertedBack = Date.from(instant);

// TemporalAdjusters
LocalDate today = LocalDate.now();
LocalDate nextMonday = today.with(TemporalAdjusters.next(DayOfWeek.MONDAY));
LocalDate firstOfMonth = today.with(TemporalAdjusters.firstDayOfMonth());
LocalDate lastOfMonth = today.with(TemporalAdjusters.lastDayOfMonth());
```

## Practice Questions

1. Why was the old Date/Calendar API replaced?
1. What is the difference between LocalDate, LocalDateTime, and ZonedDateTime?
1. What is an Instant? When would you use it?
1. Difference between Duration and Period?

## LLM Prompts for Deeper Understanding

1. "Explain java.time API design: immutable, thread-safe, fluent"
1. "Show time zone handling with ZonedDateTime, Instant, UTC conversion"
1. "Teach DateTimeFormatter patterns and TemporalAdjusters"

## Key Takeaways

- java.time (Java 8+) replaces Date/Calendar — immutable and thread-safe
- Instant for machine time (UTC), ZonedDateTime for display with zone
- DateTimeFormatter for parse/format; Duration for time, Period for dates