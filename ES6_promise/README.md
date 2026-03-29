# ES6 Promises

## Description

This project covers JavaScript Promises and asynchronous programming using ES6 features including:
- Promises (how, why, and what)
- `then`, `resolve`, `catch` methods
- Every method of the Promise object
- Throw / Try
- The `await` operator
- `async` functions

## Requirements

- Ubuntu 20.04 LTS
- Node.js 20.x.x
- npm 9.x.x
- Jest for testing
- Babel for transpilation
- ESLint for linting

## Setup

Install dependencies:

```bash
npm install
```

## Usage

Run tests:
```bash
npm run test
```

Run full test (lint + tests):
```bash
npm run full-test
```

## Learning Objectives

- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The `await` operator
- How to use an `async` function

## Files

| File | Description |
|------|-------------|
| `0-promise.js` | Returns a basic Promise |
| `1-promise.js` | Returns a resolved or rejected Promise based on a boolean |
| `2-then.js` | Handles Promise response with then, catch, and finally |
| `3-all.js` | Handles multiple promises with Promise.all |
| `4-user-promise.js` | Returns a resolved Promise with user data |
| `5-photo-reject.js` | Returns a rejected Promise with an error message |
| `6-final-user.js` | Handles multiple promises with Promise.allSettled |
| `7-load_balancer.js` | Returns the first resolved Promise using Promise.race |
| `8-try.js` | Throws an error when dividing by zero |
| `9-try.js` | Handles errors using try/catch/finally |
