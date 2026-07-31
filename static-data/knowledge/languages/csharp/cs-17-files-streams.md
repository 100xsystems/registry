---
{
  "title": "Files and Streams",
  "description": "System.IO, File/FileInfo, StreamReader/Writer, binary streams, using disposal.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read and write text files synchronously",
    "Read and write files asynchronously",
    "Use StreamReader and StreamWriter",
    "Work with binary streams"
  ],
  "knowledge_refs": [
    "csharp/cs-17-files-streams"
  ],
  "prerequisites": [
    "CS-16"
  ],
  "references": [
    {
      "title": "File and Stream I/O",
      "url": "https://learn.microsoft.com/en-us/dotnet/standard/io/"
    },
    {
      "title": "File Class",
      "url": "https://learn.microsoft.com/en-us/dotnet/api/system.io.file"
    },
    {
      "title": "StreamReader Class",
      "url": "https://learn.microsoft.com/en-us/dotnet/api/system.io.streamreader"
    }
  ]
}
---

# CS-17-FILES-STREAMS: Files and Streams

## Introduction

System.IO, File/FileInfo, StreamReader/Writer, binary streams, using disposal. By the end of this lesson you will be able to: Read and write text files synchronously; Read and write files asynchronously; Use StreamReader and StreamWriter; Work with binary streams.

## Key Concepts

### 1. Read and write text files synchronously

Target: Read and write text files synchronously. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```csharp
using System.IO;
string path = "/tmp/notes.txt";
File.WriteAllText(path, "hello");
Console.WriteLine(File.ReadAllText(path));  // hello
```
### 2. Read and write files asynchronously

Target: Read and write files asynchronously. Apply the idiomatic pattern — this is how production C# expresses this idea, so study the shape of the code.

```csharp
await File.WriteAllTextAsync(path, "async write");
string content = await File.ReadAllTextAsync(path);
Console.WriteLine(content);
```
### 3. Use StreamReader and StreamWriter

Target: Use StreamReader and StreamWriter. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```csharp
using var reader = new StreamReader(path);
string? line;
while ((line = await reader.ReadLineAsync()) != null)
    Console.WriteLine(line);

using var writer = new StreamWriter("/tmp/out.txt");
await writer.WriteLineAsync("line 1");
```
### 4. Work with binary streams

Target: Work with binary streams. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```csharp
using var fs = new FileStream("/tmp/data.bin", FileMode.Create);
byte[] bytes = { 1, 2, 3, 4 };
await fs.WriteAsync(bytes);
fs.Position = 0;
byte[] buffer = new byte[4];
await fs.ReadAsync(buffer);
Console.WriteLine(string.Join(",", buffer));  // 1,2,3,4
```

## Practice Questions

1. What is the key idea behind "Files and Streams"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Files and Streams with analogies and real-world examples"
1. "Show me common mistakes beginners make with Files and Streams"
1. "Provide advanced patterns and performance considerations for Files and Streams"

## Key Takeaways

- Master the core ideas of Files and Streams through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked Microsoft Learn docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
