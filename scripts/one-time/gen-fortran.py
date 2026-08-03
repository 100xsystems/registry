#!/usr/bin/env python3
"""Generate the 21-lesson Fortran curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from fortran-lang.org and GCC docs.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
Escape hygiene: all \\n inside samples are written as \\\\n so they render literally.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'fortran'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'fortran')

CODE = {
    1: [
        '''! Your first Fortran program — free-form source (.f90)
program hello
  implicit none
  print *, 'Hello, 100X Systems!'
end program hello
! Compile:  gfortran -o hello hello.f90
! Run:      ./hello
''',
        '''! Compile and run workflow
! $ gfortran -o greet greet.f90 && ./greet
program greet
  implicit none
  character(len=20) :: name
  name = 'Fortran'
  print *, 'Welcome to ', name
end program greet
''',
        '''! Free-form vs fixed-form source
! .f90 = free form (modern, recommended)
! .f   = fixed form (legacy 72-column layout)
program freeform
  implicit none
  print *, 'free-form source'
end program freeform
''',
        '''! implicit none — declare everything explicitly
program strict
  implicit none
  integer :: x
  x = 42
  print *, 'x =', x
end program strict
''',
    ],
    2: [
        '''program types
  implicit none
  integer :: i
  real :: r
  complex :: c
  logical :: l
  character(len=10) :: s

  i = 10
  r = 3.5
  c = (1.0, 2.0)
  l = .true.
  s = 'hello'
  print *, i, r, c, l, s
end program types
''',
        '''! Numeric literals: integer, real, double, complex, logical, character
program literals
  implicit none
  integer, parameter :: big = 1000000
  print *, 'int ', 42
  print *, 'real ', 3.14
  print *, 'double ', 3.141592653589793d0
  print *, 'complex ', (0.5, -0.25)
  print *, 'logical ', .true.
  print *, 'char ', 'a'
  print *, 'hex ', z'FF'
end program literals
''',
        '''! Kind parameters — control precision portably
program kinds
  implicit none
  integer, parameter :: dp = selected_real_kind(15, 307)
  real(dp) :: x
  x = 1.0_dp / 3.0_dp
  print *, precision(x), x
end program kinds
''',
        '''! Default real (single) vs double precision
program defaultvsdouble
  implicit none
  real :: a
  double precision :: b
  a = 1.0 / 3.0
  b = 1.0d0 / 3.0d0
  print *, a
  print *, b
end program defaultvsdouble
''',
    ],
    3: [
        '''program vars
  implicit none
  integer :: count
  real :: temperature
  character(len=30) :: name

  count = 1
  temperature = 36.6
  name = 'Ada Lovelace'
  print *, count, temperature, name
end program vars
''',
        '''! Named constants with parameter
program constants
  implicit none
  real, parameter :: pi = 3.14159265
  integer, parameter :: max_iter = 1000
  print *, 'pi =', pi
  print *, 'max iterations =', max_iter
end program constants
''',
        '''! Initialization at declaration
program init
  implicit none
  integer :: x = 5
  integer :: counter = 0
  counter = counter + 1
  print *, x, counter
end program init
''',
        '''! Variable scope: host association with internal procedures
program scope
  implicit none
  integer :: a
  a = 10
  call show(a)
contains
  subroutine show(v)
    implicit none
    integer, intent(in) :: v
    print *, 'received', v
  end subroutine show
end program scope
''',
    ],
    4: [
        '''program arith
  implicit none
  integer :: a, b
  a = 7
  b = 3
  print *, 'sum ', a + b
  print *, 'diff ', a - b
  print *, 'prod ', a * b
  print *, 'div ', a / b       ! integer division -> 2
  print *, 'mod ', mod(a, b)
  print *, 'pow ', a ** 2
end program arith
''',
        '''! Relational operators: == /= < <= > >=
program compare
  implicit none
  integer :: a, b
  a = 5
  b = 9
  print *, a < b        ! T
  print *, a <= b       ! T
  print *, a /= b       ! T  (not equal)
  print *, a == b       ! F
  print *, a > b        ! F
end program compare
''',
        '''! Logical operators: .and. .or. .not. .eqv. .neqv.
program logic
  implicit none
  logical :: p, q
  p = .true.
  q = .false.
  print *, p .and. q    ! F
  print *, p .or. q     ! T
  print *, .not. p      ! F
  print *, p .eqv. q    ! F
  print *, p .neqv. q   ! T
end program logic
''',
        '''! Operator precedence: ** > * / > + - ; ** is right-associative
program prec
  implicit none
  integer :: r
  r = 2 + 3 * 4        ! 14
  print *, r
  r = (2 + 3) * 4      ! 20
  print *, r
  r = 2 ** 3 ** 2      ! 512
  print *, r
end program prec
''',
    ],
    5: [
        '''program ifelse
  implicit none
  integer :: x
  x = -3
  if (x > 0) then
    print *, 'positive'
  else if (x < 0) then
    print *, 'negative'
  else
    print *, 'zero'
  end if
end program ifelse
''',
        '''! Single-line IF statement
program oneif
  implicit none
  integer :: n
  n = 10
  if (n > 5) print *, 'big'
  if (n > 20) print *, 'huge'   ! not printed
end program oneif
''',
        '''! SELECT CASE — clean multi-way branch
program grade
  implicit none
  integer :: score
  score = 85
  select case (score)
  case (90:)
    print *, 'A'
  case (80:89)
    print *, 'B'
  case (70:79)
    print *, 'C'
  case default
    print *, 'F'
  end select
end program grade
''',
        '''! WHERE — masked array assignment
program whereblock
  implicit none
  real, dimension(5) :: v
  v = [1.0, -2.0, 3.0, -4.0, 5.0]
  where (v < 0)
    v = 0.0
  end where
  print *, v
end program whereblock
''',
    ],
    6: [
        '''program doloop
  implicit none
  integer :: i
  do i = 1, 5
    print *, i
  end do
end program doloop
''',
        '''! DO with step, including counting down
program loopstep
  implicit none
  integer :: i
  do i = 10, 2, -2
    print *, i
  end do
end program loopstep
''',
        '''! DO WHILE — loop while a condition holds
program dwhile
  implicit none
  integer :: n
  n = 1
  do while (n <= 64)
    print *, n
    n = n * 2
  end do
end program dwhile
''',
        '''! CYCLE skips an iteration; EXIT leaves the loop
program loopctrl
  implicit none
  integer :: i
  do i = 1, 10
    if (i == 3) cycle      ! skip 3
    if (i == 8) exit       ! stop at 8
    print *, i
  end do
end program loopctrl
''',
    ],
    7: [
        '''program array1
  implicit none
  integer, dimension(5) :: a
  integer :: i
  a = [10, 20, 30, 40, 50]
  print *, a(1)
  print *, a(5)
  print *, a(2:4)          ! array section
  do i = 1, 5
    print *, a(i) * 2
  end do
end program array1
''',
        '''! Two-dimensional arrays and implied-do output
program array2d
  implicit none
  integer, dimension(2,3) :: m
  integer :: i, j
  m = reshape([1, 2, 3, 4, 5, 6], [2, 3])
  do i = 1, 2
    print *, (m(i, j), j = 1, 3)
  end do
end program array2d
''',
        '''! Whole-array operations — no explicit loops needed
program arr_ops
  implicit none
  real, dimension(3) :: a, b, c
  a = [1.0, 2.0, 3.0]
  b = [4.0, 5.0, 6.0]
  c = a + b
  print *, c
  print *, 2.0 * a
  print *, sum(a), maxval(a)
end program arr_ops
''',
        '''! Allocatable arrays — size decided at runtime
program alloc
  implicit none
  integer, allocatable :: a(:)
  integer :: n, i
  n = 5
  allocate(a(n))
  a = [(i, i = 1, n)]
  print *, a
  deallocate(a)
end program alloc
''',
    ],
    8: [
        '''! CHARACTER strings are fixed-length by default
program strings
  implicit none
  character(len=20) :: greeting
  greeting = 'Hello, Fortran'
  print *, greeting
  print *, len(greeting)
  print *, len_trim(greeting)   ! 13
end program strings
''',
        '''! Concatenation with // and trimming
program concat
  implicit none
  character(len=30) :: msg
  character(len=10) :: first, last
  first = 'Grace'
  last = 'Hopper'
  msg = trim(first) // ' ' // last
  print *, msg
end program concat
''',
        '''! Substrings and INDEX
program substr
  implicit none
  character(len=20) :: s
  s = 'The quick brown fox'
  print *, s(5:9)                 ! quick
  print *, index(s, 'fox')        ! 17
  s(5:9) = 'slow '
  print *, s
end program substr
''',
        '''! ASCII conversion with IACHAR / ACHAR
program chars
  implicit none
  character(len=1) :: c
  integer :: i
  c = 'B'
  print *, iachar(c)        ! 66
  print *, achar(65)        ! A
  do i = 97, 100
    print *, achar(i)
  end do
end program chars
''',
    ],
    9: [
        '''! External function
program funcs
  implicit none
  integer :: square
  print *, square(5)
end program funcs

integer function square(n)
  implicit none
  integer, intent(in) :: n
  square = n * n
end function square
''',
        '''! Subroutine with intent(out)
program subr
  implicit none
  real :: a, b, s
  a = 3.0
  b = 4.0
  call add(a, b, s)
  print *, s
end program subr

subroutine add(x, y, out)
  implicit none
  real, intent(in) :: x, y
  real, intent(out) :: out
  out = x + y
end subroutine add
''',
        '''! Internal procedures live inside the program (host association)
program internal
  implicit none
  print *, double(21)
contains
  integer function double(n)
    integer, intent(in) :: n
    double = 2 * n
  end function double
end program internal
''',
        '''! Recursion with RESULT clause
program recurse
  implicit none
  integer :: fib
  print *, fib(10)        ! 55
contains
  recursive function fib(n) result(f)
    integer, intent(in) :: n
    integer :: f
    if (n <= 1) then
      f = n
    else
      f = fib(n-1) + fib(n-2)
    end if
  end function fib
end program recurse
''',
    ],
    10: [
        '''! Modules group data and procedures
module math_mod
  implicit none
  real, parameter :: pi = 3.14159265
contains
  real function area(r)
    real, intent(in) :: r
    area = pi * r * r
  end function area
end module math_mod

program usemod
  use math_mod
  implicit none
  print *, area(2.0)
end program usemod
''',
        '''! Control visibility with PRIVATE / PUBLIC
module utils
  implicit none
  private
  public :: add, sub
contains
  integer function add(a, b)
    integer, intent(in) :: a, b
    add = a + b
  end function add
  integer function sub(a, b)
    integer, intent(in) :: a, b
    sub = a - b
  end function sub
  integer function mul(a, b)
    integer, intent(in) :: a, b
    mul = a * b
  end function mul
end module utils
''',
        '''! USE with ONLY — import just what you need
module constants_mod
  implicit none
  real, parameter :: pi = 3.14159
  real, parameter :: e = 2.71828
end module constants_mod

program onlyuse
  use constants_mod, only: pi
  implicit none
  print *, pi
end program onlyuse
''',
        '''! Generic interfaces let one name call several procedures
module sort_mod
  implicit none
  interface sort
    module procedure sort_int, sort_real
  end interface
contains
  subroutine sort_int(a)
    integer, intent(inout) :: a(:)
    integer :: i, j, tmp
    do i = 1, size(a)-1
      do j = i+1, size(a)
        if (a(i) > a(j)) then
          tmp = a(i); a(i) = a(j); a(j) = tmp
        end if
      end do
    end do
  end subroutine sort_int
  subroutine sort_real(a)
    real, intent(inout) :: a(:)
    integer :: i, j
    real :: tmp
    do i = 1, size(a)-1
      do j = i+1, size(a)
        if (a(i) > a(j)) then
          tmp = a(i); a(i) = a(j); a(j) = tmp
        end if
      end do
    end do
  end subroutine sort_real
end module sort_mod
''',
    ],
    11: [
        '''! Writing to a file with an explicit unit number
program fileout
  implicit none
  integer :: unit
  unit = 10
  open(unit, file='out.txt', status='replace')
  write(unit, *) 'line one'
  write(unit, *) 'line two', 42
  close(unit)
end program fileout
''',
        '''! Reading until EOF using IOSTAT
program fileread
  implicit none
  integer :: unit, ios, n
  real :: x
  unit = 11
  open(unit, file='data.txt', status='old', iostat=ios)
  if (ios /= 0) then
    print *, 'cannot open'
    stop
  end if
  do
    read(unit, *, iostat=ios) n, x
    if (ios /= 0) exit
    print *, n, x
  end do
  close(unit)
end program fileread
''',
        '''! FORMAT descriptors control exact output layout
program format
  implicit none
  integer :: id
  real :: gpa
  id = 42
  gpa = 3.7
  print '(A, I5)', 'ID: ', id
  print '(A, F5.2)', 'GPA: ', gpa
end program format
''',
        '''! Unformatted (binary) files for compact I/O
program unformatted
  implicit none
  integer :: unit, i
  unit = 20
  open(unit, file='b.dat', form='unformatted', status='replace')
  do i = 1, 3
    write(unit) i, i * 10
  end do
  close(unit)
end program unformatted
''',
    ],
    12: [
        '''! Derived types bundle related data
program dtype
  implicit none
  type :: point
    real :: x, y
  end type point
  type(point) :: p
  p = point(1.0, 2.0)
  print *, p%x, p%y
end program dtype
''',
        '''! Components can be strings and allocatable arrays
program person
  implicit none
  type :: student
    character(len=20) :: name
    integer :: age
    real, allocatable :: scores(:)
  end type student
  type(student) :: s
  s = student('Ada', 36, [9.0, 8.5, 10.0])
  print *, s%name, s%age
  print *, sum(s%scores)
end program person
''',
        '''! Arrays of derived types
program people
  implicit none
  type :: person
    character(len=20) :: name
    integer :: age
  end type person
  type(person), dimension(3) :: group
  integer :: i
  group(1) = person('Alan', 41)
  group(2) = person('Edsger', 62)
  group(3) = person('Donald', 84)
  do i = 1, 3
    print *, group(i)%name, group(i)%age
  end do
end program people
''',
        '''! Default component initialization
program typeinit
  implicit none
  type :: rect
    real :: w = 1.0
    real :: h = 1.0
  end type rect
  type(rect) :: r
  print *, r%w, r%h
end program typeinit
''',
    ],
    13: [
        '''! Pointers alias existing variables via =>
program pointers
  implicit none
  integer, target :: x
  integer, pointer :: p
  x = 7
  p => x
  print *, p            ! 7
  p = 10
  print *, x            ! 10 (through the pointer)
end program pointers
''',
        '''! ALLOCATABLE pointers with dynamic lifetime
program allocptr
  implicit none
  integer, pointer :: p(:)
  allocate(p(5))
  p = [1, 2, 3, 4, 5]
  print *, p(3)
  deallocate(p)
  nullify(p)
end program allocptr
''',
        '''! A pointer can target an array section
program ptrsection
  implicit none
  real, target :: a(10)
  real, pointer :: tail(:)
  integer :: i
  a = [(real(i), i = 1, 10)]
  tail => a(7:10)
  print *, tail
end program ptrsection
''',
        '''! Classic linked list with pointer components
program list
  implicit none
  type :: node
    integer :: val
    type(node), pointer :: next
  end type node
  type(node), pointer :: head, cur
  integer :: i
  nullify(head)
  do i = 1, 3
    allocate(cur)
    cur%val = i * 10
    cur%next => head
    head => cur
  end do
  cur => head
  do while (associated(cur))
    print *, cur%val
    cur => cur%next
  end do
end program list
''',
    ],
    14: [
        '''program intrins
  implicit none
  print *, abs(-5)
  print *, mod(7, 3)
  print *, max(1, 9, 4), min(1, 9, 4)
  print *, nint(2.7), floor(2.7), ceiling(2.2)
  print *, sqrt(16.0)
end program intrins
''',
        '''! Transcendental and exponential functions
program math
  implicit none
  print *, sin(0.0)
  print *, cos(0.0)
  print *, exp(1.0)
  print *, log(exp(1.0))
  print *, atan2(1.0, 1.0)
end program math
''',
        '''! String intrinsics
program strintr
  implicit none
  character(len=20) :: s
  s = '  hello  '
  print *, len(s)
  print *, len_trim(s)
  print *, index('abcdef', 'cd')
  print *, trim(s), '!'
end program strintr
''',
        '''! Kind / type inquiry intrinsics
program typintr
  implicit none
  integer :: a
  real :: b
  print *, kind(a), kind(b)
  print *, selected_int_kind(9)
  print *, selected_real_kind(15, 307)
end program typintr
''',
    ],
    15: [
        '''program arrintr
  implicit none
  real, dimension(4) :: v
  v = [2.0, 4.0, 6.0, 8.0]
  print *, sum(v)
  print *, product(v)
  print *, maxval(v), minval(v)
  print *, maxloc(v), minloc(v)
end program arrintr
''',
        '''! Linear algebra: dot_product and matmul
program linear
  implicit none
  real, dimension(3) :: a, b
  real, dimension(2,2) :: m1, m2, r
  a = [1.0, 2.0, 3.0]
  b = [4.0, 5.0, 6.0]
  print *, dot_product(a, b)
  m1 = reshape([1.0, 2.0, 3.0, 4.0], [2, 2])
  m2 = reshape([5.0, 6.0, 7.0, 8.0], [2, 2])
  r = matmul(m1, m2)
  print *, r(1,1), r(1,2)
  print *, r(2,1), r(2,2)
end program linear
''',
        '''! count, merge, pack — mask-driven selection
program counts
  implicit none
  integer, dimension(5) :: v
  v = [1, -2, 3, -4, 5]
  print *, count(v > 0)
  print *, merge(1, 0, v > 0)
  print *, pack(v, v > 0)
end program counts
''',
        '''! cshift and eoshift — rotate and shift arrays
program shiftarr
  implicit none
  integer, dimension(4) :: v
  v = [1, 2, 3, 4]
  print *, cshift(v, 1)
  print *, eoshift(v, 2, 0)
  print *, spread([10, 20], 1, 3)
end program shiftarr
''',
    ],
    16: [
        '''! Type-bound procedures give Fortran OOP
module shapes
  implicit none
  type :: shape
    real :: area
  contains
    procedure :: describe
  end type shape
contains
  subroutine describe(self)
    class(shape), intent(in) :: self
    print *, 'area = ', self%area
  end subroutine describe
end module shapes

program oop1
  use shapes
  implicit none
  type(shape) :: s
  s%area = 12.5
  call s%describe()
end program oop1
''',
        '''! Inheritance with TYPE, EXTENDS
module circles
  use shapes
  implicit none
  type, extends(shape) :: circle
    real :: radius
  contains
    procedure :: compute_area
  end type circle
contains
  subroutine compute_area(self)
    class(circle), intent(inout) :: self
    self%area = 3.14159 * self%radius ** 2
  end subroutine compute_area
end module circles

program oop2
  use circles
  implicit none
  type(circle) :: c
  c%radius = 2.0
  call c%compute_area()
  call c%describe()
end program oop2
''',
        '''! Polymorphism and SELECT TYPE dispatch
program oop3
  implicit none
  type :: animal
    character(len=20) :: name
  end type animal
  type, extends(animal) :: dog
    logical :: friendly
  end type dog
  class(animal), allocatable :: a
  type(dog) :: d
  d%name = 'Rex'
  d%friendly = .true.
  allocate(a, source=d)
  select type (a)
  type is (dog)
    print *, a%friendly
  class default
    print *, 'other animal'
  end select
end program oop3
''',
        '''! FINAL procedures run automatically on deallocation
module matrix_mod
  implicit none
  type :: matrix
    integer, allocatable :: data(:,:)
  contains
    final :: cleanup
  end type matrix
contains
  subroutine cleanup(m)
    type(matrix), intent(inout) :: m
    if (allocated(m%data)) deallocate(m%data)
    print *, 'cleaned up'
  end subroutine cleanup
end module matrix_mod

program oop4
  use matrix_mod
  implicit none
  type(matrix) :: m
  allocate(m%data(2,2))
  m%data = 1
  print *, m%data(1,1)
end program oop4
''',
    ],
    17: [
        '''! OpenMP: parallel regions and worksharing
program omp
  use omp_lib
  implicit none
  integer :: i, tid
  !$omp parallel private(i, tid)
  tid = omp_get_thread_num()
  !$omp do
  do i = 1, 8
    print *, 'thread', tid, 'i =', i
  end do
  !$omp end do
  !$omp end parallel
end program omp
! Compile: gfortran -fopenmp -o omp omp.f90
''',
        '''! OpenMP reduction — safe accumulation across threads
program reduction
  use omp_lib
  implicit none
  integer :: i, total
  total = 0
  !$omp parallel do reduction(+:total)
  do i = 1, 100
    total = total + i
  end do
  !$omp end parallel do
  print *, total     ! 5050
end program reduction
''',
        '''! Coarrays — Fortran's native parallel model
program coarray
  implicit none
  integer :: a[*]
  integer :: me, n
  me = this_image()
  n = num_images()
  a = me * 100
  sync all
  print *, 'image', me, 'of', n, 'saw', a[1]
end program coarray
! Compile: gfortran -fcoarray=single -o co co.f90
''',
        '''! CRITICAL section protects a shared variable
program critical
  use omp_lib
  implicit none
  integer :: i, shared
  shared = 0
  !$omp parallel do
  do i = 1, 10
    !$omp critical
    shared = shared + i
    !$omp end critical
  end do
  !$omp end parallel do
  print *, shared    ! 55
end program critical
''',
    ],
    18: [
        '''! Call C library functions via ISO_C_BINDING
program interop
  use iso_c_binding
  implicit none
  interface
    function strlen(s) bind(C, name='strlen')
      import :: c_char, c_size_t
      character(kind=c_char) :: s(*)
      integer(c_size_t) :: strlen
    end function strlen
  end interface
  character(kind=c_char), parameter :: msg(*) = [c_char_'h', c_char_'i', c_null_char]
  print *, strlen(msg)
end program interop
! Compile: gfortran -o interop interop.f90
''',
        '''! Export a Fortran procedure with a C-compatible name
module cmath
  use iso_c_binding
  implicit none
contains
  subroutine c_add(a, b, out) bind(C, name='c_add')
    integer(c_int), value :: a, b
    integer(c_int), intent(out) :: out
    out = a + b
  end subroutine c_add
end module cmath
! Callable from C as:  extern void c_add(int a, int b, int *out);
''',
        '''! c_loc / c_f_pointer — pass pointers to C
program cptr
  use iso_c_binding
  implicit none
  integer(c_int), target :: x
  type(c_ptr) :: p
  integer(c_int), pointer :: fp
  x = 42
  p = c_loc(x)
  call c_f_pointer(p, fp)
  print *, fp
end program cptr
''',
        '''! Interoperable derived types with BIND(C)
program cstruct
  use iso_c_binding
  implicit none
  type, bind(C) :: cpoint
    real(c_float) :: x, y
  end type cpoint
  type(cpoint) :: p
  p%x = 1.0
  p%y = 2.0
  print *, p%x, p%y
end program cstruct
''',
    ],
    19: [
        '''! DO CONCURRENT — safe data-parallel loops
program doconc
  implicit none
  integer, parameter :: n = 8
  real, dimension(n) :: a
  integer :: i
  do concurrent (i = 1:n)
    a(i) = real(i) ** 2
  end do
  print *, a
end program doconc
''',
        '''! ASSOCIATE gives a short name to a complex expression
program associate_demo
  implicit none
  real, dimension(3,3) :: m
  integer :: i
  m = 0.0
  do i = 1, 3
    m(i,i) = 1.0
  end do
  associate (diag => m(1,1))
    print *, diag
  end associate
  print *, m(2,2)
end program associate_demo
''',
        '''! Implied-DO array constructors
program implied
  implicit none
  integer, dimension(5) :: a
  integer :: i
  a = [(i ** 2, i = 1, 5)]
  print *, a
  print *, (i, i = 5, 1, -1)
end program implied
''',
        '''! ELEMENTAL functions apply element-by-element
program elemental_demo
  implicit none
  real, dimension(4) :: v, r
  v = [1.0, 4.0, 9.0, 16.0]
  r = sqrt(v)
  print *, r
end program elemental_demo
''',
    ],
    20: [
        '''! IOSTAT turns I/O failures into checkable codes
program errhandle
  implicit none
  integer :: ios, unit
  unit = 30
  open(unit, file='missing.txt', status='old', iostat=ios)
  if (ios /= 0) then
    print *, 'file not found'
  else
    close(unit)
  end if
end program errhandle
''',
        '''! ERROR STOP aborts with a message
program stopdemo
  implicit none
  integer :: age
  age = -5
  if (age < 0) then
    error stop 'negative age!'
  end if
  print *, 'ok'
end program stopdemo
''',
        '''! ALLOCATE with STAT handles allocation failure
program allocerr
  implicit none
  integer, allocatable :: a(:)
  integer :: stat
  allocate(a(10), stat=stat)
  if (stat /= 0) then
    print *, 'allocation failed'
    stop
  end if
  a = 1
  print *, sum(a)
  deallocate(a)
end program allocerr
''',
        '''! NEWUNIT picks an unused unit number for you
program newunit
  implicit none
  integer :: unit, ios
  open(newunit=unit, file='tmp.txt', status='replace', iostat=ios)
  write(unit, *) 'hello'
  close(unit)
  print *, 'unit used:', unit
end program newunit
''',
    ],
    21: [
        '''! Fortran arrays are column-major — loop order matters
program colmajor
  implicit none
  integer, parameter :: n = 1000
  real, dimension(n, n) :: m
  integer :: i, j
  m = 0.0
  do j = 1, n
    do i = 1, n
      m(i, j) = real(i + j)
    end do
  end do
  print *, m(1, 1), m(n, n)
end program colmajor
''',
        '''! INTENT helps the compiler optimize and catches bugs
program perf
  implicit none
  real, dimension(3) :: a
  a = [1.0, 2.0, 3.0]
  call scale(a, 2.0)
  print *, a
contains
  subroutine scale(x, factor)
    real, intent(inout) :: x(:)
    real, intent(in) :: factor
    x = x * factor
  end subroutine scale
end program perf
''',
        '''! Measure CPU time with CPU_TIME
program bench
  implicit none
  integer, parameter :: n = 1000000
  real, dimension(n) :: a, b
  real :: t1, t2, result
  a = 1.0
  b = 2.0
  call cpu_time(t1)
  result = dot_product(a, b)
  call cpu_time(t2)
  print *, result
  print *, 'elapsed', t2 - t1
end program bench
''',
        '''! MATMUL beats hand-written loops for large matrices
program matperf
  implicit none
  integer, parameter :: n = 200
  real, dimension(n, n) :: x, y, z
  real :: t1, t2
  call random_number(x)
  call random_number(y)
  call cpu_time(t1)
  z = matmul(x, y)
  call cpu_time(t2)
  print *, z(1, 1)
  print *, 'matmul time', t2 - t1
end program matperf
''',
    ],
}

LESSONS = [
    dict(
        slug='fortran-01-getting-started',
        title='Getting Started with Fortran',
        desc='Compiler setup, free-form source, and your first program.',
        diff='beginner',
        dur=15,
        objs=[
            'Write, compile, and run a hello-world program',
            'Understand free-form vs fixed-form source files',
            'Use implicit none for explicit declarations',
        ],
        prereq=[],
        refs=[dict(title='Fortran Quickstart Tutorial', url='https://fortran-lang.org/learn/quickstart/'),
              dict(title='GCC gfortran Manual', url='https://gcc.gnu.org/onlinedocs/gfortran/'),
              dict(title='fortran-lang.org — Learn', url='https://fortran-lang.org/en/learn/')]),
    dict(
        slug='fortran-02-data-types',
        title='Data Types and Literals',
        desc='Integer, real, complex, logical, and character types.',
        diff='beginner',
        dur=20,
        objs=[
            'Declare and use all intrinsic types',
            'Write typed literals including double precision',
            'Select precision portably with kind parameters',
        ],
        prereq=['fortran-01-getting-started'],
        refs=[dict(title='Fortran — Data Types', url='https://fortran-lang.org/learn/quickstart/variables/'),
              dict(title='GCC — Intrinsic Types', url='https://gcc.gnu.org/onlinedocs/gfortran/Intrinsic-Types.html')]),
    dict(
        slug='fortran-03-variables-constants',
        title='Variables and Constants',
        desc='Declaration, initialization, parameters, and scope.',
        diff='beginner',
        dur=20,
        objs=[
            'Declare and initialize variables',
            'Define named constants with parameter',
            'Explain host association with internal procedures',
        ],
        prereq=['fortran-02-data-types'],
        refs=[dict(title='Fortran — Variables', url='https://fortran-lang.org/learn/quickstart/variables/'),
              dict(title='Fortran Best Practices', url='https://fortran-lang.org/en/learn/best_practices/')]),
    dict(
        slug='fortran-04-operators',
        title='Operators and Expressions',
        desc='Arithmetic, relational, logical operators, and precedence.',
        diff='beginner',
        dur=20,
        objs=[
            'Use arithmetic operators including exponentiation',
            'Compare values with relational operators',
            'Combine conditions with logical operators',
        ],
        prereq=['fortran-03-variables-constants'],
        refs=[dict(title='Fortran — Expressions', url='https://fortran-lang.org/learn/quickstart/variables/'),
              dict(title='GCC — Operator Precedence', url='https://gcc.gnu.org/onlinedocs/gfortran/Operator-Precedence.html')]),
    dict(
        slug='fortran-05-control-flow',
        title='Control Flow',
        desc='IF, SELECT CASE, and WHERE for decision making.',
        diff='beginner',
        dur=20,
        objs=[
            'Branch with IF / ELSE IF / ELSE',
            'Use SELECT CASE for multi-way branches',
            'Apply masked assignment with WHERE',
        ],
        prereq=['fortran-04-operators'],
        refs=[dict(title='Fortran — Control Constructs', url='https://fortran-lang.org/learn/quickstart/control_constructs/'),
              dict(title='GCC — SELECT CASE', url='https://gcc.gnu.org/onlinedocs/gfortran/SELECT-CASE.html')]),
    dict(
        slug='fortran-06-loops',
        title='Loops',
        desc='DO, DO WHILE, CYCLE, and EXIT.',
        diff='beginner',
        dur=20,
        objs=[
            'Write counted DO loops with steps',
            'Loop while a condition holds with DO WHILE',
            'Control iteration with CYCLE and EXIT',
        ],
        prereq=['fortran-05-control-flow'],
        refs=[dict(title='Fortran — Loops', url='https://fortran-lang.org/learn/quickstart/loops/'),
              dict(title='GCC — DO Construct', url='https://gcc.gnu.org/onlinedocs/gfortran/DO-Construct.html')]),
    dict(
        slug='fortran-07-arrays',
        title='Arrays',
        desc='Declaring, indexing, sections, and whole-array operations.',
        diff='beginner',
        dur=25,
        objs=[
            'Declare 1-D and 2-D arrays',
            'Slice arrays with section notation',
            'Use allocatable arrays and array constructors',
        ],
        prereq=['fortran-06-loops'],
        refs=[dict(title='Fortran — Arrays', url='https://fortran-lang.org/learn/quickstart/arrays/'),
              dict(title='Fortran — Array Constructors', url='https://fortran-lang.org/learn/quickstart/arrays/')]),
    dict(
        slug='fortran-08-strings',
        title='Character Strings',
        desc='Fixed-length strings, concatenation, substrings, ASCII.',
        diff='beginner',
        dur=20,
        objs=[
            'Work with character variables of fixed length',
            'Concatenate and trim strings',
            'Slice substrings and convert with IACHAR/ACHAR',
        ],
        prereq=['fortran-07-arrays'],
        refs=[dict(title='GCC — Character Handling', url='https://gcc.gnu.org/onlinedocs/gfortran/Character-handling.html'),
              dict(title='GCC — ACHAR', url='https://gcc.gnu.org/onlinedocs/gfortran/ACHAR.html')]),
    dict(
        slug='fortran-09-procedures',
        title='Functions and Subroutines',
        desc='Functions, subroutines, intent, recursion.',
        diff='beginner',
        dur=25,
        objs=[
            'Define functions and subroutines',
            'Use intent(in), intent(out), intent(inout)',
            'Write recursive functions with RESULT',
        ],
        prereq=['fortran-08-strings'],
        refs=[dict(title='Fortran — Functions', url='https://fortran-lang.org/learn/quickstart/procedures/'),
              dict(title='Fortran — Subroutines', url='https://fortran-lang.org/learn/quickstart/procedures/')]),
    dict(
        slug='fortran-10-modules',
        title='Modules and Interfaces',
        desc='Module organization, visibility control, generics.',
        diff='intermediate',
        dur=25,
        objs=[
            'Organize code into modules with USE',
            'Control names with PRIVATE and PUBLIC',
            'Create generic interfaces',
        ],
        prereq=['fortran-09-procedures'],
        refs=[dict(title='Fortran — Modules', url='https://fortran-lang.org/learn/quickstart/modules/'),
              dict(title='GCC — MODULE', url='https://gcc.gnu.org/onlinedocs/gfortran/MODULE.html')]),
    dict(
        slug='fortran-11-file-io',
        title='File Input/Output',
        desc='OPEN/READ/WRITE/CLOSE, formatted and unformatted I/O.',
        diff='intermediate',
        dur=25,
        objs=[
            'Open, read, and write text files',
            'Handle EOF and errors with IOSTAT',
            'Use FORMAT descriptors and binary files',
        ],
        prereq=['fortran-10-modules'],
        refs=[dict(title='Fortran — File I/O', url='https://fortran-lang.org/learn/quickstart/io/'),
              dict(title='GCC — IOSTAT', url='https://gcc.gnu.org/onlinedocs/gfortran/IOSTAT.html')]),
    dict(
        slug='fortran-12-derived-types',
        title='Derived Types',
        desc='User-defined types, components, arrays of types.',
        diff='intermediate',
        dur=25,
        objs=[
            'Define and use derived types',
            'Include arrays and strings as components',
            'Build arrays of derived types',
        ],
        prereq=['fortran-11-file-io'],
        refs=[dict(title='Fortran — Derived Types', url='https://fortran-lang.org/learn/quickstart/derived_types/'),
              dict(title='GCC — Derived Types', url='https://gcc.gnu.org/onlinedocs/gfortran/Derived-Types.html')]),
    dict(
        slug='fortran-13-pointers',
        title='Pointers and Dynamic Memory',
        desc='Pointer association, allocation, linked structures.',
        diff='intermediate',
        dur=25,
        objs=[
            'Associate pointers with targets',
            'Allocate and deallocate pointer arrays',
            'Build linked structures with pointer components',
        ],
        prereq=['fortran-12-derived-types'],
        refs=[dict(title='GCC — Pointers', url='https://gcc.gnu.org/onlinedocs/gfortran/Pointers.html'),
              dict(title='Fortran — Allocatable and Pointer', url='https://fortran-lang.org/learn/quickstart/arrays/')]),
    dict(
        slug='fortran-14-intrinsics',
        title='Intrinsic Procedures',
        desc='Math, string, and inquiry functions built into the language.',
        diff='intermediate',
        dur=20,
        objs=[
            'Use numeric and rounding intrinsics',
            'Apply trigonometric and exponential functions',
            'Query types and kinds portably',
        ],
        prereq=['fortran-13-pointers'],
        refs=[dict(title='GCC — Intrinsic Procedures', url='https://gcc.gnu.org/onlinedocs/gfortran/Intrinsic-Procedures.html'),
              dict(title='Fortran — Intrinsics', url='https://fortran-lang.org/en/learn/intrinsics/')]),
    dict(
        slug='fortran-15-array-intrinsics',
        title='Array Intrinsics and Vectorization',
        desc='sum, product, matmul, where, pack — array programming.',
        diff='intermediate',
        dur=25,
        objs=[
            'Reduce arrays with sum and product',
            'Multiply matrices with matmul',
            'Select data with pack, merge, count',
        ],
        prereq=['fortran-14-intrinsics'],
        refs=[dict(title='GCC — MATMUL', url='https://gcc.gnu.org/onlinedocs/gfortran/MATMUL.html'),
              dict(title='GCC — DOT_PRODUCT', url='https://gcc.gnu.org/onlinedocs/gfortran/DOT_005fPRODUCT.html')]),
    dict(
        slug='fortran-16-oop',
        title='Object-Oriented Programming',
        desc='Type-bound procedures, inheritance, polymorphism, final.',
        diff='advanced',
        dur=30,
        objs=[
            'Attach procedures to types',
            'Extend types with TYPE, EXTENDS',
            'Dispatch polymorphically with SELECT TYPE',
        ],
        prereq=['fortran-15-array-intrinsics'],
        refs=[dict(title='Fortran — Object Oriented', url='https://fortran-lang.org/learn/quickstart/object_oriented/'),
              dict(title='GCC — Type-bound Procedures', url='https://gcc.gnu.org/onlinedocs/gfortran/Type-bound-procedures.html')]),
    dict(
        slug='fortran-17-parallel',
        title='Parallel Programming',
        desc='OpenMP directives and Fortran coarrays.',
        diff='advanced',
        dur=30,
        objs=[
            'Write OpenMP parallel regions and worksharing',
            'Use reduction to accumulate across threads',
            'Explain coarray images and synchronization',
        ],
        prereq=['fortran-16-oop'],
        refs=[dict(title='OpenMP Specification', url='https://www.openmp.org/specifications/'),
              dict(title='GCC — Coarrays', url='https://gcc.gnu.org/onlinedocs/gfortran/Coarray-Programming.html')]),
    dict(
        slug='fortran-18-c-interop',
        title='C Interoperability',
        desc='ISO_C_BINDING, BIND(C), and mixed-language programs.',
        diff='advanced',
        dur=30,
        objs=[
            'Call C functions from Fortran',
            'Export Fortran procedures to C',
            'Pass pointers with c_loc and c_f_pointer',
        ],
        prereq=['fortran-17-parallel'],
        refs=[dict(title='Fortran — C Interop', url='https://fortran-lang.org/learn/quickstart/c_interop/'),
              dict(title='GCC — ISO_C_BINDING', url='https://gcc.gnu.org/onlinedocs/gfortran/ISO_005fC_005fBINDING.html')]),
    dict(
        slug='fortran-19-modern-features',
        title='Modern Fortran Features',
        desc='DO CONCURRENT, ASSOCIATE, implied-DO, elemental functions.',
        diff='advanced',
        dur=25,
        objs=[
            'Write data-parallel DO CONCURRENT loops',
            'Use ASSOCIATE for readable expressions',
            'Apply elemental functions to arrays',
        ],
        prereq=['fortran-18-c-interop'],
        refs=[dict(title='Fortran — DO CONCURRENT', url='https://gcc.gnu.org/onlinedocs/gfortran/DO-CONCURRENT.html'),
              dict(title='GCC — ASSOCIATE', url='https://gcc.gnu.org/onlinedocs/gfortran/ASSOCIATE.html')]),
    dict(
        slug='fortran-20-error-handling',
        title='Error Handling and Robust Code',
        desc='IOSTAT, ERROR STOP, STAT, and defensive programming.',
        diff='advanced',
        dur=25,
        objs=[
            'Handle I/O failures with IOSTAT',
            'Abort cleanly with ERROR STOP',
            'Check ALLOCATE failures with STAT',
        ],
        prereq=['fortran-19-modern-features'],
        refs=[dict(title='GCC — IOSTAT', url='https://gcc.gnu.org/onlinedocs/gfortran/IOSTAT.html'),
              dict(title='Fortran Best Practices', url='https://fortran-lang.org/en/learn/best_practices/')]),
    dict(
        slug='fortran-21-performance',
        title='Performance and Real-World Example',
        desc='Column-major order, INTENT, CPU_TIME, and MATMUL.',
        diff='advanced',
        dur=30,
        objs=[
            'Order loops for column-major arrays',
            'Measure runtime with CPU_TIME',
            'Exploit MATMUL over hand-written loops',
        ],
        prereq=['fortran-20-error-handling'],
        refs=[dict(title='Fortran Performance Tips', url='https://fortran-lang.org/en/learn/best_practices/'),
              dict(title='GCC — Optimization Options', url='https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'fortran', LESSONS, CODE, BASE)
