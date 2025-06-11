package main

import "fmt"

// Main function
func main() {
    // Variables
    var name string = "John"
    age := 25 // Short variable declaration

    // Constants
    const pi = 3.14

    // Print statements
    fmt.Println("Name:", name)
    fmt.Printf("Age: %d\n", age)
    fmt.Printf("Pi: %.2f\n", pi)

    // Conditional statements
    if age > 18 {
        fmt.Println("Adult")
    } else {
        fmt.Println("Minor")
    }

    // Loops
    for i := 1; i <= 5; i++ {
        fmt.Println("Iteration:", i)
    }

    // Functions
    result := add(10, 20)
    fmt.Println("Sum:", result)
}

// Function definition
func add(a int, b int) int {
    return a + b
}