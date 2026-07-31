#!/usr/bin/env python3
"""Generate the 21-lesson C curriculum at Python/JS/Java depth.
Creates static-data/knowledge/languages/c/*.md + updates index.json lessons.
Exact sub-topic references from cppreference.com, learn-c.org, and Beej's Guide.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import json
import os

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'c')

# ─── Per-lesson: 4 sub-topic code samples (real C, distinct per sub-topic) ───
CODE = {
    1: [
        '#include <stdio.h>\n\n'
        '// compile: gcc -Wall -Wextra -o hello hello.c && ./hello\n'
        'int main(void) {\n'
        '    printf("Hello, 100X Systems!\\n");\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// toolchain: preprocessor -> compiler -> assembler -> linker\n'
        '// gcc -E hello.c (preprocess), gcc -S (assembly), gcc -c (object)\n'
        'int main(void) {\n'
        '    printf("gcc -Wall -Wextra -std=c17 hello.c\\n");\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// argc = argument count, argv = argument vector\n'
        'int main(int argc, char *argv[]) {\n'
        '    printf("argc = %d\\n", argc);\n'
        '    for (int i = 0; i < argc; i++) printf("argv[%d] = %s\\n", i, argv[i]);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // three standard streams\n'
        '    fprintf(stdout, "stdout: buffered\\n");\n'
        '    fprintf(stderr, "stderr: unbuffered\\n");\n'
        '    return 0;\n'
        '}',
    ],
    2: [
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int i = 42;              // signed integer (usually 32-bit)\n'
        '    unsigned u = 42u;        // unsigned\n'
        '    long l = 42L;            // at least 32-bit, often 64\n'
        '    float f = 3.14f;         // single precision\n'
        '    double d = 3.14;         // double precision\n'
        '    char c = \'A\';            // single byte\n'
        '    _Bool b = 1;             // boolean\n'
        '    printf("%d %u %ld %.2f %.2f %c %d\\n", i, u, l, f, d, c, b);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <inttypes.h>   // PRId32 / PRIu64 macros (includes stdint.h)\n\n'
        'int main(void) {\n'
        '    // fixed-width types\n'
        '    int32_t x = -100;         // exactly 32 bits\n'
        '    uint64_t y = 100ULL;      // exactly 64 bits\n'
        '    printf("%" PRId32 " %" PRIu64 "\\n", x, y);\n'
        '    // sizeof returns bytes\n'
        '    printf("int=%zu char=%zu ptr=%zu\\n", sizeof(int), sizeof(char), sizeof(void *));\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // signed vs unsigned overflow behavior\n'
        '    int s = 2147483647;\n'
        '    unsigned u = 4294967295U;\n'
        '    printf("s+1 = %d\\n", s + 1);   // UB: signed overflow\n'
        '    printf("u+1 = %u\\n", u + 1);   // defined: wraps to 0\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <limits.h>\n\n'
        'int main(void) {\n'
        '    printf("INT_MAX=%d INT_MIN=%d\\n", INT_MAX, INT_MIN);\n'
        '    printf("CHAR_BIT=%d\\n", CHAR_BIT);\n'
        '    // enumerations: named integer constants\n'
        '    enum Color { RED, GREEN, BLUE };\n'
        '    enum Color c = GREEN;\n'
        '    printf("%d\\n", c);   // 1\n'
        '    return 0;\n'
        '}',
    ],
    3: [
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int a = 17, b = 5;\n'
        '    printf("%d %d %d %d %d\\n", a + b, a - b, a * b, a / b, a % b);\n'
        '    // 22 12 85 3 2 (integer division truncates toward zero)\n'
        '    printf("%d\\n", -17 / 5);  // -3 (C99 truncates toward zero)\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int a = 5, b = 3;\n'
        '    printf("%d %d %d %d\\n", a == b, a != b, a < b, a >= b);\n'
        '    // logical && and || short-circuit: second operand may be skipped\n'
        '    int x = 10;\n'
        '    int zero = 0;\n'
        '    if (zero != 0 && (x = a / b)) ;   // first operand false -> x NOT assigned\n'
        '    printf("x unchanged: %d\\n", x);   // 10 (short-circuit worked)\n'
        '    if (b != 0 || (x = 99)) ;          // first operand true -> x NOT assigned\n'
        '    printf("x still: %d\\n", x);       // 10\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // bitwise operators\n'
        '    unsigned a = 0b1100, b = 0b1010;  // 12, 10\n'
        '    printf("%u %u %u\\n", a & b, a | b, a ^ b);   // 8, 14, 6\n'
        '    printf("%u %u\\n", a << 1, a >> 1);           // 24, 6\n'
        '    printf("%u\\n", ~a);                          // bitwise NOT\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // assignment + compound assignment\n'
        '    int x = 10;\n'
        '    x += 5;        // x = 15\n'
        '    x *= 2;        // x = 30\n'
        '    // increment/decrement: prefix vs postfix\n'
        '    int i = 5;\n'
        '    int pre = ++i;    // i becomes 6, pre = 6\n'
        '    int post = i++;   // post = 6, i becomes 7\n'
        '    printf("%d %d %d\\n", pre, post, i);\n'
        '    return 0;\n'
        '}',
    ],
    4: [
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int score = 85;\n'
        '    if (score >= 90) printf("A\\n");\n'
        '    else if (score >= 80) printf("B\\n");\n'
        '    else printf("C\\n");\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int day = 3;\n'
        '    switch (day) {\n'
        '        case 1: printf("Monday\\n"); break;\n'
        '        case 2: printf("Tuesday\\n"); break;\n'
        '        default: printf("Other\\n"); break;\n'
        '    }\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    for (int i = 0; i < 5; i++) printf("%d ", i);  // 0 1 2 3 4\n'
        '    printf("\\n");\n'
        '    int j = 0;\n'
        '    while (j < 3) { printf("%d ", j); j++; }       // 0 1 2\n'
        '    printf("\\n");\n'
        '    int k = 0;\n'
        '    do { printf("%d ", k); k++; } while (k < 2);   // 0 1 (runs at least once)\n'
        '    printf("\\n");\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    for (int i = 0; i < 10; i++) {\n'
        '        if (i == 2) continue;   // skip 2\n'
        '        if (i == 5) break;      // stop at 5\n'
        '        printf("%d ", i);       // 0 1 3 4\n'
        '    }\n'
        '    printf("\\n");\n'
        '    return 0;\n'
        '}',
    ],
    5: [
        '#include <stdio.h>\n\n'
        '// function prototype (declaration)\n'
        'int add(int a, int b);\n\n'
        'int main(void) {\n'
        '    printf("%d\\n", add(2, 3));\n'
        '    return 0;\n'
        '}\n\n'
        '// function definition\n'
        'int add(int a, int b) { return a + b; }',
        '#include <stdio.h>\n\n'
        '// pass-by-value: modifications do NOT affect the caller\n'
        'void try_swap(int a, int b) {\n'
        '    int t = a; a = b; b = t;\n'
        '}\n\n'
        'int main(void) {\n'
        '    int x = 1, y = 2;\n'
        '    try_swap(x, y);\n'
        '    printf("%d %d\\n", x, y);   // 1 2 (unchanged)\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// pass-by-pointer: modifications DO affect the caller\n'
        'void swap(int *a, int *b) {\n'
        '    int t = *a; *a = *b; *b = t;\n'
        '}\n\n'
        'int main(void) {\n'
        '    int x = 1, y = 2;\n'
        '    swap(&x, &y);\n'
        '    printf("%d %d\\n", x, y);   // 2 1\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// recursion: function calls itself\n'
        'long fact(int n) {\n'
        '    if (n <= 1) return 1;\n'
        '    return n * fact(n - 1);\n'
        '}\n\n'
        'int main(void) {\n'
        '    printf("%ld\\n", fact(6));  // 720\n'
        '    return 0;\n'
        '}',
    ],
    6: [
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int nums[5] = {1, 2, 3, 4, 5};\n'
        '    for (int i = 0; i < 5; i++) printf("%d ", nums[i]);\n'
        '    printf("\\n");\n'
        '    printf("nums[0]=%d size=%zu\\n", nums[0], sizeof(nums) / sizeof(nums[0]));\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <string.h>\n\n'
        'int main(void) {\n'
        '    // C strings are null-terminated char arrays\n'
        '    char msg[] = "hello";\n'
        '    printf("%s len=%zu\\n", msg, strlen(msg));   // hello len=5\n'
        '    char buf[32];\n'
        '    strcpy(buf, "world");\n'
        '    strcat(buf, "!");\n'
        '    printf("%s\\n", buf);                        // world!\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // 2D arrays: row-major\n'
        '    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};\n'
        '    for (int r = 0; r < 2; r++)\n'
        '        for (int c = 0; c < 3; c++)\n'
        '            printf("%d ", grid[r][c]);\n'
        '    printf("\\n");\n'
        '    printf("grid[1][0] = %d\\n", grid[1][0]);   // 4\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // strings are arrays of char: iterate safely\n'
        '    char *name = "100x";\n'
        '    for (int i = 0; name[i] != \'\\0\'; i++) putchar(name[i]);\n'
        '    printf("\\n");\n'
        '    // array decay: name in an expression is &name[0]\n'
        '    printf("pointer to first char: %c\\n", *name);\n'
        '    return 0;\n'
        '}',
    ],
    7: [
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int x = 42;\n'
        '    int *p = &x;             // p holds the address of x\n'
        '    printf("x=%d *p=%d\\n", x, *p);   // 42 42 (dereference)\n'
        '    *p = 100;                // write through the pointer\n'
        '    printf("x=%d\\n", x);    // 100\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int nums[4] = {10, 20, 30, 40};\n'
        '    int *p = nums;           // array decays to pointer\n'
        '    printf("%d %d\\n", *p, *(p + 1));   // 10 20 (pointer arithmetic)\n'
        '    printf("%d %d\\n", p[0], p[2]);     // indexing through pointer\n'
        '    p++;                     // move to next element\n'
        '    printf("%d\\n", *p);     // 20\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    int x = 42;\n'
        '    int *p = &x;\n'
        '    int **pp = &p;           // pointer-to-pointer\n'
        '    printf("%d %d %d\\n", x, *p, **pp);   // 42 42 42\n'
        '    **pp = 99;\n'
        '    printf("%d\\n", x);      // 99\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // null pointer checks\n'
        '    int *p = NULL;\n'
        '    if (p) printf("valid\\n");\n'
        '    else printf("null\\n");\n'
        '    // void *: generic pointer, must cast to use\n'
        '    int x = 7;\n'
        '    void *v = &x;\n'
        '    int *back = (int *)v;\n'
        '    printf("%d\\n", *back);  // 7\n'
        '    return 0;\n'
        '}',
    ],
    8: [
        '#include <stdio.h>\n\n'
        'struct Point {\n'
        '    int x;\n'
        '    int y;\n'
        '};\n\n'
        'int main(void) {\n'
        '    struct Point p = {3, 4};\n'
        '    printf("(%d, %d)\\n", p.x, p.y);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'struct Point { int x, y; };\n\n'
        'int main(void) {\n'
        '    // access through pointer with ->\n'
        '    struct Point p = {1, 2};\n'
        '    struct Point *pp = &p;\n'
        '    pp->x = 99;\n'
        '    printf("(%d, %d)\\n", p.x, p.y);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <string.h>\n\n'
        'struct Person {\n'
        '    char name[32];\n'
        '    int age;\n'
        '};\n\n'
        'int main(void) {\n'
        '    struct Person alice;\n'
        '    strcpy(alice.name, "Alice");\n'
        '    alice.age = 30;\n'
        '    printf("%s %d\\n", alice.name, alice.age);\n'
        '    // structs are copied by value\n'
        '    struct Person copy = alice;\n'
        '    copy.age = 31;\n'
        '    printf("%d %d\\n", alice.age, copy.age);  // 30 31\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// union: members share the same memory\n'
        'union Number {\n'
        '    int i;\n'
        '    float f;\n'
        '};\n\n'
        'int main(void) {\n'
        '    union Number n;\n'
        '    n.i = 42;\n'
        '    printf("%d\\n", n.i);\n'
        '    n.f = 3.14f;             // overwrites the int\n'
        '    printf("%f\\n", n.f);\n'
        '    printf("size of union: %zu\\n", sizeof(n));  // size of largest member\n'
        '    return 0;\n'
        '}',
    ],
    9: [
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        'int main(void) {\n'
        '    int *p = malloc(5 * sizeof(int));   // heap allocation\n'
        '    if (!p) return 1;                   // check for NULL\n'
        '    for (int i = 0; i < 5; i++) p[i] = i * i;\n'
        '    printf("%d\\n", p[3]);              // 9\n'
        '    free(p);                            // MUST free\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n'
        '#include <string.h>\n\n'
        'int main(void) {\n'
        '    // calloc: zero-initialized\n'
        '    int *p = calloc(5, sizeof(int));\n'
        '    if (!p) return 1;\n'
        '    printf("%d\\n", p[3]);              // 0\n'
        '    // realloc: resize (may move the block)\n'
        '    p = realloc(p, 10 * sizeof(int));\n'
        '    if (!p) return 1;\n'
        '    memset(p, 0, 10 * sizeof(int));\n'
        '    printf("%d\\n", p[9]);\n'
        '    free(p);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        'int main(void) {\n'
        '    // memory leak: forgetting free\n'
        '    // double free: freeing the same pointer twice (UB!)\n'
        '    int *a = malloc(sizeof(int));\n'
        '    int *b = a;             // both point to same block\n'
        '    free(a);\n'
        '    // free(b);             // double free — UB, crash\n'
        '    printf("freed once\\n");\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        '// typical pattern: allocate and return a heap array\n'
        'int *make_evens(int n) {\n'
        '    int *arr = malloc(n * sizeof(int));\n'
        '    if (!arr) return NULL;\n'
        '    for (int i = 0; i < n; i++) arr[i] = i * 2;\n'
        '    return arr;\n'
        '}\n\n'
        'int main(void) {\n'
        '    int *evens = make_evens(4);\n'
        '    for (int i = 0; i < 4; i++) printf("%d ", evens[i]);\n'
        '    printf("\\n");   // 0 2 4 6\n'
        '    free(evens);\n'
        '    return 0;\n'
        '}',
    ],
    10: [
        '#include <stdio.h>\n\n'
        '#define PI 3.14159\n'
        '#define SQUARE(x) ((x) * (x))\n\n'
        'int main(void) {\n'
        '    printf("%.5f\\n", PI);\n'
        '    printf("%d\\n", SQUARE(5));      // 25\n'
        '    printf("%d\\n", SQUARE(1 + 1));  // 4 (parentheses matter!)\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// include guards prevent multiple inclusion\n'
        '#ifndef MY_HEADER_H\n'
        '#define MY_HEADER_H\n'
        'int helper(void) { return 42; }\n'
        '#endif\n\n'
        'int main(void) {\n'
        '    printf("%d\\n", helper());\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// conditional compilation\n'
        '#ifdef DEBUG\n'
        '#define LOG(msg) printf("[DEBUG] %s\\n", msg)\n'
        '#else\n'
        '#define LOG(msg)\n'
        '#endif\n\n'
        'int main(void) {\n'
        '    LOG("build with -DDEBUG to see this");\n'
        '    printf("done\\n");\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// stringification and token pasting\n'
        '#define STR(x) #x\n'
        '#define CAT(a, b) a##b\n\n'
        'int main(void) {\n'
        '    printf("%s\\n", STR(hello));     // "hello"\n'
        '    int CAT(my, var) = 7;            // int myvar = 7;\n'
        '    printf("%d\\n", myvar);\n'
        '    return 0;\n'
        '}',
    ],
    11: [
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    FILE *f = fopen("/tmp/notes.txt", "w");   // "r", "w", "a", "rb"...\n'
        '    if (!f) { perror("fopen"); return 1; }\n'
        '    fprintf(f, "hello file\\n");\n'
        '    fclose(f);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    FILE *f = fopen("/tmp/notes.txt", "r");\n'
        '    if (!f) return 1;\n'
        '    char line[128];\n'
        '    while (fgets(line, sizeof(line), f)) printf("%s", line);\n'
        '    fclose(f);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // fscanf: formatted reading (careful with %s overflow!)\n'
        '    FILE *f = fopen("/tmp/data.txt", "w+");\n'
        '    if (!f) return 1;\n'
        '    fprintf(f, "100 Alice\\n");\n'
        '    rewind(f);\n'
        '    int id;\n'
        '    char name[32];\n'
        '    fscanf(f, "%d %31s", &id, name);\n'
        '    printf("%d %s\\n", id, name);\n'
        '    fclose(f);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // binary I/O + random access\n'
        '    FILE *f = fopen("/tmp/bin.dat", "wb+");\n'
        '    int data[4] = {1, 2, 3, 4};\n'
        '    fwrite(data, sizeof(int), 4, f);\n'
        '    fseek(f, 2 * sizeof(int), SEEK_SET);   // jump to index 2\n'
        '    int x;\n'
        '    fread(&x, sizeof(int), 1, f);\n'
        '    printf("%d\\n", x);   // 3\n'
        '    fclose(f);\n'
        '    return 0;\n'
        '}',
    ],
    12: [
        '#include <stdio.h>\n'
        '#include <string.h>\n\n'
        'int main(void) {\n'
        '    char a[] = "hello";\n'
        '    char b[32];\n'
        '    strcpy(b, a);\n'
        '    printf("%s %s\\n", a, b);\n'
        '    printf("compare: %d\\n", strcmp("a", "b"));   // negative\n'
        '    printf("find: %s\\n", strchr("hello", \'l\'));\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        'int main(void) {\n'
        '    printf("%d\\n", atoi("42"));       // string -> int\n'
        '    printf("%.2f\\n", atof("3.14159"));\n'
        '    long l = strtol("0xFF", NULL, 16); // base 16 parse\n'
        '    printf("%ld\\n", l);               // 255\n'
        '    int rand_val = rand() % 100;       // 0-99 (need srand seed)\n'
        '    printf("%d\\n", rand_val);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <math.h>\n\n'
        'int main(void) {\n'
        '    printf("%.2f\\n", sqrt(16.0));     // 4.00\n'
        '    printf("%.2f\\n", pow(2.0, 10.0)); // 1024.00\n'
        '    printf("%.2f\\n", fabs(-3.5));     // 3.50\n'
        '    printf("%.2f\\n", ceil(2.1));      // 3.00\n'
        '    printf("%.2f\\n", floor(2.9));     // 2.00\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <ctype.h>\n\n'
        'int main(void) {\n'
        '    printf("%d %d\\n", isalpha(\'a\'), isdigit(\'7\'));\n'
        '    printf("%c\\n", toupper(\'a\'));\n'
        '    printf("%d\\n", isspace(\' \'));\n'
        '    return 0;\n'
        '}',
    ],
    13: [
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    unsigned x = 0b1100;   // 12\n'
        '    printf("%u\\n", x & 0b1010);   // 8\n'
        '    printf("%u\\n", x | 0b0001);   // 13\n'
        '    printf("%u\\n", x ^ 0b1111);   // 3\n'
        '    printf("%u\\n", ~x);           // bitwise complement\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// bit flags: each bit is an independent on/off switch\n'
        '#define FLAG_READ  (1 << 0)   // 0b0001\n'
        '#define FLAG_WRITE (1 << 1)   // 0b0010\n'
        '#define FLAG_EXEC  (1 << 2)   // 0b0100\n\n'
        'int main(void) {\n'
        '    unsigned perms = FLAG_READ | FLAG_WRITE;\n'
        '    if (perms & FLAG_READ) printf("can read\\n");\n'
        '    if (perms & FLAG_EXEC) printf("can exec\\n");\n'
        '    perms |= FLAG_EXEC;              // add a flag\n'
        '    perms &= ~FLAG_WRITE;            // remove a flag\n'
        '    printf("exec now: %d\\n", !!(perms & FLAG_EXEC));\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// power-of-2 checks and bit tricks\n'
        'int is_pow2(unsigned x) { return x && !(x & (x - 1)); }\n'
        'int count_ones(unsigned x) {\n'
        '    int c = 0;\n'
        '    while (x) { x &= (x - 1); c++; }   // Brian Kernighan\'s trick\n'
        '    return c;\n'
        '}\n\n'
        'int main(void) {\n'
        '    printf("%d %d\\n", is_pow2(8), is_pow2(9));   // 1 0\n'
        '    printf("%d\\n", count_ones(0b101101));        // 4\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// extract and set bitfields\n'
        '#define GET_BIT(x, n) (((x) >> (n)) & 1)\n'
        '#define SET_BIT(x, n) ((x) | (1u << (n)))\n\n'
        'int main(void) {\n'
        '    unsigned x = 0b1010;\n'
        '    printf("%d\\n", GET_BIT(x, 1));   // 1\n'
        '    printf("%u\\n", SET_BIT(x, 4));   // 0b11110 = 30\n'
        '    // bitfield struct members (implementation-defined packing)\n'
        '    struct Flags { unsigned a : 1; unsigned b : 3; };\n'
        '    struct Flags f = {1, 5};\n'
        '    printf("%d %d\\n", f.a, f.b);\n'
        '    return 0;\n'
        '}',
    ],
    14: [
        '#include <stdio.h>\n\n'
        'int add(int a, int b) { return a + b; }\n'
        'int mul(int a, int b) { return a * b; }\n\n'
        'int main(void) {\n'
        '    int (*op)(int, int) = add;    // function pointer\n'
        '    printf("%d\\n", op(2, 3));     // 5\n'
        '    op = mul;\n'
        '    printf("%d\\n", op(2, 3));     // 6\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// function pointers as arguments (callbacks)\n'
        'int apply(int (*f)(int), int x) { return f(x); }\n'
        'int square(int x) { return x * x; }\n'
        'int cube(int x) { return x * x * x; }\n\n'
        'int main(void) {\n'
        '    printf("%d %d\\n", apply(square, 4), apply(cube, 3));\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        '// qsort takes a comparator callback\n'
        'int cmp(const void *a, const void *b) {\n'
        '    return (*(int *)a) - (*(int *)b);\n'
        '}\n\n'
        'int main(void) {\n'
        '    int nums[] = {5, 2, 8, 1};\n'
        '    qsort(nums, 4, sizeof(int), cmp);\n'
        '    for (int i = 0; i < 4; i++) printf("%d ", nums[i]);\n'
        '    printf("\\n");   // 1 2 5 8\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// table of function pointers: dispatch pattern\n'
        'int add(int a, int b) { return a + b; }\n'
        'int sub(int a, int b) { return a - b; }\n'
        'int mul(int a, int b) { return a * b; }\n\n'
        'int main(void) {\n'
        '    int (*ops[])(int, int) = {add, sub, mul};\n'
        '    for (int i = 0; i < 3; i++) printf("%d ", ops[i](10, 3));\n'
        '    printf("\\n");   // 13 7 30\n'
        '    return 0;\n'
        '}',
    ],
    15: [
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        '// singly linked list node\n'
        'struct Node {\n'
        '    int data;\n'
        '    struct Node *next;\n'
        '};\n\n'
        'int main(void) {\n'
        '    struct Node *head = malloc(sizeof(struct Node));\n'
        '    head->data = 1;\n'
        '    head->next = NULL;\n'
        '    printf("%d\\n", head->data);\n'
        '    free(head);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        'struct Node { int data; struct Node *next; };\n\n'
        '// push to front\n'
        'struct Node *push(struct Node *head, int val) {\n'
        '    struct Node *n = malloc(sizeof(struct Node));\n'
        '    n->data = val;\n'
        '    n->next = head;\n'
        '    return n;\n'
        '}\n\n'
        'int main(void) {\n'
        '    struct Node *head = NULL;\n'
        '    head = push(head, 3);\n'
        '    head = push(head, 2);\n'
        '    head = push(head, 1);\n'
        '    for (struct Node *p = head; p; p = p->next) printf("%d ", p->data);\n'
        '    printf("\\n");   // 1 2 3\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        '// traversal with free (always free every node)\n'
        'struct Node { int data; struct Node *next; };\n\n'
        'void free_list(struct Node *head) {\n'
        '    while (head) {\n'
        '        struct Node *tmp = head;\n'
        '        head = head->next;\n'
        '        free(tmp);\n'
        '    }\n'
        '}\n\n'
        'int main(void) {\n'
        '    // build tiny list inline\n'
        '    struct Node *a = malloc(sizeof(*a));\n'
        '    struct Node *b = malloc(sizeof(*b));\n'
        '    a->data = 1; a->next = b;\n'
        '    b->data = 2; b->next = NULL;\n'
        '    free_list(a);\n'
        '    printf("freed\\n");\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        '// generic stack of void * — reusable data structure\n'
        'struct Stack {\n'
        '    void **items;\n'
        '    int top;\n'
        '    int cap;\n'
        '};\n\n'
        'struct Stack *stack_new(int cap) {\n'
        '    struct Stack *s = malloc(sizeof(*s));\n'
        '    s->items = malloc(cap * sizeof(void *));\n'
        '    s->top = 0;\n'
        '    s->cap = cap;\n'
        '    return s;\n'
        '}\n\n'
        'void stack_push(struct Stack *s, void *v) {\n'
        '    s->items[s->top++] = v;\n'
        '}\n\n'
        'void *stack_pop(struct Stack *s) {\n'
        '    return s->top ? s->items[--s->top] : NULL;\n'
        '}\n\n'
        'int main(void) {\n'
        '    struct Stack *s = stack_new(4);\n'
        '    int a = 1, b = 2;\n'
        '    stack_push(s, &a);\n'
        '    stack_push(s, &b);\n'
        '    printf("%d %d\\n", *(int *)stack_pop(s), *(int *)stack_pop(s));  // 2 1\n'
        '    free(s->items);\n'
        '    free(s);\n'
        '    return 0;\n'
        '}',
    ],
    16: [
        '#include <stdio.h>\n\n'
        '// classic recursion: factorial\n'
        'long fact(int n) {\n'
        '    if (n <= 1) return 1;\n'
        '    return n * fact(n - 1);\n'
        '}\n\n'
        'int main(void) { printf("%ld\\n", fact(5)); return 0; }',
        '#include <stdio.h>\n\n'
        '// fibonacci: exponential without memoization\n'
        'long fib(int n) {\n'
        '    if (n <= 1) return n;\n'
        '    return fib(n - 1) + fib(n - 2);\n'
        '}\n\n'
        'int main(void) { printf("%ld\\n", fib(10)); return 0; }',
        '#include <stdio.h>\n\n'
        '// recursion over arrays: sum\n'
        'int sum(int arr[], int n) {\n'
        '    if (n == 0) return 0;\n'
        '    return arr[n - 1] + sum(arr, n - 1);\n'
        '}\n\n'
        'int main(void) {\n'
        '    int nums[] = {1, 2, 3, 4};\n'
        '    printf("%d\\n", sum(nums, 4));   // 10\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// recursion for search: binary search\n'
        'int bsearch_rec(int arr[], int lo, int hi, int target) {\n'
        '    if (lo > hi) return -1;\n'
        '    int mid = lo + (hi - lo) / 2;\n'
        '    if (arr[mid] == target) return mid;\n'
        '    if (arr[mid] > target) return bsearch_rec(arr, lo, mid - 1, target);\n'
        '    return bsearch_rec(arr, mid + 1, hi, target);\n'
        '}\n\n'
        'int main(void) {\n'
        '    int nums[] = {1, 3, 5, 7, 9};\n'
        '    printf("%d\\n", bsearch_rec(nums, 0, 4, 7));   // 3\n'
        '    return 0;\n'
        '}',
    ],
    17: [
        '#include <stdio.h>\n'
        '#include <errno.h>\n'
        '#include <string.h>\n\n'
        'int main(void) {\n'
        '    FILE *f = fopen("/nonexistent/file", "r");\n'
        '    if (!f) {\n'
        '        printf("errno=%d %s\\n", errno, strerror(errno));\n'
        '        perror("fopen");\n'
        '    }\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <errno.h>\n'
        '#include <math.h>\n\n'
        'int main(void) {\n'
        '    errno = 0;\n'
        '    double r = sqrt(-1.0);   // domain error\n'
        '    if (errno == EDOM) printf("math domain error\\n");\n'
        '    (void)r;\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// return-code convention: 0 = success, non-zero = error\n'
        'int divide(int a, int b, int *out) {\n'
        '    if (b == 0) return -1;\n'
        '    *out = a / b;\n'
        '    return 0;\n'
        '}\n\n'
        'int main(void) {\n'
        '    int result;\n'
        '    if (divide(10, 0, &result) != 0) {\n'
        '        printf("division error\\n");\n'
        '        return 1;\n'
        '    }\n'
        '    printf("%d\\n", result);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <setjmp.h>\n\n'
        '// setjmp/longjmp: non-local goto for error handling\n'
        'static jmp_buf env;\n\n'
        'int main(void) {\n'
        '    if (setjmp(env) == 0) {\n'
        '        printf("about to longjmp\\n");\n'
        '        longjmp(env, 1);\n'
        '    } else {\n'
        '        printf("recovered from longjmp\\n");\n'
        '    }\n'
        '    return 0;\n'
        '}',
    ],
    18: [
        '// point.h — declaration (interface)\n'
        '#ifndef POINT_H\n'
        '#define POINT_H\n'
        'struct Point { int x; int y; };\n'
        'int dist2(struct Point *p);\n'
        '#endif',
        '// point.c — implementation\n'
        '#include "point.h"\n'
        'int dist2(struct Point *p) { return p->x * p->x + p->y * p->y; }',
        '// main.c — includes the header\n'
        '#include <stdio.h>\n'
        '#include "point.h"\n'
        'int main(void) {\n'
        '    struct Point p = {3, 4};\n'
        '    printf("%d\\n", dist2(&p));   // 25\n'
        '    return 0;\n'
        '}\n'
        '// compile: gcc main.c point.c -o app',
        '#include <stdio.h>\n\n'
        '// static: internal linkage — visible only in this file\n'
        'static int counter = 0;\n'
        'static void bump(void) { counter++; }\n\n'
        'int main(void) {\n'
        '    bump(); bump();\n'
        '    printf("%d\\n", counter);   // 2\n'
        '    return 0;\n'
        '}',
    ],
    19: [
        '# Makefile — build automation\n'
        'CC = gcc\n'
        'CFLAGS = -Wall -Wextra -std=c17\n\n'
        'app: main.o point.o\n'
        '\t$(CC) $(CFLAGS) -o app main.o point.o\n\n'
        'main.o: main.c point.h\n'
        '\t$(CC) $(CFLAGS) -c main.c\n\n'
        'point.o: point.c point.h\n'
        '\t$(CC) $(CFLAGS) -c point.c\n\n'
        'clean:\n'
        '\trm -f *.o app',
        '# Makefile with automatic variables\n'
        'CC = gcc\n'
        'CFLAGS = -Wall -Wextra -std=c17\n'
        'SRCS = main.c point.c\n'
        'OBJS = $(SRCS:.c=.o)\n\n'
        'app: $(OBJS)\n'
        '\t$(CC) $(CFLAGS) -o $@ $^\n\n'
        '%.o: %.c point.h\n'
        '\t$(CC) $(CFLAGS) -c $< -o $@\n\n'
        'clean:\n'
        '\trm -f $(OBJS) app',
        '# compile flags you should know\n'
        '# -g          : debug symbols (for gdb)\n'
        '# -O2 / -O3   : optimization\n'
        '# -Wall -Wextra : all warnings\n'
        '# -fsanitize=address : ASan (memory errors)\n'
        '# -fsanitize=undefined : UBSan (UB detection)\n'
        '#\n'
        '# gcc -g -O0 -fsanitize=address,undefined -o app main.c',
        '# debug with gdb\n'
        '# gcc -g -o app app.c\n'
        '# gdb ./app\n'
        '#   (gdb) break main\n'
        '#   (gdb) run\n'
        '#   (gdb) next / step / print x / bt / quit\n'
        '#\n'
        '# valgrind for memory errors:\n'
        '# valgrind --leak-check=full ./app',
    ],
    20: [
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // out-of-bounds read — undefined behavior\n'
        '    int arr[3] = {1, 2, 3};\n'
        '    printf("%d\\n", arr[5]);   // UB! reads past the array\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        'int main(void) {\n'
        '    // signed overflow is UB\n'
        '    int x = 2147483647;\n'
        '    int y = x + 1;            // UB (compile with -fsanitize=signed-integer-overflow)\n'
        '    printf("%d\\n", y);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdlib.h>\n\n'
        'int main(void) {\n'
        '    // use-after-free — UB\n'
        '    int *p = malloc(sizeof(int));\n'
        '    *p = 42;\n'
        '    free(p);\n'
        '    printf("%d\\n", *p);      // UB! reading freed memory\n'
        '    return 0;\n'
        '}\n'
        '// detect with: valgrind ./app  or  -fsanitize=address',
        '#include <stdio.h>\n\n'
        '// volatile: tells the compiler the value may change externally\n'
        'volatile int flag = 0;\n\n'
        '// restrict: no aliasing promise (optimizer aid)\n'
        'void scale(int *restrict dst, const int *restrict src, int n, int k) {\n'
        '    for (int i = 0; i < n; i++) dst[i] = src[i] * k;\n'
        '}\n\n'
        'int main(void) {\n'
        '    int a[3] = {1, 2, 3}, b[3];\n'
        '    scale(b, a, 3, 10);\n'
        '    printf("%d %d %d\\n", b[0], b[1], b[2]);\n'
        '    return 0;\n'
        '}',
    ],
    21: [
        '#include <stdio.h>\n'
        '#include <stdarg.h>\n\n'
        '// variadic function: printf-like\n'
        'int sum(int count, ...) {\n'
        '    va_list args;\n'
        '    va_start(args, count);\n'
        '    int total = 0;\n'
        '    for (int i = 0; i < count; i++) total += va_arg(args, int);\n'
        '    va_end(args);\n'
        '    return total;\n'
        '}\n\n'
        'int main(void) {\n'
        '    printf("%d\\n", sum(3, 10, 20, 30));   // 60\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n\n'
        '// inline function: hint to the compiler\n'
        'static inline int clamp(int v, int lo, int hi) {\n'
        '    if (v < lo) return lo;\n'
        '    if (v > hi) return hi;\n'
        '    return v;\n'
        '}\n\n'
        'int main(void) {\n'
        '    printf("%d %d\\n", clamp(150, 0, 100), clamp(-5, 0, 100));\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <threads.h>   // C11 threads\n\n'
        'int worker(void *arg) {\n'
        '    long id = (long)arg;\n'
        '    printf("thread %ld\\n", id);\n'
        '    return 0;\n'
        '}\n\n'
        'int main(void) {\n'
        '    thrd_t t1, t2;\n'
        '    thrd_create(&t1, worker, (void *)1L);\n'
        '    thrd_create(&t2, worker, (void *)2L);\n'
        '    thrd_join(t1, NULL);\n'
        '    thrd_join(t2, NULL);\n'
        '    return 0;\n'
        '}',
        '#include <stdio.h>\n'
        '#include <stdatomic.h>\n\n'
        '// atomic types (C11): lock-free ops\n'
        'int main(void) {\n'
        '    atomic_int counter = 0;\n'
        '    atomic_fetch_add(&counter, 5);\n'
        '    printf("%d\\n", atomic_load(&counter));   // 5\n'
        '    return 0;\n'
        '}',
    ],
}

# ─── Lesson metadata ──────────────────────────────────────────────────
LESSONS = [
    dict(slug='c-01-getting-started', title='Getting Started with C',
         desc='Set up a C toolchain with gcc, understand compile/run, main function, and standard streams.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Install gcc and compile your first C program',
               'Understand the compile pipeline (preprocess, compile, link)',
               'Use main with argc/argv',
               'Write to stdout and stderr'],
         refs=[dict(title='Beej’s Guide to C — Chapter 2', url='https://beej.us/guide/bgc/html/split/hello-world.html'),
               dict(title='learn-c.org — Hello World', url='https://learn-c.org/en/Hello%2C_World'),
               dict(title='cppreference — main function', url='https://en.cppreference.com/w/c/language/main_function')]),
    dict(slug='c-02-variables-types', title='Variables and Data Types',
         desc='Integral and floating types, fixed-width types, sizeof, and enumeration.',
         dur='60 min', diff='beginner', prereq=['C-01'],
         objs=['Use int, unsigned, float, double, char, _Bool',
               'Use fixed-width types from stdint.h',
               'Understand signed vs unsigned overflow',
               'Use enum and limits.h constants'],
         refs=[dict(title='cppreference — Fundamental Types', url='https://en.cppreference.com/w/c/language/type'),
               dict(title='learn-c.org — Variables and Types', url='https://learn-c.org/en/Variables_and_Types'),
               dict(title='cppreference — Integer Types', url='https://en.cppreference.com/w/c/language/arithmetic_types')]),
    dict(slug='c-03-operators', title='Operators and Expressions',
         desc='Arithmetic, comparison, logical, bitwise operators, and precedence.',
         dur='60 min', diff='beginner', prereq=['C-02'],
         objs=['Use arithmetic and comparison operators',
               'Understand short-circuit logical operators',
               'Use bitwise operators',
               'Master assignment and increment operators'],
         refs=[dict(title='cppreference — Operator Precedence', url='https://en.cppreference.com/w/c/language/operator_precedence'),
               dict(title='learn-c.org — Operators', url='https://learn-c.org/en/Operators'),
               dict(title='cppreference — Arithmetic Operators', url='https://en.cppreference.com/w/c/language/operator_arithmetic')]),
    dict(slug='c-04-control-flow', title='Control Flow',
         desc='if/else, switch, for, while, do-while loops, and jump statements.',
         dur='60 min', diff='beginner', prereq=['C-03'],
         objs=['Write if/else branching logic',
               'Use switch statements',
               'Use for, while, and do-while loops',
               'Apply break and continue'],
         refs=[dict(title='learn-c.org — Conditions', url='https://learn-c.org/en/Conditions'),
               dict(title='learn-c.org — Loops', url='https://learn-c.org/en/Loops'),
               dict(title='cppreference — Statements', url='https://en.cppreference.com/w/c/language/statements')]),
    dict(slug='c-05-functions', title='Functions and Prototypes',
         desc='Function declarations, pass-by-value, pass-by-pointer, and recursion.',
         dur='60 min', diff='beginner', prereq=['C-04'],
         objs=['Declare functions with prototypes',
               'Understand pass-by-value semantics',
               'Pass pointers to mutate caller state',
               'Write recursive functions'],
         refs=[dict(title='learn-c.org — Functions', url='https://learn-c.org/en/Functions'),
               dict(title='cppreference — Function Declarations', url='https://en.cppreference.com/w/c/language/functions'),
               dict(title='Beej’s Guide — Functions', url='https://beej.us/guide/bgc/html/split/function-basics.html')]),
    dict(slug='c-06-arrays-strings', title='Arrays and Strings',
         desc='One and multi-dimensional arrays, null-terminated strings, string.h.',
         dur='60 min', diff='beginner', prereq=['C-05'],
         objs=['Declare and iterate arrays',
               'Work with C strings and string.h',
               'Use multi-dimensional arrays',
               'Understand array decay to pointers'],
         refs=[dict(title='learn-c.org — Arrays', url='https://learn-c.org/en/Arrays'),
               dict(title='learn-c.org — Strings', url='https://learn-c.org/en/Strings'),
               dict(title='cppreference — String Functions', url='https://en.cppreference.com/w/c/string/byte')]),
    dict(slug='c-07-pointers', title='Pointers',
         desc='Address-of, dereference, pointer arithmetic, pointer-to-pointer, void*.',
         dur='75 min', diff='intermediate', prereq=['C-06'],
         objs=['Take addresses and dereference pointers',
               'Do pointer arithmetic with arrays',
               'Use pointer-to-pointer',
               'Work with NULL and void*'],
         refs=[dict(title='learn-c.org — Pointers', url='https://learn-c.org/en/Pointers'),
               dict(title='cppreference — Pointer Declarations', url='https://en.cppreference.com/w/c/language/pointer'),
               dict(title='Beej’s Guide — Pointers', url='https://beej.us/guide/bgc/html/split/pointers.html')]),
    dict(slug='c-08-structs-unions', title='Structs and Unions',
         desc='Struct declaration, member access, arrow operator, copies, unions.',
         dur='60 min', diff='intermediate', prereq=['C-07'],
         objs=['Declare and use structs',
               'Access members through pointers with ->',
               'Copy and pass structs by value',
               'Use unions for shared memory'],
         refs=[dict(title='learn-c.org — Structures', url='https://learn-c.org/en/Structures'),
               dict(title='cppreference — Struct Declaration', url='https://en.cppreference.com/w/c/language/struct'),
               dict(title='cppreference — Union Declaration', url='https://en.cppreference.com/w/c/language/union')]),
    dict(slug='c-09-memory', title='Dynamic Memory',
         desc='malloc, calloc, realloc, free, memory leaks, and heap patterns.',
         dur='75 min', diff='intermediate', prereq=['C-08'],
         objs=['Allocate with malloc and free',
               'Zero-init with calloc and resize with realloc',
               'Avoid leaks and double-free',
               'Return heap arrays from functions'],
         refs=[dict(title='learn-c.org — Dynamic Memory', url='https://learn-c.org/en/Dynamic_allocation'),
               dict(title='cppreference — malloc', url='https://en.cppreference.com/w/c/memory/malloc'),
               dict(title='cppreference — free', url='https://en.cppreference.com/w/c/memory/free')]),
    dict(slug='c-10-preprocessor', title='Preprocessor and Macros',
         desc='#define, function-like macros, include guards, conditional compilation.',
         dur='60 min', diff='intermediate', prereq=['C-09'],
         objs=['Define object-like macros',
               'Write function-like macros safely',
               'Use include guards',
               'Compile conditionally with #ifdef'],
         refs=[dict(title='cppreference — Preprocessor', url='https://en.cppreference.com/w/c/preprocessor'),
               dict(title='learn-c.org — Preprocessor', url='https://learn-c.org/en/Preprocessor'),
               dict(title='cppreference — Conditional Inclusion', url='https://en.cppreference.com/w/c/preprocessor/conditional')]),
    dict(slug='c-11-file-io', title='File I/O',
         desc='fopen, fprintf/fscanf, fgets, binary I/O, fseek, and error handling.',
         dur='60 min', diff='intermediate', prereq=['C-10'],
         objs=['Open files with fopen and modes',
               'Read lines with fgets',
               'Read formatted data with fscanf',
               'Do binary I/O with fwrite/fread and fseek'],
         refs=[dict(title='learn-c.org — File I/O', url='https://learn-c.org/en/File_I/O'),
               dict(title='cppreference — fopen', url='https://en.cppreference.com/w/c/io/fopen'),
               dict(title='cppreference — Input/Output Functions', url='https://en.cppreference.com/w/c/io')]),
    dict(slug='c-12-stdlib', title='Standard Library',
         desc='string.h, stdlib.h, math.h, and ctype.h essentials.',
         dur='60 min', diff='intermediate', prereq=['C-11'],
         objs=['Use string.h functions',
               'Convert strings with atoi/strtol',
               'Use math.h functions',
               'Use ctype.h character classification'],
         refs=[dict(title='cppreference — Standard Library Header', url='https://en.cppreference.com/w/c/header'),
               dict(title='cppreference — string.h', url='https://en.cppreference.com/w/c/string'),
               dict(title='cppreference — stdlib.h', url='https://en.cppreference.com/w/c/header/stdlib')]),
    dict(slug='c-13-bit-manipulation', title='Bit Manipulation',
         desc='Bitwise operators, bit flags, bit tricks, and bitfields.',
         dur='60 min', diff='intermediate', prereq=['C-12'],
         objs=['Apply bitwise AND/OR/XOR/NOT',
               'Use bit flags with masks',
               'Apply power-of-2 and counting tricks',
               'Extract and set individual bits'],
         refs=[dict(title='cppreference — Bitwise Operators', url='https://en.cppreference.com/w/c/language/operator_arithmetic'),
               dict(title='learn-c.org — Bitwise Operators', url='https://learn-c.org/en/Bitwise_operators'),
               dict(title='Bit Twiddling Hacks', url='https://graphics.stanford.edu/~seander/bithacks.html')]),
    dict(slug='c-14-function-pointers', title='Function Pointers and Callbacks',
         desc='Function pointer syntax, callbacks, qsort comparators, dispatch tables.',
         dur='75 min', diff='advanced', prereq=['C-13'],
         objs=['Declare and call function pointers',
               'Pass callbacks as arguments',
               'Write qsort comparators',
               'Build dispatch tables'],
         refs=[dict(title='learn-c.org — Function Pointers', url='https://learn-c.org/en/Function_Pointers'),
               dict(title='cppreference — qsort', url='https://en.cppreference.com/w/c/algorithm/qsort'),
               dict(title='Beej’s Guide — Function Pointers', url='https://beej.us/guide/bgc/html/split/pointers-part-ii.html')]),
    dict(slug='c-15-data-structures', title='Linked Lists and Data Structures',
         desc='Struct nodes, linked lists, traversal, free, and reusable patterns.',
         dur='75 min', diff='advanced', prereq=['C-14'],
         objs=['Build singly linked list nodes',
               'Push and traverse linked lists',
               'Free lists safely',
               'Design reusable container patterns'],
         refs=[dict(title='learn-c.org — Linked Lists', url='https://learn-c.org/en/Linked_lists'),
               dict(title='cppreference — Struct Pointer Members', url='https://en.cppreference.com/w/c/language/struct'),
               dict(title='Wikipedia — Linked List', url='https://en.wikipedia.org/wiki/Linked_list')]),
    dict(slug='c-16-recursion', title='Recursion',
         desc='Recursive functions, factorial, fibonacci, divide-and-conquer.',
         dur='45 min', diff='intermediate', prereq=['C-15'],
         objs=['Write base cases and recursive steps',
               'Understand exponential blowup',
               'Recurse over arrays',
               'Use recursion for binary search'],
         refs=[dict(title='learn-c.org — Recursion', url='https://learn-c.org/en/Recursion'),
               dict(title='cppreference — Recursion Notes', url='https://en.cppreference.com/w/c/language/functions'),
               dict(title='Khan Academy — Recursion', url='https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion')]),
    dict(slug='c-17-error-handling', title='Error Handling',
         desc='errno, perror, strerror, return codes, and setjmp/longjmp.',
         dur='60 min', diff='intermediate', prereq=['C-16'],
         objs=['Use errno with perror and strerror',
               'Detect math domain errors',
               'Use return-code conventions',
               'Use setjmp/longjmp for non-local errors'],
         refs=[dict(title='cppreference — errno', url='https://en.cppreference.com/w/c/error/errno'),
               dict(title='cppreference — perror', url='https://en.cppreference.com/w/c/io/perror'),
               dict(title='cppreference — setjmp', url='https://en.cppreference.com/w/c/program/setjmp')]),
    dict(slug='c-18-multi-file', title='Multi-file Projects and Headers',
         desc='Header files, include guards, separate compilation, static linkage.',
         dur='60 min', diff='intermediate', prereq=['C-17'],
         objs=['Split code into .h and .c files',
               'Write include guards',
               'Compile multiple translation units',
               'Use static for internal linkage'],
         refs=[dict(title='cppreference — Source Files', url='https://en.cppreference.com/w/c/language/translation_phases'),
               dict(title='Beej’s Guide — Multi-file', url='https://beej.us/guide/bgc/html/split/header-files.html'),
               dict(title='learn-c.org — Header Files', url='https://learn-c.org/en/Header_Files')]),
    dict(slug='c-19-build-tooling', title='Make and Build Tooling',
         desc='Makefiles, targets, automatic variables, compiler flags, sanitizers.',
         dur='60 min', diff='intermediate', prereq=['C-18'],
         objs=['Write Makefiles with targets and deps',
               'Use automatic variables',
               'Compile with -Wall -Wextra -fsanitize',
               'Run gdb and valgrind'],
         refs=[dict(title='GNU Make Manual', url='https://www.gnu.org/software/make/manual/html_node/Introduction.html'),
               dict(title='gcc Options Summary', url='https://gcc.gnu.org/onlinedocs/gcc/Option-Summary.html'),
               dict(title='Valgrind Quick Start', url='https://valgrind.org/docs/manual/quick-start.html')]),
    dict(slug='c-20-debugging', title='Undefined Behavior and Debugging',
         desc='OOB access, signed overflow, use-after-free, volatile, restrict, sanitizers.',
         dur='75 min', diff='advanced', prereq=['C-19'],
         objs=['Recognize out-of-bounds undefined behavior',
               'Understand signed overflow UB',
               'Avoid use-after-free',
               'Use volatile, restrict, and sanitizers'],
         refs=[dict(title='cppreference — Undefined Behavior', url='https://en.cppreference.com/w/c/language/behavior'),
               dict(title='gcc -fsanitize docs', url='https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html'),
               dict(title='Valgrind Manual', url='https://valgrind.org/docs/manual/mc-manual.html')]),
    dict(slug='c-21-advanced', title='Advanced: Variadics, Threads, and Atomics',
         desc='Variadic functions, inline, C11 threads, atomics, low-level control.',
         dur='75 min', diff='expert', prereq=['C-20'],
         objs=['Write variadic functions with stdarg.h',
               'Use inline functions',
               'Create threads with C11 threads.h',
               'Use atomic operations'],
         refs=[dict(title='cppreference — Variadic Functions', url='https://en.cppreference.com/w/c/variadic'),
               dict(title='cppreference — threads.h', url='https://en.cppreference.com/w/c/thread'),
               dict(title='cppreference — Atomics', url='https://en.cppreference.com/w/c/atomic')]),
]


def sample_intro(i, obj):
    """Vary the prose per sub-topic position so the lesson body is not a verbatim template."""
    openings = [
        'Start with the foundations — read the runnable example carefully and trace its output before moving on.',
        'Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.',
        'Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.',
        'Put it together — extend the example to combine this concept with what you learned in earlier lessons.',
    ]
    return f'Target: {obj}. {openings[i % len(openings)]}'


def build_lesson(ls, samples):
    n = ls['order']
    code_list = samples.get(n, samples.get(1))
    objs = ls['objs']

    concepts = []
    for i in range(4):
        obj = objs[i] if i < len(objs) else objs[0]
        sample = code_list[i] if i < len(code_list) else code_list[0]
        concepts.append(f"""### {i + 1}. {obj}

