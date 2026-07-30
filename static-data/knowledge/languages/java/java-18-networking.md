---
{
  "title": "Networking and HTTP Clients",
  "description": "Use Socket/ServerSocket for TCP networking",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Socket/ServerSocket for TCP networking",
    "Use HttpClient (Java 11+) for HTTP requests",
    "Handle JSON with Jackson/Gson",
    "Build REST API clients"
  ],
  "knowledge_refs": [
    "java/java-18-networking"
  ],
  "prerequisites": [
    "JV-08"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Networking",
      "url": "https://docs.oracle.com/javase/tutorial/networking/urls/index.html"
    },
    {
      "title": "Oracle Docs — HttpClient",
      "url": "https://docs.oracle.com/en/java/javase/21/docs/api/java.net.http/java/net/http/HttpClient.html"
    },
    {
      "title": "Jackson Docs",
      "url": "https://github.com/FasterXML/jackson"
    },
    {
      "title": "Baeldung — Java HTTP Client",
      "url": "https://www.baeldung.com/java-httpclient"
    }
  ]
}
---

# JAVA-18-NETWORKING: Networking and HTTP Clients

## Introduction

Java provides networking APIs from low-level Socket to high-level HTTP client (Java 11+). HttpClient supports HTTP/2, WebSocket, sync and async requests. JSON libraries parse responses.

## Key Concepts

### 1. TCP Networking with Socket

Socket for client connections, ServerSocket for servers. InputStream/OutputStream for data. Multithreading for concurrent clients. java.nio.channels for non-blocking I/O.

```java
// Server
try (ServerSocket server = new ServerSocket(8080)) {
    System.out.println("Server listening on 8080");
    while (true) {
        Socket client = server.accept();  // blocks until connect
        new Thread(() -> handleClient(client)).start();
    }
}

// Client
try (Socket socket = new Socket("localhost", 8080)) {
    PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
    BufferedReader in = new BufferedReader(
        new InputStreamReader(socket.getInputStream()));
    out.println("Hello Server");
    System.out.println("Response: " + in.readLine());
}
```

### 2. HttpClient (Java 11+)

HttpClient replaces HttpURLConnection. Supports HTTP/2, WebSocket, async. Build with HttpClient.newBuilder(). Send HttpRequest, get HttpResponse. BodyHandlers for response parsing.

```java
// Create client
HttpClient client = HttpClient.newBuilder()
    .connectTimeout(Duration.ofSeconds(10))
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();

// Sync request
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/users"))
    .header("Accept", "application/json")
    .timeout(Duration.ofSeconds(30))
    .GET()
    .build();

HttpResponse<String> response = client.send(
    request, HttpResponse.BodyHandlers.ofString());

System.out.println("Status: " + response.statusCode());
System.out.println("Body: " + response.body());
```

### 3. Async HTTP Requests

sendAsync() returns CompletableFuture<HttpResponse>. Chain with thenApply, thenAccept. Handle errors with exceptionally. Best for concurrent API calls without blocking threads.

```java
// Async request
CompletableFuture<HttpResponse<String>> future = client.sendAsync(
    request, HttpResponse.BodyHandlers.ofString());

// Process response when complete
future.thenApply(HttpResponse::body)
    .thenAccept(System.out::println)
    .exceptionally(ex -> {
        System.err.println("Request failed: " + ex.getMessage());
        return null;
    });

// Multiple concurrent requests
List<URI> urls = List.of(URI.create("https://api1.com"), URI.create("https://api2.com"));
List<CompletableFuture<String>> futures = urls.stream()
    .map(uri -> client.sendAsync(
        HttpRequest.newBuilder(uri).GET().build(),
        HttpResponse.BodyHandlers.ofString())
        .thenApply(HttpResponse::body))
    .collect(Collectors.toList());

// Wait for all
CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();
```

### 4. JSON with Jackson

Jackson deserializes JSON to Java objects. ObjectMapper is thread-safe. Customize with annotations: @JsonProperty, @JsonIgnore, @JsonFormat. Parse arrays with TypeReference.

```java
// Add jackson-databind dependency
// Maven: com.fasterxml.jackson.core:jackson-databind

ObjectMapper mapper = new ObjectMapper();

// Serialize object to JSON
User user = new User("Alice", 30);
String json = mapper.writeValueAsString(user);

// Deserialize JSON to object
User parsed = mapper.readValue(json, User.class);

// Parse array
List<User> users = mapper.readValue(
    jsonArray,
    new TypeReference<List<User>>() {}
);

// Jackson annotations
public class User {
    @JsonProperty("user_name")
    private String name;
    @JsonIgnore
    private String password;
}
```

### 5. RESTful API Client Patterns

Combine HttpClient + JSON for REST clients. Retry with exponential backoff. Error handling with status codes. Authentication with headers.

```java
// Typed API client
public class GitHubClient {
    private final HttpClient client = HttpClient.newHttpClient();
    private final ObjectMapper mapper = new ObjectMapper();

    public CompletableFuture<List<Repo>> getUserRepos(String username) {
        HttpRequest request = HttpRequest.newBuilder(
            URI.create("https://api.github.com/users/" + username + "/repos"))
            .header("Accept", "application/vnd.github.v3+json")
            .GET()
            .build();

        return client.sendAsync(request,
                HttpResponse.BodyHandlers.ofString())
            .thenApply(resp -> {
                if (resp.statusCode() != 200) {
                    throw new RuntimeException("API error: " + resp.statusCode());
                }
                try {
                    return mapper.readValue(resp.body(),
                        new TypeReference<List<Repo>>() {});
                } catch (JsonProcessingException e) {
                    throw new RuntimeException(e);
                }
            });
    }
}
```

## Practice Questions

1. What is the difference between synchronous and async HttpClient?
1. How does sendAsync work with CompletableFuture?
1. What does ObjectMapper do in Jackson?
1. What are the advantages of HttpClient (Java 11+) over HttpURLConnection?

## LLM Prompts for Deeper Understanding

1. "Explain Java HttpClient API: sync vs async, HTTP/2, WebSocket"
1. "Show Jackson serialization/deserialization with annotations"
1. "Teach REST client patterns with retry, error handling, authentication"

## Key Takeaways

- HttpClient (Java 11+) supports HTTP/2, sync and async requests
- sendAsync returns CompletableFuture for non-blocking HTTP calls
- Jackson ObjectMapper serializes/deserializes JSON to Java objects