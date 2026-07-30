---
{
  "title": "Testing with JUnit 5 and Mockito",
  "description": "Write unit tests with JUnit 5 annotations",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write unit tests with JUnit 5 annotations",
    "Use assertions with JUnit 5 Jupiter API",
    "Mock dependencies with Mockito",
    "Write parameterized tests"
  ],
  "knowledge_refs": [
    "java/java-14-junit-testing"
  ],
  "prerequisites": [
    "JV-01"
  ],
  "references": [
    {
      "title": "JUnit 5 User Guide",
      "url": "https://junit.org/junit5/docs/current/user-guide/"
    },
    {
      "title": "Mockito Docs",
      "url": "https://site.mockito.org/"
    },
    {
      "title": "Baeldung — JUnit 5",
      "url": "https://www.baeldung.com/junit-5"
    },
    {
      "title": "Baeldung — Mockito",
      "url": "https://www.baeldung.com/mockito"
    }
  ]
}
---

# JAVA-14-JUNIT-TESTING: Testing with JUnit 5 and Mockito

## Introduction

JUnit 5 (Jupiter) is the modern testing framework for Java. It supports parameterized tests, nested tests, dependency injection, and extension APIs. Mockito provides mocking for isolating units under test.

## Key Concepts

### 1. JUnit 5 Basics: @Test, Assertions

JUnit 5 uses @Test, @BeforeEach, @AfterEach, @BeforeAll, @AfterAll. Assertions API: assertEquals, assertTrue, assertThrows, assertAll for grouped assertions. Use assertAll to report all failures at once.

```java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private Calculator calc;

    @BeforeEach
    void setUp() {
        calc = new Calculator();
    }

    @Test
    void shouldAddTwoNumbers() {
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    void shouldThrowOnDivisionByZero() {
        assertThrows(ArithmeticException.class, () -> calc.divide(1, 0));
    }

    @Test
    void multipleAssertions() {
        assertAll("user",
            () -> assertEquals("Alice", user.getName()),
            () -> assertEquals(30, user.getAge())
        );
    }
}
```

### 2. Parameterized Tests

@ParameterizedTest with @ValueSource, @CsvSource, @MethodSource. Reduces code duplication by testing multiple inputs. Must add @ParameterizedTest annotation.

```java
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.*;

class ParameterizedCalculatorTest {

    @ParameterizedTest
    @ValueSource(ints = {1, 2, 3, 4, 5})
    void shouldBePositive(int number) {
        assertTrue(number > 0);
    }

    @ParameterizedTest
    @CsvSource({"1,1,2", "2,3,5", "10,-5,5"})
    void shouldAdd(int a, int b, int expected) {
        assertEquals(expected, calc.add(a, b));
    }

    @ParameterizedTest
    @MethodSource("provideNumbers")
    void shouldDetectEven(int number, boolean expected) {
        assertEquals(expected, number % 2 == 0);
    }

    static Stream<Arguments> provideNumbers() {
        return Stream.of(
            Arguments.of(2, true),
            Arguments.of(3, false)
        );
    }
}
```

### 3. Mockito Basics

Mockito creates mock objects. @Mock annotation with MockitoAnnotations.openMocks. when().thenReturn() for stubbing. verify() checks if methods were called. ArgumentMatchers for flexible matching.

```java
import org.mockito.*;
import static org.mockito.Mockito.*;

class UserServiceTest {
    @Mock private UserRepository repository;
    @InjectMocks private UserService service;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void shouldFindUser() {
        User expected = new User("Alice");
        when(repository.findById("1")).thenReturn(Optional.of(expected));

        Optional<User> result = service.findUser("1");

        assertTrue(result.isPresent());
        assertEquals("Alice", result.get().getName());
        verify(repository).findById("1");
    }
}
```

### 4. Advanced Mockito: Spies, Answer, ArgumentCaptor

@Spy wraps real objects (partial mocking). Answer for complex stub behavior. ArgumentCaptor captures arguments for verification. doThrow for void methods. Mockito.lenient for unnecessary stubs.

```java
// Spy — partial mocking on real object
@Spy
private List<String> list = new ArrayList<>();

// Answer — custom stub logic
when(repository.findById(any()))
    .thenAnswer(invocation -> {
        String id = invocation.getArgument(0);
        return Optional.of(new User("User-" + id));
    });

// ArgumentCaptor — capture method args
ArgumentCaptor<String> captor = ArgumentCaptor.forClass(String.class);
verify(repository).deleteById(captor.capture());
assertEquals("123", captor.getValue());

// doThrow for void methods
doThrow(new RuntimeException("DB error"))
    .when(repository).deleteById(any());
```

### 5. Test Patterns: TDD, Fixtures, Coverage

Write test before implementation. Use @DisplayName for readable names. Nested test classes for grouping. Test coverage with JaCoCo. Focus on edge cases and boundary conditions.

```java
@DisplayName("UserService should")
class UserServiceTest {

    @Nested
    @DisplayName("when finding users")
    class FindUser {
        @Test
        @DisplayName("should return user for valid ID")
        void validId() { }

        @Test
        @DisplayName("should return empty for invalid ID")
        void invalidId() { }
    }

    @Nested
    @DisplayName("when deleting users")
    class DeleteUser {
        @Test
        @DisplayName("should throw if user not found")
        void notFound() { }
    }
}
```

## Practice Questions

1. What is the difference between @BeforeEach and @BeforeAll?
1. How does @ParameterizedTest reduce code duplication?
1. What is the difference between @Mock and @Spy?
1. What does verify() do in Mockito?

## LLM Prompts for Deeper Understanding

1. "Explain JUnit 5 lifecycle: BeforeAll, BeforeEach, Test, AfterEach, AfterAll"
1. "Show Mockito patterns: stubbing, verification, ArgumentCaptor, Answer"
1. "Teach parameterized tests with CsvSource, MethodSource, enum values"

## Key Takeaways

- JUnit 5 uses @Test, @BeforeEach/@AfterEach, @BeforeAll/@AfterAll
- Mockito mocks external dependencies; verify() checks interaction
- Parameterized tests eliminate duplication with multiple input sources