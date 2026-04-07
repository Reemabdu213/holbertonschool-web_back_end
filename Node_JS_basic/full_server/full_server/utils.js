import fs from 'fs';

export function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = {};
      
      // نتخطى السطر الأول (Header) ونعالج باقي الأسطر
      lines.slice(1).forEach((line) => {
        if (line) {
          const [firstname, , , field] = line.split(',');
          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(firstname);
        }
      });
      resolve(students);
    });
  });
}
