export class HolbertonClass {
  constructor(year, location) {
    this.year = year;
    this.location = location;
  }

  get year() {
    return this._year;
  }

  set year(value) {
    if (typeof value !== 'number') throw new TypeError('Year must be a number');
    this._year = value;
  }

  get location() {
    return this._location;
  }

  set location(value) {
    if (typeof value !== 'string') throw new TypeError('Location must be a string');
    this._location = value;
  }
}

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get firstName() {
    return this._firstName;
  }

  set firstName(value) {
    if (typeof value !== 'string') throw new TypeError('First name must be a string');
    this._firstName = value;
  }

  get lastName() {
    return this._lastName;
  }

  set lastName(value) {
    if (typeof value !== 'string') throw new TypeError('Last name must be a string');
    this._lastName = value;
  }

  get holbertonClass() {
    return this._holbertonClass;
  }

  set holbertonClass(value) {
    if (!(value instanceof HolbertonClass)) throw new TypeError('holbertonClass must be a HolbertonClass instance');
    this._holbertonClass = value;
  }

  get fullStudentDescription() {
    return `${this.fullName} - Holberton ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}

export const class2019 = new HolbertonClass(2019, 'San Francisco');
export const class2020 = new HolbertonClass(2020, 'San Francisco');

export const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
export const student2 = new StudentHolberton('John', 'Doe', class2020);
export const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
export const student4 = new StudentHolberton('Donald', 'Bush', class2019);
export const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export const listOfStudents = [student1, student2, student3, student4, student5];
