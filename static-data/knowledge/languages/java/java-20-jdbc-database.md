---
{
  "title": "Database Access with JDBC and JPA",
  "description": "Connect to databases with JDBC",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Connect to databases with JDBC",
    "Execute queries with PreparedStatement",
    "Use connection pooling with HikariCP",
    "Understand JPA and ORM basics"
  ],
  "knowledge_refs": [
    "java/java-20-jdbc-database"
  ],
  "prerequisites": [
    "JV-08"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — JDBC",
      "url": "https://docs.oracle.com/javase/tutorial/jdbc/basics/index.html"
    },
    {
      "title": "HikariCP Docs",
      "url": "https://github.com/brettwooldridge/HikariCP"
    },
    {
      "title": "Baeldung — JDBC Guide",
      "url": "https://www.baeldung.com/java-jdbc"
    },
    {
      "title": "Baeldung — HikariCP",
      "url": "https://www.baeldung.com/hikaricp"
    }
  ]
}
---

# JAVA-20-JDBC-DATABASE: Database Access with JDBC and JPA

## Introduction

JDBC is the built-in database access API. PreparedStatement prevents SQL injection. Connection pooling (HikariCP) is essential for performance. JPA (Hibernate) provides ORM for object-relational mapping.

## Key Concepts

### 1. JDBC Connection and Statement

DriverManager.getConnection() with URL, username, password. Statement for simple queries. ResultSet iterates results. Always close resources with try-with-resources.

```java
String url = "jdbc:postgresql://localhost:5432/mydb";
String user = "app";
String password = "secret";

try (Connection conn = DriverManager.getConnection(url, user, password);
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT id, name FROM users")) {

    while (rs.next()) {
        int id = rs.getInt("id");
        String name = rs.getString("name");
        System.out.println(id + ": " + name);
    }
} catch (SQLException e) {
    System.err.println("DB error: " + e.getMessage());
}
```

### 2. PreparedStatement — SQL Injection Prevention

PreparedStatement pre-compiles SQL with ? parameters. Prevents SQL injection. Supports batch operations for performance. Returns generated keys if needed.

```java
// Safe parameterized query
String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
try (PreparedStatement pstmt = conn.prepareStatement(sql,
        Statement.RETURN_GENERATED_KEYS)) {
    pstmt.setString(1, "Alice");
    pstmt.setString(2, "alice@example.com");
    int rows = pstmt.executeUpdate();

    // Get auto-generated key
    try (ResultSet keys = pstmt.getGeneratedKeys()) {
        if (keys.next()) {
            int newId = keys.getInt(1);
            System.out.println("Created user: " + newId);
        }
    }
}
```

### 3. Connection Pooling with HikariCP

HikariCP is the fastest connection pool. Configure max pool size, timeout, idle timeout. Never create connections manually in production — always pool.

```java
// HikariCP configuration
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setUsername("app");
config.setPassword("secret");
config.setMaximumPoolSize(10);
config.setMinimumIdle(2);
config.setConnectionTimeout(30000);  // 30 seconds
config.setIdleTimeout(600000);       // 10 minutes
config.setMaxLifetime(1800000);      // 30 minutes

HikariDataSource ds = new HikariDataSource(config);

// Usage — same try-with-resources pattern
try (Connection conn = ds.getConnection();
     PreparedStatement pstmt = conn.prepareStatement(sql)) {
    // use connection...
}
```

### 4. Transactions and Batch Operations

SetAutoCommit(false) for transactions. Commit() or rollback(). Savepoints for partial rollback. Batch operations with addBatch() and executeBatch().

```java
// Transaction
try (Connection conn = ds.getConnection()) {
    conn.setAutoCommit(false);
    try (PreparedStatement debit = conn.prepareStatement(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?");
         PreparedStatement credit = conn.prepareStatement(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?")) {

        debit.setBigDecimal(1, amount);
        debit.setInt(2, fromAccount);
        debit.executeUpdate();

        credit.setBigDecimal(1, amount);
        credit.setInt(2, toAccount);
        credit.executeUpdate();

        conn.commit();  // both succeed
    } catch (SQLException e) {
        conn.rollback();  // both fail
    }
}
```

### 5. JPA and Hibernate Basics

JPA is the ORM standard; Hibernate is the popular implementation. @Entity maps classes to tables. EntityManager persists, finds, queries. JPQL queries objects (not tables).

```java
@Entity
@Table(name = "users")
public class User {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(unique = true)
    private String email;
}

// EntityManager operations
EntityManagerFactory emf = Persistence.createEntityManagerFactory("my-pu");
EntityManager em = emf.createEntityManager();

em.getTransaction().begin();
User user = new User();
user.setName("Alice");
em.persist(user);  // INSERT
em.getTransaction().commit();

// Find by ID
User found = em.find(User.class, 1L);

// JPQL query
List<User> users = em.createQuery(
    "SELECT u FROM User u WHERE u.name LIKE :name", User.class)
    .setParameter("name", "A%")
    .getResultList();
```

## Practice Questions

1. Why use PreparedStatement over Statement?
1. What is connection pooling? Why is HikariCP needed?
1. How do transactions work in JDBC?
1. What is the difference between JDBC and JPA?

## LLM Prompts for Deeper Understanding

1. "Explain JDBC with PreparedStatement to prevent SQL injection"
1. "Show HikariCP configuration for production-grade connection pooling"
1. "Teach JPA/Hibernate: entities, EntityManager, JPQL, relationships"

## Key Takeaways

- PreparedStatement prevents SQL injection (never use Statement with user input)
- HikariCP is the standard connection pool for production applications
- JPA/Hibernate provides ORM mapping; JPQL queries objects not tables