{sample_intro(i, obj)}

```c
{sample}
```""")

    qs = [
        f'What is the key idea behind "{ls["title"]}"?',
        'Write a small program that exercises at least two concepts from this lesson.',
        'How would you explain this topic to a fellow developer in one paragraph?',
    ]
    llm = [
        f'"Explain {ls["title"]} with analogies and real-world examples"',
        f'"Show me common mistakes beginners make with {ls["title"]}"',
        f'"Provide advanced patterns and performance considerations for {ls["title"]}"',
    ]
    kts = [
        f'Master the core ideas of {ls["title"]} through practice',
        'Combine this lesson with prior lessons to build real programs',
        'Explore the linked cppreference docs for authoritative depth',
    ]

    fm = {
        'title': ls['title'],
        'description': ls['desc'],
        'type': 'lesson',
        'order': n,
        'duration': ls['dur'],
        'difficulty': ls['diff'],
        'learning_objectives': objs,
        'knowledge_refs': [f'c/{ls["slug"]}'],
        'prerequisites': ls['prereq'],
        'references': ls['refs'],
    }

    slug_h1 = ls['slug'].upper()
    intro = f"{ls['desc']} By the end of this lesson you will be able to: {'; '.join(objs)}."
    content = f"""---
{json.dumps(fm, indent=2, ensure_ascii=False)}
---

