import Foundation

struct User: Codable {
let id: Int
let name: String
let email: String
}

// ... (functions for generating random data: generateRandomName, generateRandomDate)

// Function to generate a large JSON file
func generateLargeJSONFile(numberOfUsers: Int) {
// ... (same as before)
}

// Example usage (generate a file with 1000 users)
generateLargeJSONFile(numberOfUsers: 1000)

Combine these two scripts into one with a copy/paste mindset to its creation. If necessary, make changes for the sake of efficiency but nothing to compromise the testing I have yet to implement. It is important to have a solid script that produces varying sized JSON files for User Data Processing. Try to write the JSON string to a file (e.g., 'large_user_data.json')

import Foundation

struct User: Codable {
let id: Int
let name: String
let email: String
}

// Function to generate a random name
func generateRandomName() -> String {
let firstNames = ["Alice", "Bob", "Charlie", "David", "Emily"]
let lastNames = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
return "(firstNames.randomElement()!) (lastNames.randomElement()!)"
}

// Function to generate a random date
func generateRandomDate() -> Date {
let today = Date()
let earliestDate = Calendar.current.date(byAdding: .year, value: -50, to: today)!
let timeInterval = earliestDate.timeIntervalSinceReferenceDate + Double.random(in: 0...86400 * 365 * 50) // 50 years
return Date(timeIntervalSinceReferenceDate: timeInterval)
}

// Function to generate a large JSON file (optional)
func generateLargeJSONFile(numberOfUsers: Int) {
var users: [User] = []
for i in 1...numberOfUsers {
let user = User(id: i, name: generateRandomName(), email: "(generateRandomName().lowercased())@example.com")
users.append(user)
}
let encoder = JSONEncoder()
encoder.outputFormatting = .prettyPrinted // Optional: for readability

if let jsonData = try? encoder.encode(users),
   let jsonString = String(data: jsonData, encoding: .utf8) {
    // Write the JSON string to a file (e.g., 'large_user_data.json')
    let fileURL = URL(fileURLWithPath: "large_user_data.json")
    try? jsonString.write(to: fileURL, atomically: true, encoding: .utf8)