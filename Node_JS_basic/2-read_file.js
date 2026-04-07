const fs = require('fs');

const countStudents = (path) => {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.trim().split('\n');
  const students = lines.slice(1).filter((line) => line.trim() !== '');

  console.log(`Number of students: ${students.length}`);

  const fields = {};
  students.forEach((student) => {
    const [firstname, , , field] = student.split(',');
    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstname);
  });

  Object.entries(fields).forEach(([field, names]) => {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  });
};

module.exports = countStudents;
