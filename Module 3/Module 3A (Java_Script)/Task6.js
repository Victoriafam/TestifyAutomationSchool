// This program prints the name of the triangle based on the length of the sides
// in relation to one another.

const side1 = 5
const side2 = 5
const side3 = 5

if (side1===side2 && side2===side3 && side3===side1) {
    console.log('Equilateral triangle')
    } else if (side1 === side2 ||  side1 === side3 || side2 === side3) {
        console.log('Isosceles triangle')
    } else {
        console.log('Scalene triangle')

    }
