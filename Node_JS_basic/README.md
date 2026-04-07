# Node.js Project

A comprehensive introduction to Node.js covering core modules, Express.js, Babel, and Nodemon.

## Learning Objectives

- Run JavaScript using NodeJS
- Use NodeJS modules
- Use specific Node JS module to read files
- Use `process` to access command line arguments and the environment
- Create a small HTTP server using Node JS
- Create a small HTTP server using Express JS
- Create advanced routes with Express JS
- Use ES6 with Node JS with Babel-node
- Use Nodemon to develop faster

## Requirements

- Ubuntu 20.04 LTS
- Node.js version 20.x.x
- All files use the `.js` extension

## Setup

```bash
$ npm install
```

## Running Tests

```bash
$ npm run test
```

## Full Test (lint + tests)

```bash
$ npm run full-test
```

## Tasks

### Task 0 — Executing basic JavaScript with Node JS
`0-console.js` — Prints a string argument to STDOUT.

### Task 1 — Using Process stdin
`1-stdin.js` — Reads from stdin and prints to stdout.

### Task 2 — Reading a file synchronously with Node JS
`2-read_file.js` — Reads `database.csv` synchronously and counts students by field.

### Task 3 — Reading a file asynchronously with Node JS
`3-read_file_async.js` — Reads `database.csv` asynchronously and returns a Promise.

### Task 4 — Create a small HTTP server using Node's HTTP module
`4-http.js` — Simple HTTP server on port 1245.

### Task 5 — Create a more complex HTTP server using Node's HTTP module
`5-http.js` — HTTP server that reads from `database.csv` and serves student data.

### Task 6 — Create a small HTTP server using Express
`6-http_express.js` — Simple Express server on port 1245.

### Task 7 — Create a more complex HTTP server using Express
`7-http_express.js` — Express server with multiple routes serving student data.

### Task 8 — Organize a complex HTTP server using Express
`8-http_express/` — A full MVC-style Express app with controllers and routes.

## Files

| File | Description |
|------|-------------|
| `database.csv` | Student data (firstname, lastname, age, field) |
| `package.json` | NPM configuration |
| `babel.config.js` | Babel transpiler configuration |
| `.eslintrc.js` | ESLint linting rules |
