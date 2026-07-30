---
{
  "title": "TypeScript with React",
  "description": "Type React components with proper prop interfaces",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Type React components with proper prop interfaces",
    "Use generic components for polymorphic props",
    "Type hooks: useState, useReducer, useContext",
    "Type event handlers and refs correctly"
  ],
  "knowledge_refs": [
    "typescript/ts-18-react-typescript"
  ],
  "prerequisites": [
    "TS-08",
    "TS-04"
  ],
  "references": [
    {
      "title": "React TypeScript Cheatsheet",
      "url": "https://react-typescript-cheatsheet.netlify.app/"
    },
    {
      "title": "TS Handbook — JSX",
      "url": "https://www.typescriptlang.org/docs/handbook/jsx.html"
    },
    {
      "title": "React Docs — TypeScript",
      "url": "https://react.dev/learn/typescript"
    }
  ]
}
---

# TS-18-REACT-TYPESCRIPT: TypeScript with React

## Introduction

TypeScript enhances React development by catching prop errors, hook misuse, and event handler mismatches at compile time. Properly typed React components are self-documenting and reduce runtime bugs significantly.

## Key Concepts

### 1. Typing Component Props

Use `interface` for props (benefits from declaration merging). Use `React.FC` sparingly — it adds `children` implicitly. Prefer explicit children typing. Leverage `React.ComponentProps<T>` for wrapping native elements.

```typescript
// Best practice: explicit props interface
interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary' | 'danger';
  disabled?: boolean;
  loading?: boolean;
  onClick: (event: React.MouseEvent<HTMLButtonElement>) => void;
  children?: React.ReactNode;
}

function Button({ label, variant = 'primary', disabled, loading, onClick, children }: ButtonProps) {
  return (
    <button
      disabled={disabled || loading}
      onClick={onClick}
      className={`btn btn-${variant}`}
    >
      {loading ? 'Loading...' : children || label}
    </button>
  );
}

// Wrapping native elements with component props
interface InputProps extends React.ComponentPropsWithoutRef<'input'> {
  label: string;
  error?: string;
}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, ...props }, ref) => (
    <div>
      <label>{label}</label>
      <input ref={ref} {...props} />
      {error && <span className='error'>{error}</span>}
    </div>
  )
);
```

### 2. Generic Components — Polymorphic Props

Generic components let the caller specify the type. Common patterns include `Select<T>`, `List<T>`, and polymorphic `as` props that change the rendered element while preserving type safety.

```typescript
// Generic list component
interface ListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => React.ReactNode;
  keyExtractor: (item: T) => string;
}

function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={keyExtractor(item)}>{renderItem(item, index)}</li>
      ))}
    </ul>
  );
}

// Usage — type inferred from items
<List
  items={[{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }]}
  keyExtractor={(user) => String(user.id)}
  renderItem={(user) => <span>{user.name}</span>}
/>

// Polymorphic 'as' prop
interface TypographyProps<T extends React.ElementType> {
  as?: T;
  children: React.ReactNode;
}

function Typography<T extends React.ElementType = 'p'>({ as, children }: TypographyProps<T>) {
  const Component = as || 'p';
  return <Component>{children}</Component>;
}

// <Typography as='h1'>Heading</Typography> — renders <h1>
```

### 3. Typing Hooks: useState, useReducer, useContext

TypeScript infers hook types from initial values. For complex state, provide explicit generic parameters. `useReducer` benefits from discriminated union actions.

```typescript
// useState — inference from initial value
const [count, setCount] = useState(0);           // number
const [name, setName] = useState('');              // string
const [user, setUser] = useState<User | null>(null); // explicit union

// useReducer with discriminated union
type Action =
  | { type: 'increment'; amount: number }
  | { type: 'decrement'; amount: number }
  | { type: 'reset' };

interface CounterState {
  value: number;
  lastAction: string;
}

function counterReducer(state: CounterState, action: Action): CounterState {
  switch (action.type) {
    case 'increment':
      return { value: state.value + action.amount, lastAction: 'increment' };
    case 'decrement':
      return { value: state.value - action.amount, lastAction: 'decrement' };
    case 'reset':
      return { value: 0, lastAction: 'reset' };
    default:
      const _exhaustive: never = action;
      return state;
  }
}

// useContext with custom hook
interface ThemeContextType {
  theme: 'light' | 'dark';
  toggleTheme: () => void;
}
const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

function useTheme(): ThemeContextType {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error('useTheme must be used inside ThemeProvider');
  return ctx;
}
```

### 4. Event Handlers and Refs

React event types are parameterized generics: `React.ChangeEvent<HTMLInputElement>`, `React.FormEvent<HTMLFormElement>`. Refs use `useRef<T>` with union types for mutable vs immutable refs.

```typescript
// Typed event handlers
function Form() {
  const [value, setValue] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('Submitted:', value);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      console.log('Enter pressed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={value} onChange={handleChange} onKeyDown={handleKeyDown} />
    </form>
  );
}

// Typed refs
function AutoFocusInput() {
  const inputRef = useRef<HTMLInputElement>(null);  // mutable ref

  useEffect(() => {
    // null check required because ref could be null
    inputRef.current?.focus();
  }, []);

  return <input ref={inputRef} />;
}

// Callback ref for dynamic ref assignment
function MeasuredDiv() {
  const [width, setWidth] = useState(0);
  const measuredRef = useCallback((node: HTMLDivElement | null) => {
    if (node !== null) {
      setWidth(node.getBoundingClientRect().width);
    }
  }, []);

  return <div ref={measuredRef}>Width: {width}px</div>;
}
```

### 5. Higher-Order Components and Render Props

HOCs and render props benefit from generics. A typed HOC preserves the wrapped component's props while adding new ones. Render props use generic interfaces to type the children function.

```typescript
// Typed HOC — adds loading state
interface WithLoadingProps {
  loading: boolean;
}

function withLoading<T extends object>(
  Component: React.ComponentType<T & { loading: boolean }>
) {
  return function WrappedComponent(props: T) {
    const [loading, setLoading] = useState(false);
    return <Component {...props} loading={loading} />;
  };
}

// Typed render props
interface DataFetcherProps<T> {
  url: string;
  children: (state: AsyncState<T>) => React.ReactNode;
}

function DataFetcher<T>({ url, children }: DataFetcherProps<T>) {
  const [state, setState] = useState<AsyncState<T>>({ status: 'loading' });

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(data => setState({ status: 'success', data, timestamp: Date.now() }))
      .catch(error => setState({ status: 'error', error }));
  }, [url]);

  return <>{children(state)}</>;
}

// Usage
<DataFetcher<User[]> url='/api/users'>
  {(state) => {
    if (state.status === 'loading') return <Spinner />;
    if (state.status === 'error') return <Error msg={state.error.message} />;
    return <UserList users={state.data} />;
  }}
</DataFetcher>
```

## Practice Questions

1. Why is `React.FC` often discouraged for component typing? What alternative is preferred?
1. How do generic components with `T extends unknown[]` enable type-safe list rendering?
1. What is the type of `event.target.value` in an `onChange` handler for `<input type="checkbox">` vs `<input type="text">`?
1. Write a typed HOC that adds authentication check to any component.

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript with React: typing props, state, events, and refs comprehensively"
1. "Show me generic React component patterns for polymorphic and data-fetching components"
1. "Teach me typed HOC and render props patterns in TypeScript React"

## Key Takeaways

- Use explicit prop interfaces instead of `React.FC` for better type safety
- Generic components enable type-safe reusable patterns like `<List<T>>`
- useReducer with discriminated union actions ensures exhaustive case handling
