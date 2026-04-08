const fs = require('fs');

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(err);
      return;
    }
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    const result = {};
    for (const student of students) {
      const fields = student.split(',');
      if (fields.length < 4) continue;
      const firstname = fields[0].trim();
      const field = fields[3].trim();
      if (!result[field]) {
        result[field] = [];
      }
      result[field].push(firstname);
    }
    resolve(result);
  });
});

module.exports = readDatabase;
