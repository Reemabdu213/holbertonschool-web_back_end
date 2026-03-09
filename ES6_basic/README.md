# ES6 Basics

A project exploring ECMAScript 6 (ES2015) features and syntax.

## Learning Objectives

By the end of this project, you should be able to explain:

- What ES6 is and its new features
- The difference between `const` and `let` (vs `var`)
- Block-scoped variables
- Arrow functions and default parameters
- Rest and spread function parameters
- String templating (template literals)
- Object creation and shorthand properties in ES6
- Iterators and `for-of` loops

## Requirements

- Node 20.x.x
- npm 9.x.x
- All files use the `.js` extension
- Tested with Jest
- Linted with ESLint

## Setup

```bash
# Install dependencies
npm install

# Run tests
npm test

# Run linter
npm run lint

# Run linter + tests
npm run full-test
```

## Configuration Files

| File | Purpose |
|------|---------|
| `package.json` | Project dependencies and scripts |
| `babel.config.js` | Babel transpiler configuration |
| `.eslintrc.js` | ESLint linting rules |

## Key ES6 Features Covered

### `const` and `let`
Block-scoped variable declarations replacing `var`.

### Arrow Functions
```js
const add = (a, b) => a + b;
```

### Default Parameters
```js
function greet(name = 'World') { return `Hello, ${name}!`; }
```

### Rest Parameters
```js
function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }
```

### Spread Operator
```js
const merged = [...arr1, ...arr2];
```

### Template Literals
```js
const msg = `Hello, ${name}!`;
```

### Iterators & for-of
```js
for (const item of iterable) { console.log(item); }
```
