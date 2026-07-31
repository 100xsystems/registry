#!/usr/bin/env python3
"""Generate the 21-lesson C++ curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from cppreference.com + learncpp.com.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'cpp'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'cpp')

CODE = {
    1: [
        '#include <iostream>\n\n'
        'int main() {\n'
        '    std::cout << "Hello, 100X Systems!" << std::endl;\n'
        '    return 0;\n'
        '}\n'
        '// compile: g++ -Wall -Wextra -std=c++20 -o hello hello.cpp',
        '#include <iostream>\n\n'
        'int main(int argc, char *argv[]) {\n'
        '    std::cout << "argc = " << argc << "\\n";\n'
        '    for (int i = 0; i < argc; i++) std::cout << argv[i] << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        '// namespaces organize code and avoid collisions\n'
        'namespace math {\n'
        '    int add(int a, int b) { return a + b; }\n'
        '}\n\n'
        'int main() {\n'
        '    std::cout << math::add(2, 3) << "\\n";\n'
        '    using std::cout;   // bring a name into scope\n'
        '    cout << "using declaration\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <string>\n\n'
        'int main() {\n'
        '    // type-safe I/O streams\n'
        '    std::string name;\n'
        '    std::cout << "Enter name: ";\n'
        '    std::getline(std::cin, name);\n'
        '    std::cout << "Hello, " << name << "!\\n";\n'
        '    return 0;\n'
        '}',
    ],
    2: [
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int i = 42;\n'
        '    unsigned u = 42u;\n'
        '    long long ll = 42LL;\n'
        '    float f = 3.14f;\n'
        '    double d = 3.14;\n'
        '    bool b = true;\n'
        '    char c = \'A\';\n'
        '    std::cout << i << " " << u << " " << ll << " " << f << " " << d << " " << b << " " << c << "\\n";\n'
        '    std::cout << "sizeof(int)=" << sizeof(int) << " sizeof(double)=" << sizeof(double) << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    // const: value never changes; constexpr: compile-time constant\n'
        '    const int days = 7;\n'
        '    constexpr double pi = 3.14159265;\n'
        '    std::cout << days << " " << pi << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    // auto deduces the type\n'
        '    auto x = 42;          // int\n'
        '    auto y = 3.14;        // double\n'
        '    auto s = "hello";     // const char*\n'
        '    std::cout << x << " " << y << " " << s << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <cstdint>\n\n'
        'int main() {\n'
        '    // fixed-width integer types\n'
        '    std::int32_t a = -100;\n'
        '    std::uint64_t b = 100ULL;\n'
        '    std::cout << a << " " << b << "\\n";\n'
        '    return 0;\n'
        '}',
    ],
    3: [
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int a = 17, b = 5;\n'
        '    std::cout << a + b << " " << a - b << " " << a * b << " " << a / b << " " << a % b << "\\n";\n'
        '    // 22 12 85 3 2\n'
        '    std::cout << 17.0 / 5.0 << "\\n";   // 3.4 (float division)\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int a = 5, b = 3;\n'
        '    std::cout << (a == b) << (a != b) << (a < b) << (a >= b) << "\\n";\n'
        '    bool both = a > 0 && b > 0;\n'
        '    bool either = a > 100 || b > 0;\n'
        '    std::cout << both << " " << either << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    unsigned a = 0b1100, b = 0b1010;\n'
        '    std::cout << (a & b) << " " << (a | b) << " " << (a ^ b) << "\\n";  // 8 14 6\n'
        '    std::cout << (a << 1) << " " << (a >> 1) << "\\n";                  // 24 6\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int x = 10;\n'
        '    x += 5;   // 15\n'
        '    x *= 2;   // 30\n'
        '    std::cout << x << "\\n";\n'
        '    int i = 5;\n'
        '    ++i;\n'
        '    std::cout << i << " ";   // 6 (prefix)\n'
        '    std::cout << i++ << " ";   // 6 (postfix: returns old value)\n'
        '    std::cout << i << "\\n";   // 7 (i already incremented)\n'
        '    return 0;\n'
        '}',
    ],
    4: [
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int score = 85;\n'
        '    if (score >= 90) std::cout << "A\\n";\n'
        '    else if (score >= 80) std::cout << "B\\n";\n'
        '    else std::cout << "C\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int day = 3;\n'
        '    switch (day) {\n'
        '        case 1: std::cout << "Monday\\n"; break;\n'
        '        case 2: std::cout << "Tuesday\\n"; break;\n'
        '        default: std::cout << "Other\\n"; break;\n'
        '    }\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    for (int i = 0; i < 5; i++) std::cout << i << " ";   // 0 1 2 3 4\n'
        '    std::cout << "\\n";\n'
        '    int j = 0;\n'
        '    while (j < 3) { std::cout << j << " "; j++; }        // 0 1 2\n'
        '    std::cout << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n\n'
        'int main() {\n'
        '    // range-based for (C++11): iterate any container\n'
        '    std::vector<int> v = {10, 20, 30};\n'
        '    for (int x : v) std::cout << x << " ";\n'
        '    std::cout << "\\n";\n'
        '    for (auto &x : v) x *= 2;   // modify in place\n'
        '    std::cout << v[1] << "\\n";  // 40\n'
        '    return 0;\n'
        '}',
    ],
    5: [
        '#include <iostream>\n\n'
        'int add(int a, int b);   // declaration\n\n'
        'int main() {\n'
        '    std::cout << add(2, 3) << "\\n";\n'
        '    return 0;\n'
        '}\n\n'
        'int add(int a, int b) { return a + b; }   // definition',
        '#include <iostream>\n\n'
        '// function overloading: same name, different signatures\n'
        'int max(int a, int b) { return a > b ? a : b; }\n'
        'double max(double a, double b) { return a > b ? a : b; }\n'
        'int max(int a, int b, int c) { return max(max(a, b), c); }\n\n'
        'int main() {\n'
        '    std::cout << max(3, 7) << " " << max(2.5, 1.5) << " " << max(1, 5, 3) << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <string>\n\n'
        '// default arguments + reference parameters\n'
        'void greet(const std::string &name, const std::string &prefix = "Hello") {\n'
        '    std::cout << prefix << ", " << name << "!\\n";\n'
        '}\n\n'
        'int main() {\n'
        '    greet("Alice");          // uses default prefix\n'
        '    greet("Bob", "Hi");\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <string>\n\n'
        '// const reference: read without copying\n'
        'int length(const std::string &s) { return s.size(); }\n\n'
        'int main() {\n'
        '    std::string s = "hello";\n'
        '    std::cout << length(s) << "\\n";   // 5\n'
        '    return 0;\n'
        '}',
    ],
    6: [
        '#include <iostream>\n'
        '#include <vector>\n\n'
        'int main() {\n'
        '    std::vector<int> v = {1, 2, 3};\n'
        '    v.push_back(4);\n'
        '    v.insert(v.begin(), 0);\n'
        '    std::cout << v.size() << " " << v[0] << " " << v.back() << "\\n";  // 5 0 4\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <string>\n\n'
        'int main() {\n'
        '    std::string s = "hello";\n'
        '    s += " world";\n'
        '    s.push_back(\'!\');\n'
        '    std::cout << s << "\\n";                    // hello world!\n'
        '    std::cout << s.substr(0, 5) << "\\n";      // hello\n'
        '    std::cout << (s.find("world") != std::string::npos) << "\\n";  // 1\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int arr[5] = {1, 2, 3, 4, 5};\n'
        '    for (int i = 0; i < 5; i++) std::cout << arr[i] << " ";\n'
        '    std::cout << "\\n";\n'
        '    // range-based for over C array\n'
        '    for (int x : arr) std::cout << x << " ";\n'
        '    std::cout << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    // multi-dimensional array\n'
        '    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};\n'
        '    std::cout << grid[1][0] << "\\n";   // 4\n'
        '    return 0;\n'
        '}',
    ],
    7: [
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int x = 42;\n'
        '    int *p = &x;                  // pointer\n'
        '    int &r = x;                   // reference (alias)\n'
        '    *p = 100;\n'
        '    std::cout << x << " " << r << "\\n";   // 100 100\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        '// references cannot be null and always alias something\n'
        'void swap(int &a, int &b) {\n'
        '    int t = a; a = b; b = t;\n'
        '}\n\n'
        'int main() {\n'
        '    int x = 1, y = 2;\n'
        '    swap(x, y);\n'
        '    std::cout << x << " " << y << "\\n";   // 2 1\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'int main() {\n'
        '    int nums[4] = {10, 20, 30, 40};\n'
        '    int *p = nums;                 // array decays to pointer\n'
        '    std::cout << *p << " " << *(p + 2) << "\\n";   // 10 30\n'
        '    p++;\n'
        '    std::cout << *p << "\\n";      // 20\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        '// pointer-to-pointer and nullptr (C++11)\n'
        'int main() {\n'
        '    int x = 42;\n'
        '    int *p = &x;\n'
        '    int **pp = &p;\n'
        '    std::cout << **pp << "\\n";    // 42\n'
        '    int *q = nullptr;\n'
        '    if (q) std::cout << "non-null\\n";\n'
        '    else std::cout << "null\\n";\n'
        '    return 0;\n'
        '}',
    ],
    8: [
        '#include <iostream>\n\n'
        'class BankAccount {\n'
        'private:\n'
        '    double balance_ = 0.0;\n'
        'public:\n'
        '    void deposit(double amount) { balance_ += amount; }\n'
        '    double balance() const { return balance_; }\n'
        '};\n\n'
        'int main() {\n'
        '    BankAccount acct;\n'
        '    acct.deposit(100);\n'
        '    std::cout << acct.balance() << "\\n";   // 100\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'class Point {\n'
        'public:\n'
        '    Point(int x, int y) : x_(x), y_(y) {}   // constructor init list\n'
        '    void print() const { std::cout << "(" << x_ << ", " << y_ << ")\\n"; }\n'
        'private:\n'
        '    int x_, y_;\n'
        '};\n\n'
        'int main() {\n'
        '    Point p(3, 4);\n'
        '    p.print();\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'class Counter {\n'
        'public:\n'
        '    Counter() { instances_++; }\n'
        '    static int instances() { return instances_; }\n'
        'private:\n'
        '    static int instances_;\n'
        '};\n\n'
        'int Counter::instances_ = 0;\n\n'
        'int main() {\n'
        '    Counter a, b, c;\n'
        '    std::cout << Counter::instances() << "\\n";   // 3 (static member)\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        '// const methods + this pointer\n'
        'class Square {\n'
        'public:\n'
        '    Square(int side) : side_(side) {}\n'
        '    int area() const { return side_ * side_; }\n'
        '    Square *grow() { side_ *= 2; return this; }\n'
        'private:\n'
        '    int side_;\n'
        '};\n\n'
        'int main() {\n'
        '    Square s(4);\n'
        '    s.grow()->grow();\n'
        '    std::cout << s.area() << "\\n";   // 256\n'
        '    return 0;\n'
        '}',
    ],
    9: [
        '#include <iostream>\n\n'
        'class Resource {\n'
        'public:\n'
        '    Resource() { std::cout << "acquire\\n"; }\n'
        '    ~Resource() { std::cout << "release\\n"; }   // destructor\n'
        '};\n\n'
        'int main() {\n'
        '    Resource r;   // RAII: constructor acquires, destructor releases\n'
        '    std::cout << "in scope\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <string>\n\n'
        'class Person {\n'
        'public:\n'
        '    Person(std::string name, int age) : name_(name), age_(age) {}\n'
        '    std::string name() const { return name_; }\n'
        '    int age() const { return age_; }\n'
        'private:\n'
        '    std::string name_;\n'
        '    int age_;\n'
        '};\n\n'
        'int main() {\n'
        '    Person alice("Alice", 30);\n'
        '    Person copy = alice;          // copy constructor\n'
        '    std::cout << copy.name() << " " << copy.age() << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n\n'
        'class Container {\n'
        'public:\n'
        '    Container(std::vector<int> data) : data_(std::move(data)) {}\n'
        '    // move constructor (C++11): steal resources, no copy\n'
        '    Container(Container &&other) noexcept : data_(std::move(other.data_)) {}\n'
        '    int size() const { return data_.size(); }\n'
        'private:\n'
        '    std::vector<int> data_;\n'
        '};\n\n'
        'int main() {\n'
        '    Container a({1, 2, 3});\n'
        '    Container b = std::move(a);   // move\n'
        '    std::cout << b.size() << "\\n";   // 3\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <algorithm>\n\n'
        '// rule of three: destructor, copy ctor, copy assignment\n'
        'class Buffer {\n'
        'public:\n'
        '    Buffer(int size) : size_(size), data_(new int[size]) {}\n'
        '    ~Buffer() { delete[] data_; }\n'
        '    Buffer(const Buffer &other) : size_(other.size_), data_(new int[other.size_]) {\n'
        '        std::copy(other.data_, other.data_ + size_, data_);\n'
        '    }\n'
        '    int *data() { return data_; }\n'
        'private:\n'
        '    int size_;\n'
        '    int *data_;\n'
        '};\n\n'
        'int main() {\n'
        '    Buffer a(4);\n'
        '    Buffer b = a;   // deep copy, no double-free\n'
        '    std::cout << (b.data() != a.data()) << "\\n";   // 1 (distinct buffers)\n'
        '    return 0;\n'
        '}',
    ],
    10: [
        '#include <iostream>\n\n'
        'class Complex {\n'
        'public:\n'
        '    Complex(double re, double im) : re_(re), im_(im) {}\n'
        '    Complex operator+(const Complex &o) const {\n'
        '        return Complex(re_ + o.re_, im_ + o.im_);\n'
        '    }\n'
        '    void print() const { std::cout << re_ << "+" << im_ << "i\\n"; }\n'
        'private:\n'
        '    double re_, im_;\n'
        '};\n\n'
        'int main() {\n'
        '    Complex a(1, 2), b(3, 4);\n'
        '    (a + b).print();   // 4+6i (operator overload)\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'class Fraction {\n'
        'public:\n'
        '    Fraction(int n, int d) : n_(n), d_(d) {}\n'
        '    bool operator<(const Fraction &o) const { return n_ * o.d_ < o.n_ * d_; }\n'
        '    int num() const { return n_; }\n'
        'private:\n'
        '    int n_, d_;\n'
        '};\n\n'
        'int main() {\n'
        '    Fraction a(1, 3), b(1, 2);\n'
        '    std::cout << (a < b) << "\\n";   // 1 (1/3 < 1/2)\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'class Counter {\n'
        'public:\n'
        '    Counter &operator++() { value_++; return *this; }     // prefix\n'
        '    Counter operator++(int) { Counter t = *this; ++value_; return t; }  // postfix\n'
        '    int value() const { return value_; }\n'
        'private:\n'
        '    int value_ = 0;\n'
        '};\n\n'
        'int main() {\n'
        '    Counter c;\n'
        '    c++;\n'
        '    ++c;\n'
        '    std::cout << c.value() << "\\n";   // 2\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n'
        '#include <algorithm>\n'
        '#include <string>\n\n'
        'class Book {\n'
        'public:\n'
        '    Book(std::string t, int p) : title_(t), pages_(p) {}\n'
        '    bool operator<(const Book &o) const { return pages_ < o.pages_; }\n'
        '    std::string title() const { return title_; }\n'
        'private:\n'
        '    std::string title_;\n'
        '    int pages_;\n'
        '};\n\n'
        'int main() {\n'
        '    std::vector<Book> books = {{"A", 100}, {"B", 50}, {"C", 200}};\n'
        '    std::sort(books.begin(), books.end());   // uses operator<\n'
        '    std::cout << books[0].title() << "\\n";   // B\n'
        '    return 0;\n'
        '}',
    ],
    11: [
        '#include <iostream>\n\n'
        'class Animal {\n'
        'public:\n'
        '    virtual std::string speak() const { return "..."; }\n'
        '    virtual ~Animal() = default;\n'
        '};\n\n'
        'class Dog : public Animal {\n'
        'public:\n'
        '    std::string speak() const override { return "Woof"; }\n'
        '};\n\n'
        'int main() {\n'
        '    Animal *a = new Dog();\n'
        '    std::cout << a->speak() << "\\n";   // Woof (virtual dispatch)\n'
        '    delete a;\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <memory>\n\n'
        'class Animal {\n'
        'public:\n'
        '    virtual std::string speak() const = 0;   // pure virtual\n'
        '    virtual ~Animal() = default;\n'
        '};\n\n'
        'class Cat : public Animal {\n'
        'public:\n'
        '    std::string speak() const override { return "Meow"; }\n'
        '};\n\n'
        'int main() {\n'
        '    std::unique_ptr<Animal> a = std::make_unique<Cat>();\n'
        '    std::cout << a->speak() << "\\n";   // Meow\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'class Base {\n'
        'public:\n'
        '    Base(int x) : x_(x) {}\n'
        '    void show() const { std::cout << "Base " << x_ << "\\n"; }\n'
        'protected:\n'
        '    int x_;\n'
        '};\n\n'
        'class Derived : public Base {\n'
        'public:\n'
        '    Derived(int x, int y) : Base(x), y_(y) {}   // base ctor\n'
        '    void show() const { Base::show(); std::cout << "Derived " << y_ << "\\n"; }\n'
        'private:\n'
        '    int y_;\n'
        '};\n\n'
        'int main() {\n'
        '    Derived d(1, 2);\n'
        '    d.show();\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'class Shape {                       // abstract base\n'
        'public:\n'
        '    virtual double area() const = 0;\n'
        '    virtual ~Shape() = default;\n'
        '};\n\n'
        'class Circle : public Shape {\n'
        'public:\n'
        '    Circle(double r) : r_(r) {}\n'
        '    double area() const override { return 3.14159 * r_ * r_; }\n'
        'private:\n'
        '    double r_;\n'
        '};\n\n'
        'class Square : public Shape {\n'
        'public:\n'
        '    Square(double s) : s_(s) {}\n'
        '    double area() const override { return s_ * s_; }\n'
        'private:\n'
        '    double s_;\n'
        '};\n\n'
        'int main() {\n'
        '    Circle c(2);\n'
        '    Square sq(3);\n'
        '    std::cout << c.area() << " " << sq.area() << "\\n";\n'
        '    return 0;\n'
        '}',
    ],
    12: [
        '#include <iostream>\n\n'
        'class Shape {   // abstract with pure virtual\n'
        'public:\n'
        '    virtual double area() const = 0;\n'
        '    virtual ~Shape() = default;\n'
        '};\n\n'
        'int main() {\n'
        '    // Shape s;  // error: cannot instantiate abstract class\n'
        '    std::cout << "abstract classes cannot be instantiated\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        '// interfaces in C++ = abstract classes with only pure virtuals\n'
        'class Drawable {\n'
        'public:\n'
        '    virtual void draw() const = 0;\n'
        '    virtual ~Drawable() = default;\n'
        '};\n\n'
        'class Circle : public Drawable {\n'
        'public:\n'
        '    void draw() const override { std::cout << "draw circle\\n"; }\n'
        '};\n\n'
        'int main() {\n'
        '    Circle c;\n'
        '    Drawable &d = c;\n'
        '    d.draw();\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        '// multiple inheritance\n'
        'struct Printable { virtual void print() const = 0; };\n'
        'struct Serializable { virtual void save() const = 0; };\n\n'
        'class Doc : public Printable, public Serializable {\n'
        'public:\n'
        '    void print() const override { std::cout << "print doc\\n"; }\n'
        '    void save() const override { std::cout << "save doc\\n"; }\n'
        '};\n\n'
        'int main() {\n'
        '    Doc d;\n'
        '    d.print();\n'
        '    d.save();\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <memory>\n'
        '#include <vector>\n\n'
        'struct Animal { virtual std::string speak() const = 0; virtual ~Animal() = default; };\n'
        'struct Dog : Animal { std::string speak() const override { return "Woof"; } };\n'
        'struct Cat : Animal { std::string speak() const override { return "Meow"; } };\n\n'
        'int main() {\n'
        '    std::vector<std::unique_ptr<Animal>> animals;\n'
        '    animals.push_back(std::make_unique<Dog>());\n'
        '    animals.push_back(std::make_unique<Cat>());\n'
        '    for (auto &a : animals) std::cout << a->speak() << " ";\n'
        '    std::cout << "\\n";   // Woof Meow\n'
        '    return 0;\n'
        '}',
    ],
    13: [
        '#include <iostream>\n\n'
        'template <typename T>\n'
        'T max_of(T a, T b) { return a > b ? a : b; }\n\n'
        'int main() {\n'
        '    std::cout << max_of(3, 7) << " " << max_of(2.5, 1.5) << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        'template <typename T>\n'
        'class Box {\n'
        'public:\n'
        '    Box(T value) : value_(value) {}\n'
        '    T get() const { return value_; }\n'
        'private:\n'
        '    T value_;\n'
        '};\n\n'
        'int main() {\n'
        '    Box<int> ib(42);\n'
        '    Box<std::string> sb("hello");\n'
        '    std::cout << ib.get() << " " << sb.get() << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <concepts>\n\n'
        '// C++20 concepts: constrained templates\n'
        'template <typename T>\n'
        'requires std::integral<T>\n'
        'T square(T x) { return x * x; }\n\n'
        'int main() {\n'
        '    std::cout << square(5) << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n\n'
        '// variadic templates (C++11)\n'
        'template <typename T>\n'
        'T sum(T v) { return v; }\n\n'
        'template <typename T, typename... Rest>\n'
        'T sum(T first, Rest... rest) { return first + sum(rest...); }\n\n'
        'int main() {\n'
        '    std::cout << sum(1, 2, 3, 4) << "\\n";   // 10\n'
        '    return 0;\n'
        '}',
    ],
    14: [
        '#include <iostream>\n'
        '#include <vector>\n'
        '#include <map>\n'
        '#include <unordered_map>\n'
        '#include <set>\n'
        '#include <string>\n\n'
        'int main() {\n'
        '    std::vector<int> v = {3, 1, 2};          // dynamic array\n'
        '    std::map<std::string, int> ages = {{"A", 30}};   // ordered tree map\n'
        '    std::unordered_map<std::string, int> h = {{"A", 30}};  // hash map\n'
        '    std::set<int> s = {3, 1, 2, 1};          // unique sorted\n'
        '    std::cout << v[0] << " " << ages["A"] << " " << h["A"] << " " << s.size() << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <map>\n'
        '#include <string>\n\n'
        'int main() {\n'
        '    std::map<std::string, int> freq;\n'
        '    freq["apple"]++;\n'
        '    freq["apple"]++;\n'
        '    freq["banana"]++;\n'
        '    for (const auto &[k, v] : freq)   // structured bindings (C++17)\n'
        '        std::cout << k << "=" << v << " ";\n'
        '    std::cout << "\\n";   // apple=2 banana=1\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <deque>\n'
        '#include <queue>\n'
        '#include <stack>\n\n'
        'int main() {\n'
        '    std::deque<int> d = {1, 2};\n'
        '    d.push_front(0);\n'
        '    std::queue<int> q;   // FIFO\n'
        '    q.push(1); q.push(2);\n'
        '    std::stack<int> st;  // LIFO\n'
        '    st.push(1); st.push(2);\n'
        '    std::cout << d[0] << " " << q.front() << " " << st.top() << "\\n";  // 0 1 2\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n\n'
        'int main() {\n'
        '    // emplace_back constructs in place (no copy)\n'
        '    std::vector<std::pair<int, int>> v;\n'
        '    v.emplace_back(1, 2);\n'
        '    v.emplace_back(3, 4);\n'
        '    std::cout << v.size() << " " << v[1].second << "\\n";   // 2 4\n'
        '    return 0;\n'
        '}',
    ],
    15: [
        '#include <iostream>\n'
        '#include <vector>\n'
        '#include <algorithm>\n\n'
        'int main() {\n'
        '    std::vector<int> v = {5, 2, 8, 1};\n'
        '    std::sort(v.begin(), v.end());\n'
        '    std::reverse(v.begin(), v.end());\n'
        '    for (int x : v) std::cout << x << " ";\n'
        '    std::cout << "\\n";   // 8 5 2 1\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n'
        '#include <algorithm>\n\n'
        'int main() {\n'
        '    std::vector<int> v = {1, 2, 3, 4, 5};\n'
        '    auto it = std::find(v.begin(), v.end(), 4);\n'
        '    std::cout << (it != v.end()) << " " << *it << "\\n";   // 1 4\n'
        '    int count = std::count_if(v.begin(), v.end(), [](int x) { return x > 2; });\n'
        '    std::cout << count << "\\n";   // 3\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n'
        '#include <numeric>\n\n'
        'int main() {\n'
        '    std::vector<int> v = {1, 2, 3, 4};\n'
        '    int total = std::accumulate(v.begin(), v.end(), 0);\n'
        '    int product = std::accumulate(v.begin(), v.end(), 1, [](int a, int b) { return a * b; });\n'
        '    std::cout << total << " " << product << "\\n";   // 10 24\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n'
        '#include <algorithm>\n\n'
        'int main() {\n'
        '    std::vector<int> v = {1, 2, 3, 4, 5};\n'
        '    auto it = std::lower_bound(v.begin(), v.end(), 3);   // first >= 3\n'
        '    std::cout << *it << "\\n";   // 3\n'
        '    std::cout << std::binary_search(v.begin(), v.end(), 4) << "\\n";   // 1\n'
        '    return 0;\n'
        '}',
    ],
    16: [
        '#include <iostream>\n'
        '#include <memory>\n\n'
        'int main() {\n'
        '    std::unique_ptr<int> p = std::make_unique<int>(42);   // exclusive ownership\n'
        '    std::cout << *p << "\\n";   // 42\n'
        '    // auto q = p;   // error: cannot copy unique_ptr\n'
        '    std::unique_ptr<int> q = std::move(p);   // transfer ownership\n'
        '    std::cout << *q << "\\n";   // 42\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <memory>\n\n'
        'int main() {\n'
        '    std::shared_ptr<int> a = std::make_shared<int>(10);\n'
        '    std::shared_ptr<int> b = a;   // shared ownership\n'
        '    std::cout << a.use_count() << "\\n";   // 2\n'
        '    b.reset();\n'
        '    std::cout << a.use_count() << "\\n";   // 1\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <memory>\n\n'
        '// weak_ptr: observe without owning (breaks cycles)\n'
        'int main() {\n'
        '    std::shared_ptr<int> s = std::make_shared<int>(7);\n'
        '    std::weak_ptr<int> w = s;\n'
        '    std::cout << w.expired() << "\\n";   // 0 (still alive)\n'
        '    if (auto sp = w.lock()) std::cout << *sp << "\\n";   // 7\n'
        '    s.reset();\n'
        '    std::cout << w.expired() << "\\n";   // 1 (gone)\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <memory>\n'
        '#include <vector>\n\n'
        'int main() {\n'
        '    std::vector<std::shared_ptr<int>> items;\n'
        '    for (int i = 0; i < 3; i++)\n'
        '        items.push_back(std::make_shared<int>(i * 10));\n'
        '    for (auto &p : items) std::cout << *p << " ";\n'
        '    std::cout << "\\n";   // 0 10 20\n'
        '    return 0;\n'
        '}',
    ],
    17: [
        '#include <iostream>\n'
        '#include <stdexcept>\n\n'
        'int main() {\n'
        '    try {\n'
        '        throw std::runtime_error("something failed");\n'
        '    } catch (const std::runtime_error &e) {\n'
        '        std::cout << "caught: " << e.what() << "\\n";\n'
        '    }\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <stdexcept>\n\n'
        'int divide(int a, int b) {\n'
        '    if (b == 0) throw std::invalid_argument("division by zero");\n'
        '    return a / b;\n'
        '}\n\n'
        'int main() {\n'
        '    try {\n'
        '        divide(10, 0);\n'
        '    } catch (const std::invalid_argument &e) {\n'
        '        std::cout << e.what() << "\\n";\n'
        '    }\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <fstream>\n'
        '#include <string>\n\n'
        '// RAII + exceptions: file closes automatically\n'
        'void write_file(const std::string &path) {\n'
        '    std::ofstream out(path);\n'
        '    if (!out) throw std::runtime_error("cannot open " + path);\n'
        '    out << "hello\\n";\n'
        '}   // out destructor runs here, file closed\n\n'
        'int main() {\n'
        '    try { write_file("/tmp/out.txt"); }\n'
        '    catch (const std::exception &e) { std::cout << e.what() << "\\n"; }\n'
        '    std::cout << "done\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <stdexcept>\n\n'
        '// custom exception types\n'
        'class ValidationError : public std::runtime_error {\n'
        'public:\n'
        '    explicit ValidationError(const std::string &field)\n'
        '        : std::runtime_error("invalid field: " + field) {}\n'
        '};\n\n'
        'int main() {\n'
        '    try { throw ValidationError("email"); }\n'
        '    catch (const ValidationError &e) { std::cout << e.what() << "\\n"; }\n'
        '    return 0;\n'
        '}',
    ],
    18: [
        '#include <iostream>\n'
        '#include <utility>\n'
        '#include <string>\n\n'
        'int main() {\n'
        '    std::string a = "hello";\n'
        '    std::string b = std::move(a);   // steal buffer\n'
        '    std::cout << b << "\\n";        // hello\n'
        '    std::cout << a.size() << "\\n"; // 0 (moved-from: valid but empty)\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <string>\n\n'
        '// rvalue references &&: bind only to temporaries\n'
        'void take(std::string &&s) {\n'
        '    std::cout << "got: " << s << "\\n";\n'
        '}\n\n'
        'int main() {\n'
        '    take(std::string("temp"));   // binds to rvalue\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <utility>\n'
        '#include <vector>\n\n'
        '// perfect forwarding with std::forward (C++11)\n'
        'template <typename T, typename... Args>\n'
        'T *make(Args &&... args) {\n'
        '    return new T(std::forward<Args>(args)...);\n'
        '}\n\n'
        'int main() {\n'
        '    auto p = make<std::vector<int>>(5, 42);   // 5 copies of 42\n'
        '    std::cout << p->size() << " " << (*p)[0] << "\\n";   // 5 42\n'
        '    delete p;\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n\n'
        'class Big {\n'
        'public:\n'
        '    Big() { std::cout << "default\\n"; }\n'
        '    Big(const Big &) { std::cout << "copy\\n"; }\n'
        '    Big(Big &&) noexcept { std::cout << "move\\n"; }\n'
        '};\n\n'
        'int main() {\n'
        '    std::vector<Big> v;\n'
        '    v.reserve(2);\n'
        '    v.push_back(Big{});   // move, not copy\n'
        '    return 0;\n'
        '}',
    ],
    19: [
        '#include <iostream>\n'
        '#include <algorithm>\n'
        '#include <vector>\n\n'
        'int main() {\n'
        '    std::vector<int> v = {1, 2, 3, 4};\n'
        '    auto square = [](int x) { return x * x; };   // lambda\n'
        '    std::transform(v.begin(), v.end(), v.begin(), square);\n'
        '    std::cout << v[2] << "\\n";   // 9\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <vector>\n'
        '#include <algorithm>\n\n'
        'int main() {\n'
        '    int limit = 3;\n'
        '    std::vector<int> v = {1, 2, 3, 4, 5};\n'
        '    // capture by value [limit]\n'
        '    auto count = std::count_if(v.begin(), v.end(), [limit](int x) { return x > limit; });\n'
        '    std::cout << count << "\\n";   // 2 (4, 5)\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <functional>\n'
        '#include <algorithm>\n'
        '#include <vector>\n\n'
        'int main() {\n'
        '    std::function<int(int)> fib = [&](int n) {   // recursive lambda via std::function\n'
        '        return n <= 1 ? n : fib(n - 1) + fib(n - 2);\n'
        '    };\n'
        '    std::cout << fib(10) << "\\n";   // 55\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <algorithm>\n'
        '#include <vector>\n\n'
        'int main() {\n'
        '    std::vector<int> v = {1, 2, 3, 4, 5};\n'
        '    auto even = [](int x) { return x % 2 == 0; };\n'
        '    v.erase(std::remove_if(v.begin(), v.end(), even), v.end());\n'
        '    for (int x : v) std::cout << x << " ";\n'
        '    std::cout << "\\n";   // 1 3 5\n'
        '    return 0;\n'
        '}',
    ],
    20: [
        '#include <iostream>\n'
        '#include <thread>\n\n'
        'void hello() { std::cout << "thread says hi\\n"; }\n\n'
        'int main() {\n'
        '    std::thread t(hello);\n'
        '    t.join();   // wait for the thread\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <thread>\n'
        '#include <mutex>\n\n'
        'int main() {\n'
        '    std::mutex m;\n'
        '    int counter = 0;\n'
        '    auto worker = [&] {\n'
        '        for (int i = 0; i < 1000; i++) {\n'
        '            std::lock_guard<std::mutex> lock(m);   // RAII lock\n'
        '            counter++;\n'
        '        }\n'
        '    };\n'
        '    std::thread t1(worker), t2(worker);\n'
        '    t1.join(); t2.join();\n'
        '    std::cout << counter << "\\n";   // 2000\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <future>\n\n'
        'int main() {\n'
        '    auto fut = std::async(std::launch::async, [] {\n'
        '        return 42;\n'
        '    });\n'
        '    std::cout << fut.get() << "\\n";   // 42 (blocks until ready)\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <condition_variable>\n'
        '#include <mutex>\n'
        '#include <queue>\n\n'
        'int main() {\n'
        '    std::queue<int> q;\n'
        '    std::mutex m;\n'
        '    std::condition_variable cv;\n'
        '    bool done = false;\n'
        '    auto producer = [&] {\n'
        '        { std::lock_guard<std::mutex> l(m); q.push(1); }\n'
        '        cv.notify_one();\n'
        '        { std::lock_guard<std::mutex> l(m); done = true; }\n'
        '        cv.notify_one();\n'
        '    };\n'
        '    std::thread p(producer);\n'
        '    std::unique_lock<std::mutex> lk(m);\n'
        '    cv.wait(lk, [&] { return done; });\n'
        '    std::cout << q.size() << "\\n";   // 1\n'
        '    p.join();\n'
        '    return 0;\n'
        '}',
    ],
    21: [
        '#include <iostream>\n\n'
        '// constexpr: evaluated at compile time\n'
        'constexpr int square(int x) { return x * x; }\n\n'
        'int main() {\n'
        '    constexpr int val = square(5);   // computed at compile time\n'
        '    std::cout << val << "\\n";   // 25\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <string>\n\n'
        'int main() {\n'
        '    std::string s = "hello";\n'
        '    auto [first, last] = std::pair<int, std::string>{1, "one"};  // structured binding\n'
        '    std::cout << first << " " << last << "\\n";   // 1 one\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <variant>\n'
        '#include <string>\n\n'
        'int main() {\n'
        '    // C++17 std::variant: type-safe union\n'
        '    std::variant<int, std::string> v = 42;\n'
        '    std::cout << std::get<int>(v) << "\\n";\n'
        '    v = "now a string";\n'
        '    std::cout << std::get<std::string>(v) << "\\n";\n'
        '    return 0;\n'
        '}',
        '#include <iostream>\n'
        '#include <optional>\n'
        '#include <string>\n\n'
        'int main() {\n'
        '    // C++17 std::optional: value or nothing\n'
        '    std::optional<std::string> maybe = "present";\n'
        '    if (maybe) std::cout << *maybe << "\\n";\n'
        '    std::cout << maybe.value_or("fallback") << "\\n";\n'
        '    std::optional<int> none;\n'
        '    std::cout << none.value_or(-1) << "\\n";   // -1\n'
        '    return 0;\n'
        '}',
    ],
}

LESSONS = [
    dict(slug='cpp-01-getting-started', title='Getting Started with C++',
         desc='Set up a C++ toolchain with g++, compile/run, namespaces, and I/O streams.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Install g++ and compile your first C++ program',
               'Use main with argc/argv',
               'Use namespaces to organize code',
               'Read and write with iostream'],
         refs=[dict(title='learncpp — Introduction', url='https://www.learncpp.com/'),
               dict(title='cppreference — Tutorial', url='https://en.cppreference.com/w/cpp/language'),
               dict(title='cppreference — iostream', url='https://en.cppreference.com/w/cpp/header/iostream')]),
    dict(slug='cpp-02-variables-types', title='Variables and Fundamental Types',
         desc='Fundamental types, const/constexpr, auto deduction, fixed-width integers.',
         dur='60 min', diff='beginner', prereq=['CPP-01'],
         objs=['Use fundamental numeric and boolean types',
               'Use const and constexpr',
               'Deduce types with auto',
               'Use fixed-width integers'],
         refs=[dict(title='learncpp — Fundamental Data Types', url='https://www.learncpp.com/cpp-tutorial/fundamental-data-types/'),
               dict(title='cppreference — Fundamental Types', url='https://en.cppreference.com/w/cpp/language/types'),
               dict(title='cppreference — constexpr', url='https://en.cppreference.com/w/cpp/language/constexpr')]),
    dict(slug='cpp-03-operators', title='Operators and Expressions',
         desc='Arithmetic, comparison, logical, bitwise operators, precedence.',
         dur='60 min', diff='beginner', prereq=['CPP-02'],
         objs=['Use arithmetic and comparison operators',
               'Understand short-circuit logical operators',
               'Use bitwise operators',
               'Master assignment and increment operators'],
         refs=[dict(title='learncpp — Operators', url='https://www.learncpp.com/cpp-tutorial/introduction-to-operators/'),
               dict(title='cppreference — Operator Precedence', url='https://en.cppreference.com/w/cpp/language/operator_precedence'),
               dict(title='cppreference — Arithmetic Operators', url='https://en.cppreference.com/w/cpp/language/operator_arithmetic')]),
    dict(slug='cpp-04-control-flow', title='Control Flow',
         desc='if/else, switch, loops, range-based for, and jump statements.',
         dur='60 min', diff='beginner', prereq=['CPP-03'],
         objs=['Write if/else branching logic',
               'Use switch statements',
               'Use for, while, and do-while loops',
               'Iterate containers with range-based for'],
         refs=[dict(title='learncpp — If Statements', url='https://www.learncpp.com/cpp-tutorial/if-statements/'),
               dict(title='learncpp — For Loops', url='https://www.learncpp.com/cpp-tutorial/for-statements/'),
               dict(title='cppreference — Range-based for', url='https://en.cppreference.com/w/cpp/language/range-for')]),
    dict(slug='cpp-05-functions', title='Functions and Overloading',
         desc='Declarations vs definitions, overloading, default arguments, const references.',
         dur='60 min', diff='beginner', prereq=['CPP-04'],
         objs=['Declare and define functions',
               'Overload functions by signature',
               'Use default arguments',
               'Pass by const reference'],
         refs=[dict(title='learncpp — Functions', url='https://www.learncpp.com/cpp-tutorial/introduction-to-functions/'),
               dict(title='learncpp — Function Overloading', url='https://www.learncpp.com/cpp-tutorial/introduction-to-function-overloading/'),
               dict(title='cppreference — Functions', url='https://en.cppreference.com/w/cpp/language/functions')]),
    dict(slug='cpp-06-containers', title='Arrays, Strings, and Vectors',
         desc='C arrays, std::string, std::vector, and multi-dimensional arrays.',
         dur='60 min', diff='beginner', prereq=['CPP-05'],
         objs=['Use std::vector with push_back',
               'Manipulate std::string',
               'Use C-style arrays and range-based for',
               'Work with multi-dimensional arrays'],
         refs=[dict(title='learncpp — Vectors', url='https://www.learncpp.com/cpp-tutorial/introduction-to-stdvector-and-list-constructors/'),
               dict(title='cppreference — std::vector', url='https://en.cppreference.com/w/cpp/container/vector'),
               dict(title='cppreference — std::string', url='https://en.cppreference.com/w/cpp/string/basic_string')]),
    dict(slug='cpp-07-pointers-references', title='Pointers and References',
         desc='Pointer vs reference semantics, pointer arithmetic, nullptr.',
         dur='75 min', diff='intermediate', prereq=['CPP-06'],
         objs=['Dereference pointers and use references',
               'Pass by reference',
               'Do pointer arithmetic',
               'Use nullptr and pointer-to-pointer'],
         refs=[dict(title='learncpp — References', url='https://www.learncpp.com/cpp-tutorial/introduction-to-references/'),
               dict(title='learncpp — Pointers', url='https://www.learncpp.com/cpp-tutorial/introduction-to-pointers/'),
               dict(title='cppreference — Pointers', url='https://en.cppreference.com/w/cpp/language/pointer')]),
    dict(slug='cpp-08-classes-objects', title='Classes and Objects',
         desc='Class definitions, access specifiers, constructors, static members, this.',
         dur='75 min', diff='beginner', prereq=['CPP-07'],
         objs=['Define classes with private data and public methods',
               'Write constructors with initializer lists',
               'Use static members',
               'Write const methods and use this'],
         refs=[dict(title='learncpp — Classes', url='https://www.learncpp.com/cpp-tutorial/introduction-to-classes/'),
               dict(title='learncpp — Constructors', url='https://www.learncpp.com/cpp-tutorial/constructors/'),
               dict(title='cppreference — Classes', url='https://en.cppreference.com/w/cpp/language/classes')]),
    dict(slug='cpp-09-copy-move', title='Constructors, Destructors, and Copy Semantics',
         desc='RAII, copy constructors, move semantics, rule of three.',
         dur='75 min', diff='intermediate', prereq=['CPP-08'],
         objs=['Write constructors and destructors (RAII)',
               'Write copy constructors',
               'Write move constructors',
               'Apply the rule of three'],
         refs=[dict(title='learncpp — Destructors', url='https://www.learncpp.com/cpp-tutorial/destructors/'),
               dict(title='learncpp — Move Semantics', url='https://www.learncpp.com/cpp-tutorial/move-semantics-and-stdmove/'),
               dict(title='cppreference — Rule of three/five/zero', url='https://en.cppreference.com/w/cpp/language/rule_of_three')]),
    dict(slug='cpp-10-operator-overloading', title='Operator Overloading',
         desc='Overload operators, comparison operators, increment/decrement.',
         dur='60 min', diff='intermediate', prereq=['CPP-09'],
         objs=['Overload arithmetic operators',
               'Overload comparison operators',
               'Overload prefix and postfix increment',
               'Use overloaded operators with STL algorithms'],
         refs=[dict(title='learncpp — Operator Overloading', url='https://www.learncpp.com/cpp-tutorial/introduction-to-operator-overloading/'),
               dict(title='cppreference — Operator Overloading', url='https://en.cppreference.com/w/cpp/language/operators'),
               dict(title='cppreference — Comparison Operators', url='https://en.cppreference.com/w/cpp/language/operator_comparison')]),
    dict(slug='cpp-11-inheritance', title='Inheritance and Polymorphism',
         desc='Base/derived classes, virtual functions, abstract classes.',
         dur='75 min', diff='intermediate', prereq=['CPP-10'],
         objs=['Create derived classes',
               'Use virtual functions for polymorphism',
               'Use pure virtual functions (abstract classes)',
               'Compose with base class references'],
         refs=[dict(title='learncpp — Inheritance', url='https://www.learncpp.com/cpp-tutorial/introduction-to-inheritance/'),
               dict(title='learncpp — Virtual Functions', url='https://www.learncpp.com/cpp-tutorial/virtual-functions/'),
               dict(title='cppreference — Virtual Functions', url='https://en.cppreference.com/w/cpp/language/virtual')]),
    dict(slug='cpp-12-interfaces', title='Interfaces and Abstract Classes',
         desc='Abstract classes as interfaces, multiple inheritance, polymorphic collections.',
         dur='60 min', diff='intermediate', prereq=['CPP-11'],
         objs=['Design abstract base classes',
               'Implement interfaces with pure virtual methods',
               'Use multiple inheritance',
               'Store polymorphic objects with unique_ptr'],
         refs=[dict(title='learncpp — Pure Virtual Functions', url='https://www.learncpp.com/cpp-tutorial/pure-virtual-functions-abstract-base-classes-and-interface-classes/'),
               dict(title='cppreference — Abstract Classes', url='https://en.cppreference.com/w/cpp/language/abstract_class'),
               dict(title='cppreference — Multiple Inheritance', url='https://en.cppreference.com/w/cpp/language/multiple_inheritance')]),
    dict(slug='cpp-13-templates', title='Templates',
         desc='Function templates, class templates, concepts, variadic templates.',
         dur='75 min', diff='advanced', prereq=['CPP-12'],
         objs=['Write function templates',
               'Write class templates',
               'Constrain templates with concepts (C++20)',
               'Write variadic templates'],
         refs=[dict(title='learncpp — Templates', url='https://www.learncpp.com/cpp-tutorial/function-templates/'),
               dict(title='cppreference — Templates', url='https://en.cppreference.com/w/cpp/language/templates'),
               dict(title='cppreference — Concepts', url='https://en.cppreference.com/w/cpp/language/constraints')]),
    dict(slug='cpp-14-stl-containers', title='STL Containers',
         desc='vector, map, unordered_map, set, deque, queue, stack.',
         dur='75 min', diff='intermediate', prereq=['CPP-13'],
         objs=['Use vector and map',
               'Use unordered_map and set',
               'Use queue and stack adaptors',
               'Emplace elements efficiently'],
         refs=[dict(title='cppreference — Containers', url='https://en.cppreference.com/w/cpp/container'),
               dict(title='cppreference — std::map', url='https://en.cppreference.com/w/cpp/container/map'),
               dict(title='learncpp — STL Containers', url='https://www.learncpp.com/cpp-tutorial/introduction-to-stl-containers/')]),
    dict(slug='cpp-15-stl-algorithms', title='STL Algorithms and Iterators',
         desc='sort, reverse, find, count_if, accumulate, lower_bound, binary_search.',
         dur='75 min', diff='intermediate', prereq=['CPP-14'],
         objs=['Sort and reverse containers',
               'Search with find and binary_search',
               'Accumulate with std::accumulate',
               'Use lower_bound for sorted ranges'],
         refs=[dict(title='cppreference — Algorithms', url='https://en.cppreference.com/w/cpp/algorithm'),
               dict(title='cppreference — std::sort', url='https://en.cppreference.com/w/cpp/algorithm/sort'),
               dict(title='learncpp — Algorithms', url='https://www.learncpp.com/cpp-tutorial/introduction-to-standard-library-algorithms/')]),
    dict(slug='cpp-16-smart-pointers', title='Smart Pointers',
         desc='unique_ptr, shared_ptr, weak_ptr, ownership semantics.',
         dur='60 min', diff='advanced', prereq=['CPP-15'],
         objs=['Use unique_ptr for exclusive ownership',
               'Use shared_ptr for shared ownership',
               'Use weak_ptr to break cycles',
               'Store polymorphic objects safely'],
         refs=[dict(title='learncpp — Smart Pointers', url='https://www.learncpp.com/cpp-tutorial/introduction-to-smart-pointers-and-move-semantics/'),
               dict(title='cppreference — unique_ptr', url='https://en.cppreference.com/w/cpp/memory/unique_ptr'),
               dict(title='cppreference — shared_ptr', url='https://en.cppreference.com/w/cpp/memory/shared_ptr')]),
    dict(slug='cpp-17-exceptions', title='Exception Handling and RAII',
         desc='try/catch, throwing, custom exceptions, RAII cleanup.',
         dur='60 min', diff='intermediate', prereq=['CPP-16'],
         objs=['Throw and catch exceptions',
               'Write exception-safe code',
               'Use RAII for resource cleanup',
               'Define custom exception types'],
         refs=[dict(title='learncpp — Exceptions', url='https://www.learncpp.com/cpp-tutorial/introduction-to-exceptions/'),
               dict(title='cppreference — Exceptions', url='https://en.cppreference.com/w/cpp/language/exceptions'),
               dict(title='cppreference — try/catch', url='https://en.cppreference.com/w/cpp/language/try_catch')]),
    dict(slug='cpp-18-move-semantics', title='Move Semantics and Rvalue References',
         desc='std::move, rvalue references, perfect forwarding, move constructors.',
         dur='60 min', diff='advanced', prereq=['CPP-17'],
         objs=['Move objects with std::move',
               'Bind rvalue references',
               'Forward perfectly with std::forward',
               'Write move constructors'],
         refs=[dict(title='learncpp — Move Semantics', url='https://www.learncpp.com/cpp-tutorial/move-semantics-and-stdmove/'),
               dict(title='cppreference — Rvalue References', url='https://en.cppreference.com/w/cpp/language/reference'),
               dict(title='cppreference — std::move', url='https://en.cppreference.com/w/cpp/utility/move')]),
    dict(slug='cpp-19-lambdas', title='Lambdas and Functional Programming',
         desc='Lambda expressions, captures, std::function, higher-order patterns.',
         dur='60 min', diff='intermediate', prereq=['CPP-18'],
         objs=['Write lambda expressions',
               'Capture variables by value and reference',
               'Use std::function',
               'Combine with STL algorithms'],
         refs=[dict(title='learncpp — Lambdas', url='https://www.learncpp.com/cpp-tutorial/introduction-to-lambdas-anonymous-functions/'),
               dict(title='cppreference — Lambda Expressions', url='https://en.cppreference.com/w/cpp/language/lambda'),
               dict(title='cppreference — std::function', url='https://en.cppreference.com/w/cpp/utility/functional/function')]),
    dict(slug='cpp-20-concurrency', title='Concurrency',
         desc='std::thread, mutex, lock_guard, async/future, condition_variable.',
         dur='75 min', diff='advanced', prereq=['CPP-19'],
         objs=['Create and join threads',
               'Synchronize with mutex and lock_guard',
               'Use async and future',
               'Coordinate with condition_variable'],
         refs=[dict(title='cppreference — Thread Support', url='https://en.cppreference.com/w/cpp/thread'),
               dict(title='cppreference — std::thread', url='https://en.cppreference.com/w/cpp/thread/thread'),
               dict(title='cppreference — std::async', url='https://en.cppreference.com/w/cpp/thread/async')]),
    dict(slug='cpp-21-modern', title='Modern C++: C++17/20 Features',
         desc='constexpr, structured bindings, variant, optional, modern idioms.',
         dur='75 min', diff='expert', prereq=['CPP-20'],
         objs=['Use constexpr functions',
               'Use structured bindings',
               'Use std::variant and std::optional',
               'Apply modern C++ idioms'],
         refs=[dict(title='cppreference — C++20 Features', url='https://en.cppreference.com/w/cpp/20'),
               dict(title='cppreference — C++17 Features', url='https://en.cppreference.com/w/cpp/17'),
               dict(title='cppreference — std::variant', url='https://en.cppreference.com/w/cpp/utility/variant')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'cpp', LESSONS, CODE, BASE)
