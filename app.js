const people = [
  { nombre: "Juan", edad: 25, ciudad: "Madrid" },
  { nombre: "Carlos", edad: 30, ciudad: "Barcelona" },
  { nombre: "Franz", edad: 28, ciudad: "Valencia" },
  { nombre: "Cinthia", edad: 27, ciudad: "Sevilla" },
  { nombre: "Samira", edad: 26, ciudad: "Malaga" },
];

const filterPeople = people.filter((person) => person.edad > 25);
console.log(filterPeople);
