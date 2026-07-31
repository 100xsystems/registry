#!/usr/bin/env python3
"""Generate the 21-lesson Ruby curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from ruby-doc.org + docs.ruby-lang.org.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'ruby'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'ruby')

CODE = {
    1: [
        'puts "Hello, 100X Systems!"\n'
        '# run: ruby hello.rb',
        'print "no newline "\n'
        'p [1, 2, 3]      # inspect form\n'
        'pp({a: 1})       # pretty print',
        'puts "What is your name?"\n'
        'name = gets.chomp\n'
        'puts "Hello, #{name}!"\n'
        'ARGV.each { |a| puts "arg: #{a}" }',
        'p RUBY_VERSION\n'
        'p RUBY_ENGINE\n'
        'p $0            # script name\n'
        'p __FILE__\n'
        'p __LINE__',
    ],
    2: [
        'x = 42\n'
        'y = 3.14\n'
        'name = "Alice"\n'
        'flag = true\n'
        'nothing = nil\n'
        'p x.class, y.class, name.class, flag.class, nothing.class',
        '# scope types: local, instance, class, global\n'
        'class Demo\n'
        '  @iv = 1          # instance variable\n'
        '  @@cv = 2         # class variable\n'
        '  $gv = 3          # global variable\n'
        '  def show\n'
        '    lv = 4         # local variable\n'
        '    [@iv, @@cv, $gv, lv]\n'
        '  end\n'
        'end\n'
        'p Demo.new.show',
        '# dynamic typing: same variable, different types\n'
        'v = 42\n'
        'v = "hello"\n'
        'v = [1, 2, 3]\n'
        'p v',
        '# symbols are immutable, interned identifiers\n'
        ':name.object_id == :name.object_id   # => true\n'
        'p :name.class\n'
        'p "name".to_sym',
    ],
    3: [
        'a = 17\n'
        'b = 5\n'
        'p a + b, a - b, a * b, a / b, a % b   # 22 12 85 3 2\n'
        'p 17.0 / 5.0                          # 3.4 (float division)',
        'p 2 ** 10        # 1024 (power)\n'
        'p 7 / 2          # 3 (integer division)\n'
        'p 7.0 / 2        # 3.5\n'
        'p -7 / 2         # -4 (Ruby floors)',
        'p 1_000_000      # readability underscores\n'
        'p 0xFF           # 255 hex\n'
        'p 0b1010         # 10 binary\n'
        'p 3.14.round(1)  # 3.1\n'
        'p 3.7.floor, 3.2.ceil, -3.14.abs',
        '# arbitrary-precision integers\n'
        'p 2 ** 100\n'
        'p 10.class.ancestors.first(3)\n'
        'require "bigdecimal"\n'
        'p BigDecimal("0.1") + BigDecimal("0.2")',
    ],
    4: [
        'greeting = "hello"\n'
        'p greeting.upcase       # HELLO\n'
        'p greeting.capitalize   # Hello\n'
        'p greeting.reverse      # olleh\n'
        'p greeting.length       # 5\n'
        'p greeting.include?("ell")  # true',
        'name = "World"\n'
        'p "Hello, #{name}!"      # interpolation\n'
        'p \'#{name} not interpolated\'\n'
        'p format("%.2f", 3.14159)',
        's = "a,b,c"\n'
        'p s.split(",")          # ["a", "b", "c"]\n'
        'p ["x", "y"].join("-")  # "x-y"\n'
        'p "hello world".gsub("l", "L")  # heLLo worLd',
        '# mutable strings; freeze to protect\n'
        's = "abc"\n'
        's << "d"       # mutates\n'
        'p s            # abcd\n'
        'frozen = "abc".freeze\n'
        'p frozen.frozen?  # true',
    ],
    5: [
        'score = 85\n'
        'if score >= 90\n'
        '  puts "A"\n'
        'elsif score >= 80\n'
        '  puts "B"\n'
        'else\n'
        '  puts "C"\n'
        'end',
        'day = 3\n'
        'case day\n'
        'when 1 then puts "Monday"\n'
        'when 2, 3 then puts "Weekday"\n'
        'else puts "Other"\n'
        'end',
        '# unless: the inverse of if\n'
        'logged_in = false\n'
        'puts "please log in" unless logged_in\n'
        'puts "welcome" if logged_in\n'
        'puts "error" unless 2 > 1',
        '3.times { |i| print i }       # 012\n'
        'puts\n'
        '1.upto(3) { |i| print i }     # 123\n'
        'puts\n'
        '(1..3).each { |i| print i }   # 123\n'
        'puts\n'
        'i = 0\n'
        'while i < 2\n'
        '  print i\n'
        '  i += 1\n'
        'end                          # 01',
    ],
    6: [
        'arr = [1, 2, 3]\n'
        'p arr[0]          # 1\n'
        'p arr[-1]         # 3 (from end)\n'
        'p arr[0, 2]       # [1, 2] (slice)\n'
        'p arr[1..2]       # [2, 3]\n'
        'arr << 4          # append\n'
        'p arr             # [1, 2, 3, 4]',
        'arr = [5, 2, 8, 1]\n'
        'p arr.sort        # [1, 2, 5, 8]\n'
        'p arr.sort.reverse\n'
        'p arr.max, arr.min, arr.sum\n'
        'p arr.first(2), arr.last(2)',
        'arr = [1, 2, 3, 4]\n'
        'p arr.select { |x| x.even? }   # [2, 4]\n'
        'p arr.reject { |x| x.even? }   # [1, 3]\n'
        'p arr.map { |x| x * 2 }        # [2, 4, 6, 8]\n'
        'p arr.any?(&:even?)            # true',
        '# multidimensional and uniq\n'
        'grid = [[1, 2], [3, 4]]\n'
        'p grid[1][0]      # 3\n'
        'p [1, 1, 2].uniq  # [1, 2]\n'
        'p [1, 2, 3].include?(2)  # true',
    ],
    7: [
        'h = { "name" => "Alice", "age" => 30 }\n'
        'p h["name"]       # "Alice"\n'
        'h["city"] = "NYC"\n'
        'p h               # 3 keys',
        '# symbol keys + modern syntax\n'
        'h = { name: "Alice", age: 30 }\n'
        'p h[:name]\n'
        'p h.key?(:age)    # true\n'
        'p h.keys, h.values\n'
        'h.each { |k, v| puts "#{k}=#{v}" }',
        'h = { a: 1, b: 2, c: 3 }\n'
        'p h.select { |_, v| v > 1 }    # {b: 2, c: 3}\n'
        'p h.map { |k, v| "#{k}#{v}" }\n'
        'p h.transform_values { |v| v * 10 }',
        'p ({a: 1}.merge(b: 2))    # {a: 1, b: 2}\n'
        'p ({a: 1}.key?(:x))       # false\n'
        'p ({a: 1}.fetch(:x, 0))   # 0 (default)',
    ],
    8: [
        'def greet(name)\n'
        '  "Hello, #{name}!"\n'
        'end\n'
        'p greet("Alice")',
        'def sum(a, b)\n'
        '  a + b\n'
        'end\n'
        '# implicit return: last expression\n'
        'p sum(2, 3)   # 5\n'
        'p (sum 2, 3)  # 5 (parens optional)',
        '# splat and keyword args\n'
        'def log(*messages)\n'
        '  messages\n'
        'end\n'
        'def config(name:, port: 80)\n'
        '  [name, port]\n'
        'end\n'
        'p log(1, 2, 3)\n'
        'p config(name: "web")\n'
        'p config(name: "api", port: 3000)',
        '# default args + block param\n'
        'def repeat(msg, times = 2)\n'
        '  times.times { print msg }\n'
        'end\n'
        'def with_block(&blk)\n'
        '  blk.call("inside")\n'
        'end\n'
        'repeat("hi ", 3)\n'
        'puts\n'
        'with_block { |s| puts s }',
    ],
    9: [
        'class Dog\n'
        '  def speak\n'
        '    "Woof"\n'
        '  end\n'
        'end\n'
        'p Dog.new.speak',
        'class Person\n'
        '  def initialize(name)\n'
        '    @name = name\n'
        '  end\n'
        '  attr_reader :name\n'
        '  attr_writer :name\n'
        '  attr_accessor :age\n'
        'end\n'
        'p = Person.new("Alice")\n'
        'p p.name\n'
        'p.name = "Bob"\n'
        'p p.name',
        'class Counter\n'
        '  @@count = 0\n'
        '  def initialize\n'
        '    @@count += 1\n'
        '  end\n'
        '  def self.count\n'
        '    @@count\n'
        '  end\n'
        'end\n'
        'Counter.new; Counter.new\n'
        'p Counter.count   # 2',
        '# to_s and inspect\n'
        'class Point\n'
        '  def initialize(x, y)\n'
        '    @x, @y = x, y\n'
        '  end\n'
        '  def to_s\n'
        '    "(#{@x}, #{@y})"\n'
        '  end\n'
        'end\n'
        'puts Point.new(3, 4)   # (3, 4)',
    ],
    10: [
        'module Greetable\n'
        '  def greet\n'
        '    "Hello from #{self.class}"\n'
        '  end\n'
        'end\n'
        'class Person\n'
        '  include Greetable\n'
        'end\n'
        'p Person.new.greet',
        'module Logger\n'
        '  def log(msg)\n'
        '    puts "[LOG] #{msg}"\n'
        '  end\n'
        'end\n'
        'class Service\n'
        '  extend Logger   # class-level methods\n'
        'end\n'
        'Service.log("started")',
        'module M1\n'
        '  def who; "M1"; end\n'
        'end\n'
        'module M2\n'
        '  def who; "M2"; end\n'
        'end\n'
        'class Both\n'
        '  include M1\n'
        '  include M2   # later include wins\n'
        'end\n'
        'p Both.new.who',
        '# prepend vs include (prepend is consulted first)\n'
        'module Wrap\n'
        '  def greet\n'
        '    "wrapped: " + super\n'
        '  end\n'
        'end\n'
        'class Greeter\n'
        '  prepend Wrap\n'
        '  def greet; "hi"; end\n'
        'end\n'
        'p Greeter.new.greet   # wrapped: hi',
    ],
    11: [
        'class Animal\n'
        '  def speak\n'
        '    "..."\n'
        '  end\n'
        'end\n'
        'class Dog < Animal\n'
        '  def speak\n'
        '    "Woof"\n'
        '  end\n'
        'end\n'
        'p Dog.new.speak',
        'class Base\n'
        '  def initialize(x)\n'
        '    @x = x\n'
        '  end\n'
        'end\n'
        'class Derived < Base\n'
        '  def initialize(x, y)\n'
        '    super(x)     # call parent\n'
        '    @y = y\n'
        '  end\n'
        '  attr_reader :x, :y\n'
        'end\n'
        'd = Derived.new(1, 2)\n'
        'p [d.x, d.y]',
        'class Animal\n'
        '  def speak; "animal"; end\n'
        'end\n'
        'class Dog < Animal\n'
        '  def speak\n'
        '    super + " (dog)"\n'
        '  end\n'
        'end\n'
        'p Dog.new.speak   # animal (dog)',
        '# is_a? and ancestry\n'
        'class Cat < Animal; end\n'
        'c = Cat.new\n'
        'p c.is_a?(Cat)\n'
        'p c.is_a?(Animal)\n'
        'p Cat.ancestors.first(4)',
    ],
    12: [
        '# blocks: passed with do/end or braces\n'
        'def call_block\n'
        '  yield "from yield"\n'
        'end\n'
        'call_block { |m| puts m }',
        'def twice\n'
        '  yield\n'
        '  yield\n'
        'end\n'
        'twice { puts "hello" }',
        '# proc vs lambda: return semantics differ\n'
        'def test_proc\n'
        '  p = proc { return "from proc" }   # returns from METHOD\n'
        '  p.call\n'
        '  "unreachable"\n'
        'end\n'
        'def test_lambda\n'
        '  l = -> { return "from lambda" }   # returns from LAMBDA only\n'
        '  l.call\n'
        '  "after lambda"\n'
        'end\n'
        'p test_proc\n'
        'p test_lambda',
        '# &block captures a block as a proc\n'
        'def each_arg(&blk)\n'
        '  [1, 2, 3].each(&blk)\n'
        'end\n'
        'result = []\n'
        'each_arg { |x| result << x * 10 }\n'
        'p result   # [10, 20, 30]',
    ],
    13: [
        '# Enumerable: the heart of Ruby collections\n'
        'p (1..5).map { |x| x * x }       # [1, 4, 9, 16, 25]\n'
        'p (1..10).select(&:even?)        # [2, 4, 6, 8, 10]\n'
        'p (1..5).reduce(:+)               # 15',
        'words = %w[cat dog elephant]\n'
        'p words.max_by(&:length)          # elephant\n'
        'p words.sort_by(&:length)         # [cat, dog, elephant]\n'
        'p words.group_by(&:length)        # {3=>[cat, dog], 8=>[elephant]}',
        'p [1, 2, 3, 2].tally               # {1=>1, 2=>2, 3=>1}\n'
        'p (1..5).each_with_object([]) { |x, acc| acc << x * 2 }\n'
        'p [1, 2, 3].partition(&:odd?)      # [[1, 3], [2]]',
        '# enumerators are lazy chains\n'
        'e = (1..Float::INFINITY).lazy.select(&:even?).first(5)\n'
        'p e   # [2, 4, 6, 8, 10]\n'
        'p (1..5).to_enum(:each).next',
    ],
    14: [
        'begin\n'
        '  raise "custom failure"\n'
        'rescue => e\n'
        '  puts "caught: #{e.message}"\n'
        'ensure\n'
        '  puts "always runs"\n'
        'end',
        'begin\n'
        '  1 / 0\n'
        'rescue ZeroDivisionError => e\n'
        '  puts "#{e.class}: #{e.message}"\n'
        'end',
        'class ValidationError < StandardError; end\n'
        'def validate!(v)\n'
        '  raise ValidationError, "bad value" if v.nil?\n'
        'end\n'
        'begin\n'
        '  validate!(nil)\n'
        'rescue ValidationError => e\n'
        '  puts e.message\n'
        'end',
        'def risky\n'
        '  yield\n'
        'rescue ArgumentError\n'
        '  :argument\n'
        'rescue StandardError\n'
        '  :standard\n'
        'end\n'
        'p risky { raise ArgumentError }\n'
        'p risky { raise "generic" }',
    ],
    15: [
        'File.write("/tmp/notes.txt", "hello file\\n")\n'
        'p File.read("/tmp/notes.txt")',
        'File.open("/tmp/data.txt", "w") do |f|\n'
        '  f.puts "line 1"\n'
        '  f.puts "line 2"\n'
        'end\n'
        'p File.readlines("/tmp/data.txt")   # auto-closed by block',
        'File.foreach("/tmp/data.txt") { |line| puts line.upcase }\n'
        'p File.exist?("/tmp/data.txt")\n'
        'p File.size("/tmp/data.txt")',
        'require "fileutils"\n'
        'FileUtils.mkdir_p("/tmp/a/b")\n'
        'FileUtils.cp("/tmp/data.txt", "/tmp/a/b/copy.txt")\n'
        'p Dir.glob("/tmp/a/**/*").first(5)\n'
        'p Dir.children("/tmp/a")',
    ],
    16: [
        'text = "The quick brown fox"\n'
        'p text =~ /quick/            # 4 (index)\n'
        'p /quick/.match?(text)       # true\n'
        'p text =~ /xyz/              # nil',
        'm = /(\\d{2})-(\\d{2})/.match("date 12-34")\n'
        'p m[0]    # "12-34"\n'
        'p m[1]    # "12"\n'
        'p m[2]    # "34"',
        'p "hello 42 world".scan(/\\d+/)     # ["42"]\n'
        'p "a1b2".gsub(/\\d/) { |d| d.to_i * 2 }   # a2b4\n'
        'p "hello".sub("l", "L")            # heLlo',
        'p /\\Astart/ === "start here"\n'
        'p /end\\z/ === "the end"\n'
        'p /[a-z]{3}/ === "abc"\n'
        'email = "a@b.com"\n'
        'p email =~ /\\A[^@]+@[^@]+\\.[^@]+\\z/   # 0 (valid)',
    ],
    17: [
        '# metaprogramming: define methods dynamically\n'
        'class Calculator\n'
        '  %i[add sub mul].each do |op|\n'
        '    define_method(op) do |a, b|\n'
        '      a.public_send(op == :mul ? :* : (op == :add ? :+ : :-), b)\n'
        '    end\n'
        '  end\n'
        'end\n'
        'c = Calculator.new\n'
        'p c.add(2, 3)   # 5',
        'class Ghost\n'
        '  def method_missing(name, *args)\n'
        '    "#{name} called with #{args.inspect}"\n'
        '  end\n'
        '  def respond_to_missing?(name, include_private = false)\n'
        '    true\n'
        '  end\n'
        'end\n'
        'p Ghost.new.any_method(1, 2)',
        '# send: dynamic dispatch\n'
        'class Greeter\n'
        '  def hello; "hi"; end\n'
        '  def goodbye; "bye"; end\n'
        'end\n'
        'g = Greeter.new\n'
        'p g.send(:hello)\n'
        'p g.public_send(:goodbye)',
        '# instance_eval: execute in object context\n'
        'class Config\n'
        '  def initialize; @values = {}; end\n'
        'end\n'
        'c = Config.new\n'
        'c.instance_eval { @values[:timeout] = 30 }\n'
        'p c.instance_variable_get(:@values)',
    ],
    18: [
        '# gems + Bundler\n'
        '# Gemfile:\n'
        '#   source "https://rubygems.org"\n'
        '#   gem "rails"\n'
        '#   gem "json"\n'
        '#   bundle install\n'
        'p Gem::Specification.find_all_by_name("json").any?',
        'require "json"\n'
        'data = { name: "Alice", tags: [1, 2] }\n'
        'json = JSON.generate(data)\n'
        'p json\n'
        'p JSON.parse(json)',
        'require "date"\n'
        'd = Date.today\n'
        'p d.year\n'
        'p (d + 7).to_s\n'
        'require "time"\n'
        'p Time.now.strftime("%Y-%m-%d")',
        'require "net/http"\n'
        'require "uri"\n'
        'uri = URI("https://example.com")\n'
        'res = Net::HTTP.get_response(uri)\n'
        'p res.code    # "200"\n'
        'p res.body.length',
    ],
    19: [
        '# minitest\n'
        'require "minitest/autorun"\n'
        'class TestCalc < Minitest::Test\n'
        '  def test_addition\n'
        '    assert_equal 5, 2 + 3\n'
        '  end\n'
        '  def test_truthy\n'
        '    assert 1 == 1\n'
        '  end\n'
        'end',
        '# assert basics\n'
        'require "minitest/autorun"\n'
        'class TestArray < Minitest::Test\n'
        '  def test_sort\n'
        '    assert_equal [1, 2, 3], [3, 1, 2].sort\n'
        '    refute [1].empty?\n'
        '    assert_includes [1, 2], 2\n'
        '  end\n'
        'end',
        '# describe/it style\n'
        'require "minitest/autorun"\n'
        'describe "String" do\n'
        '  it "upcases" do\n'
        '    _("hi".upcase).must_equal "HI"\n'
        '  end\n'
        'end',
        '# testing with mocks\n'
        'require "minitest/autorun"\n'
        'class Service\n'
        '  def initialize(client); @client = client; end\n'
        '  def run; @client.fetch("key"); end\n'
        'end\n'
        'describe Service do\n'
        '  it "delegates" do\n'
        '    client = Minitest::Mock.new\n'
        '    client.expect(:fetch, "value", ["key"])\n'
        '    assert_equal "value", Service.new(client).run\n'
        '  end\n'
        'end',
    ],
    20: [
        '# threads: concurrent execution\n'
        'threads = 3.times.map do |i|\n'
        '  Thread.new { sleep(rand * 0.1); puts "thread #{i}" }\n'
        'end\n'
        'threads.each(&:join)\n'
        'puts "all done"',
        '# thread safety with Mutex\n'
        'require "thread"\n'
        'mutex = Mutex.new\n'
        'counter = 0\n'
        'threads = 10.times.map do\n'
        '  Thread.new do\n'
        '    100.times { mutex.synchronize { counter += 1 } }\n'
        '  end\n'
        'end\n'
        'threads.each(&:join)\n'
        'p counter   # 1000',
        '# Queue: thread-safe producer/consumer\n'
        'require "thread"\n'
        'q = Queue.new\n'
        'producer = Thread.new { 5.times { |i| q << i } }\n'
        'consumer = Thread.new { 5.times { p q.pop } }\n'
        '[producer, consumer].each(&:join)',
        '# Fiber: cooperative concurrency\n'
        'f = Fiber.new do\n'
        '  3.times do |i|\n'
        '    Fiber.yield i\n'
        '  end\n'
        '  "done"\n'
        'end\n'
        'p f.resume   # 0\n'
        'p f.resume   # 1\n'
        'p f.resume   # 2\n'
        'p f.resume   # done',
    ],
    21: [
        '# pattern matching (Ruby 2.7+/3.x)\n'
        'case { name: "Alice", age: 30 }\n'
        'in { name:, age: }\n'
        '  puts "name=#{name} age=#{age}"\n'
        'else\n'
        '  puts "no match"\n'
        'end',
        'case [1, 2, 3]\n'
        'in [first, *rest]\n'
        '  p [first, rest]   # [1, [2, 3]]\n'
        'end',
        'value = 42\n'
        'case value\n'
        'in Integer => n if n > 40\n'
        '  puts "big int #{n}"\n'
        'in String\n'
        '  puts "string"\n'
        'end',
        '# refinements: scoped monkey-patching\n'
        'module UppercaseRefinement\n'
        '  refine String do\n'
        '    def shout; upcase + "!"; end\n'
        '  end\n'
        'end\n'
        'using UppercaseRefinement\n'
        'p "hello".shout   # HELLO!',
    ],
}

LESSONS = [
    dict(slug='ruby-01-getting-started', title='Getting Started with Ruby',
         desc='Install Ruby, run scripts, I/O basics, and understand the interpreter.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Install Ruby and run your first script',
               'Use puts, print, p, and pp for output',
               'Read input with gets and handle ARGV',
               'Understand Ruby version and runtime'],
         refs=[dict(title='Ruby Documentation Home', url='https://www.ruby-lang.org/en/documentation/'),
               dict(title='Ruby in Twenty Minutes', url='https://www.ruby-lang.org/en/documentation/quickstart/'),
               dict(title='ruby-doc.org', url='https://ruby-doc.org/core-3.2.0/')]),
    dict(slug='ruby-02-variables-types', title='Variables and Data Types',
         desc='Local/instance/class/global variables, dynamic typing, symbols.',
         dur='60 min', diff='beginner', prereq=['RUBY-01'],
         objs=['Use the main object types and their classes',
               'Understand variable scope types',
               'Leverage dynamic typing',
               'Use symbols as lightweight identifiers'],
         refs=[dict(title='Ruby — Variables', url='https://docs.ruby-lang.org/en/master/syntax/assignment_rdoc.html'),
               dict(title='Ruby — Symbols', url='https://docs.ruby-lang.org/en/master/Symbol.html'),
               dict(title='Ruby — Literals', url='https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html')]),
    dict(slug='ruby-03-numbers', title='Numbers and Arithmetic',
         desc='Integer/Float semantics, operators, precision, and big numbers.',
         dur='45 min', diff='beginner', prereq=['RUBY-02'],
         objs=['Perform arithmetic with integers and floats',
               'Understand division semantics',
               'Use numeric literals and rounding',
               'Work with arbitrary-precision numbers'],
         refs=[dict(title='Ruby — Integer', url='https://docs.ruby-lang.org/en/master/Integer.html'),
               dict(title='Ruby — Float', url='https://docs.ruby-lang.org/en/master/Float.html'),
               dict(title='Ruby — BigDecimal', url='https://docs.ruby-lang.org/en/master/BigDecimal.html')]),
    dict(slug='ruby-04-strings', title='Strings and String Methods',
         desc='String manipulation, interpolation, formatting, and mutation.',
         dur='60 min', diff='beginner', prereq=['RUBY-03'],
         objs=['Use common string methods',
               'Interpolate and format strings',
               'Split, join, and replace text',
               'Understand mutability and freeze'],
         refs=[dict(title='Ruby — String', url='https://docs.ruby-lang.org/en/master/String.html'),
               dict(title='Ruby — String Literals', url='https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html'),
               dict(title='Ruby — format/sprintf', url='https://docs.ruby-lang.org/en/master/Kernel.html#method-i-sprintf')]),
    dict(slug='ruby-05-control-flow', title='Control Flow',
         desc='if/elsif/else, case/when, unless, and loops.',
         dur='60 min', diff='beginner', prereq=['RUBY-04'],
         objs=['Write if/elsif/else branches',
               'Use case/when expressions',
               'Use unless and inline conditionals',
               'Iterate with times, upto, and while'],
         refs=[dict(title='Ruby — Control Expressions', url='https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html'),
               dict(title='Ruby — Case Expression', url='https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html#label-case+Expression'),
               dict(title='Ruby — Loops', url='https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html#label-Loop+Control')]),
    dict(slug='ruby-06-arrays', title='Arrays',
         desc='Indexing, slicing, sorting, and Enumerable-powered transformation.',
         dur='60 min', diff='beginner', prereq=['RUBY-05'],
         objs=['Index and slice arrays',
               'Sort and search arrays',
               'Transform with map, select, reject',
               'Use nested and unique arrays'],
         refs=[dict(title='Ruby — Array', url='https://docs.ruby-lang.org/en/master/Array.html'),
               dict(title='Ruby — Enumerable', url='https://docs.ruby-lang.org/en/master/Enumerable.html'),
               dict(title='Ruby — Array Literals', url='https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html')]),
    dict(slug='ruby-07-hashes', title='Hashes and Symbols',
         desc='Hash construction, symbol keys, iteration, and transformation.',
         dur='60 min', diff='beginner', prereq=['RUBY-06'],
         objs=['Build and index hashes',
               'Use symbol keys with modern syntax',
               'Iterate and transform hashes',
               'Merge and fetch with defaults'],
         refs=[dict(title='Ruby — Hash', url='https://docs.ruby-lang.org/en/master/Hash.html'),
               dict(title='Ruby — Hash Literals', url='https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html'),
               dict(title='Ruby — Symbol', url='https://docs.ruby-lang.org/en/master/Symbol.html')]),
    dict(slug='ruby-08-methods', title='Methods and Arguments',
         desc='Method definitions, implicit returns, splat, keyword args, blocks.',
         dur='60 min', diff='intermediate', prereq=['RUBY-07'],
         objs=['Define methods with implicit returns',
               'Use splat (*) for variable arguments',
               'Use keyword and default arguments',
               'Accept blocks with &block'],
         refs=[dict(title='Ruby — Methods', url='https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html'),
               dict(title='Ruby — Method Arguments', url='https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html'),
               dict(title='Ruby — Method Calling', url='https://docs.ruby-lang.org/en/master/syntax/calling_methods_rdoc.html')]),
    dict(slug='ruby-09-classes', title='Classes and Objects',
         desc='Class definitions, initialize, attr_*, self, to_s.',
         dur='75 min', diff='beginner', prereq=['RUBY-08'],
         objs=['Define classes with initialize',
               'Use attr_reader/writer/accessor',
               'Use class variables and methods',
               'Override to_s and inspect'],
         refs=[dict(title='Ruby — Classes', url='https://docs.ruby-lang.org/en/master/syntax/classes_and_modules_rdoc.html'),
               dict(title='Ruby — attr_accessor', url='https://docs.ruby-lang.org/en/master/Module.html#method-i-attr_accessor'),
               dict(title='Ruby — Object Basics', url='https://docs.ruby-lang.org/en/master/Object.html')]),
    dict(slug='ruby-10-modules', title='Modules and Mixins',
         desc='include, extend, prepend, and namespace modules.',
         dur='75 min', diff='intermediate', prereq=['RUBY-09'],
         objs=['Define and include modules',
               'Use extend for class methods',
               'Understand include vs prepend ordering',
               'Compose behavior with mixins'],
         refs=[dict(title='Ruby — Modules', url='https://docs.ruby-lang.org/en/master/syntax/classes_and_modules_rdoc.html'),
               dict(title='Ruby — Module#include', url='https://docs.ruby-lang.org/en/master/Module.html#method-i-include'),
               dict(title='Ruby — Module#prepend', url='https://docs.ruby-lang.org/en/master/Module.html#method-i-prepend')]),
    dict(slug='ruby-11-inheritance', title='Inheritance',
         desc='Subclassing, super, override, and ancestry.',
         dur='60 min', diff='intermediate', prereq=['RUBY-10'],
         objs=['Subclass and override methods',
               'Call parent code with super',
               'Extend parent behavior',
               'Inspect ancestry with ancestors'],
         refs=[dict(title='Ruby — Inheritance', url='https://docs.ruby-lang.org/en/master/syntax/classes_and_modules_rdoc.html'),
               dict(title='Ruby — super', url='https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html'),
               dict(title='Ruby — Module#ancestors', url='https://docs.ruby-lang.org/en/master/Module.html#method-i-ancestors')]),
    dict(slug='ruby-12-blocks-procs', title='Blocks, Procs, and Lambdas',
         desc='yield, block params, proc vs lambda semantics, &block.',
         dur='75 min', diff='intermediate', prereq=['RUBY-11'],
         objs=['Yield to blocks',
               'Pass blocks explicitly with &',
               'Distinguish proc vs lambda return semantics',
               'Use shorthand syntax (&:method)'],
         refs=[dict(title='Ruby — Blocks', url='https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html#label-Block+Argument'),
               dict(title='Ruby — Proc', url='https://docs.ruby-lang.org/en/master/Proc.html'),
               dict(title='Ruby — Lambda', url='https://docs.ruby-lang.org/en/master/Proc.html#class-Proc-label-Lambda+semantics')]),
    dict(slug='ruby-13-enumerable', title='Enumerable Module',
         desc='map, select, reduce, group_by, tally, and lazy chains.',
         dur='75 min', diff='intermediate', prereq=['RUBY-12'],
         objs=['Transform with map and select',
               'Aggregate with reduce',
               'Group and tally data',
               'Build lazy enumerator chains'],
         refs=[dict(title='Ruby — Enumerable', url='https://docs.ruby-lang.org/en/master/Enumerable.html'),
               dict(title='Ruby — Enumerator::Lazy', url='https://docs.ruby-lang.org/en/master/Enumerator/Lazy.html'),
               dict(title='Ruby — each_with_object', url='https://docs.ruby-lang.org/en/master/Enumerable.html#method-i-each_with_object')]),
    dict(slug='ruby-14-exceptions', title='Exceptions and Error Handling',
         desc='begin/rescue/ensure, custom exceptions, raise.',
         dur='60 min', diff='intermediate', prereq=['RUBY-13'],
         objs=['Write begin/rescue/ensure blocks',
               'Rescue specific exception classes',
               'Define custom exception classes',
               'Use rescue clauses in methods'],
         refs=[dict(title='Ruby — Exceptions', url='https://docs.ruby-lang.org/en/master/syntax/exceptions_rdoc.html'),
               dict(title='Ruby — Exception Class', url='https://docs.ruby-lang.org/en/master/Exception.html'),
               dict(title='Ruby — raise', url='https://docs.ruby-lang.org/en/master/Kernel.html#method-i-raise')]),
    dict(slug='ruby-15-file-io', title='File I/O',
         desc='File read/write, blocks, iteration, FileUtils.',
         dur='60 min', diff='intermediate', prereq=['RUBY-14'],
         objs=['Write and read files',
               'Use File.open with blocks',
               'Iterate lines efficiently',
               'Manipulate files with FileUtils'],
         refs=[dict(title='Ruby — File', url='https://docs.ruby-lang.org/en/master/File.html'),
               dict(title='Ruby — IO', url='https://docs.ruby-lang.org/en/master/IO.html'),
               dict(title='Ruby — FileUtils', url='https://docs.ruby-lang.org/en/master/FileUtils.html')]),
    dict(slug='ruby-16-regex', title='Regular Expressions',
         desc='=~, match, scan, gsub, anchors, captures.',
         dur='75 min', diff='intermediate', prereq=['RUBY-15'],
         objs=['Match with =~ and Regexp',
               'Extract captures',
               'Scan and substitute text',
               'Write anchored and character-class patterns'],
         refs=[dict(title='Ruby — Regexp', url='https://docs.ruby-lang.org/en/master/Regexp.html'),
               dict(title='Ruby — Regexp Literals', url='https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html'),
               dict(title='Ruby — String#scan', url='https://docs.ruby-lang.org/en/master/String.html#method-i-scan')]),
    dict(slug='ruby-17-metaprogramming', title='Metaprogramming',
         desc='define_method, method_missing, send, instance_eval.',
         dur='75 min', diff='advanced', prereq=['RUBY-16'],
         objs=['Define methods dynamically',
               'Handle missing methods',
               'Dispatch dynamically with send',
               'Evaluate code in object context'],
         refs=[dict(title='Ruby — define_method', url='https://docs.ruby-lang.org/en/master/Module.html#method-i-define_method'),
               dict(title='Ruby — method_missing', url='https://docs.ruby-lang.org/en/master/BasicObject.html#method-i-method_missing'),
               dict(title='Ruby — send', url='https://docs.ruby-lang.org/en/master/Object.html#method-i-send')]),
    dict(slug='ruby-18-gems-tooling', title='Gems, Bundler, and Standard Library',
         desc='Gems, JSON, dates, Net::HTTP, and the standard library.',
         dur='60 min', diff='intermediate', prereq=['RUBY-17'],
         objs=['Understand gems and Bundler',
               'Parse and generate JSON',
               'Work with dates and times',
               'Make HTTP requests'],
         refs=[dict(title='RubyGems Guides', url='https://guides.rubygems.org/'),
               dict(title='Ruby — JSON', url='https://docs.ruby-lang.org/en/master/JSON.html'),
               dict(title='Ruby — Net::HTTP', url='https://docs.ruby-lang.org/en/master/Net/HTTP.html')]),
    dict(slug='ruby-19-testing', title='Testing with Minitest',
         desc='assertions, test classes, describe/it, mocks.',
         dur='60 min', diff='intermediate', prereq=['RUBY-18'],
         objs=['Write Minitest test classes',
               'Use assertions effectively',
               'Use describe/it style',
               'Mock collaborators'],
         refs=[dict(title='Minitest Documentation', url='https://docs.seattlerb.org/minitest/'),
               dict(title='Ruby — Minitest Guide', url='https://www.ruby-lang.org/en/documentation/'),
               dict(title='Minitest GitHub', url='https://github.com/minitest/minitest')]),
    dict(slug='ruby-20-concurrency', title='Threads and Concurrency',
         desc='Thread.new, Mutex, Queue, Fiber.',
         dur='75 min', diff='advanced', prereq=['RUBY-19'],
         objs=['Create and join threads',
               'Synchronize with Mutex',
               'Use Queue for producer/consumer',
               'Understand fibers'],
         refs=[dict(title='Ruby — Thread', url='https://docs.ruby-lang.org/en/master/Thread.html'),
               dict(title='Ruby — Mutex', url='https://docs.ruby-lang.org/en/master/Mutex.html'),
               dict(title='Ruby — Queue', url='https://docs.ruby-lang.org/en/master/Queue.html')]),
    dict(slug='ruby-21-advanced', title='Advanced: Pattern Matching and Refinements',
         desc='Case/in patterns, guards, and refinements.',
         dur='75 min', diff='expert', prereq=['RUBY-20'],
         objs=['Use hash and array patterns',
               'Destructure with in',
               'Guard patterns with if conditions',
               'Scope changes with refinements'],
         refs=[dict(title='Ruby — Pattern Matching', url='https://docs.ruby-lang.org/en/master/syntax/pattern_matching_rdoc.html'),
               dict(title='Ruby — Refinements', url='https://docs.ruby-lang.org/en/master/syntax/refinements_rdoc.html'),
               dict(title='Ruby — Case/In', url='https://docs.ruby-lang.org/en/master/syntax/control_expressions_rdoc.html')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'ruby', LESSONS, CODE, BASE)