# {slug_h1}: {ls['title']}

## Introduction

{intro}

## Key Concepts

{chr(10).join(concepts)}

## Practice Questions

1. {qs[0]}
1. {qs[1]}
1. {qs[2]}

## LLM Prompts for Deeper Understanding

1. {llm[0]}
1. {llm[1]}
1. {llm[2]}

## Key Takeaways

- {kts[0]}
- {kts[1]}
- {kts[2]}

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
"""
    return content


def main():
    os.makedirs(BASE, exist_ok=True)
    for f in ['fundamentals.md', 'practical-guide.md']:
        p = os.path.join(BASE, f)
        if os.path.exists(p):
            os.remove(p)
            print(f'removed {f}')

    for i, ls in enumerate(LESSONS, 1):
        ls['order'] = i
        with open(os.path.join(BASE, f"{ls['slug']}.md"), 'w') as fh:
            fh.write(build_lesson(ls, CODE))
    print(f'wrote {len(LESSONS)} lesson files')

    idx_path = os.path.join(BASE, 'index.json')
    with open(idx_path) as fh:
        idx = json.load(fh)
    idx['lessons'] = [dict(
        slug=ls['slug'],
        title=ls['title'],
        description=ls['desc'],
        type='lesson',
        order=ls['order'],
        duration=ls['dur'],
        difficulty=ls['diff'],
        knowledge_refs=[f'c/{ls["slug"]}'],
    ) for ls in LESSONS]
    with open(idx_path, 'w') as fh:
        json.dump(idx, fh, indent=2, ensure_ascii=False)
    print('updated index.json')


if __name__ == '__main__':
    main()
