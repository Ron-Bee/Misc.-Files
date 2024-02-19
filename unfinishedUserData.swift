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
    return "\(firstNames.randomElement()!) \(lastNames.randomElement()!)"
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
        let user = User(id: i, name: generateRandomName(), email: "\(generateRandomName().lowercased())@example.com")
        users.append(user)
    }

    let encoder = JSONEncoder()
    encoder.outputFormatting = .prettyPrinted // Optional: for readability

    if let jsonData = try? encoder.encode(users),
       let jsonString = String(data: jsonData, encoding: .utf8) {
        // Write the JSON string to a file (e.g., 'large_user_data.json')
        let fileURL = URL(fileURLWithPath: "large_user_data.json")
        try? jsonString.write(to: fileURL, atomically: true, encoding: .utf8)
    }
}

// Function to fetch user data (mocked for testing)
func fetchUserData() -> Data {
    if let url = Bundle.main.url(forResource: "userData", withExtension: "json") {
        return try! Data(contentsOf: url)
    } else {
        fatalError("Error: Could not find userData.json")
    }
}

// Function to read configuration
func readConfiguration() -> (Int, String)? {
    if let url = Bundle.main.url(forResource: "config", withExtension: "json") {
        do {
            let data = try Data(contentsOf: url)
            let decoder = JSONDecoder()
            let config = try decoder.decode(Config.self, from: data)
            return (config.fileSizeThreshold, config.largeFileStrategy)
        } catch {
            print("Error reading configuration: \(error)")
            return nil
        }
    } else {
        print("Error: Could not find config.json")
        return nil
    }
}

// Configuration struct
struct Config: Codable {
    let fileSizeThreshold: Int
    let largeFileStrategy: String
}

// Main processing logic
func processUserData() {
    let data = fetchUserData()

    if let (threshold, strategy) = readConfiguration() {
        if data.count > threshold {
            if strategy == "indexing" {
                // Implement indexing logic (TODO)
            } else if strategy == "definition" {
                // Implement definition logic (TODO)
            } else {
                print("Invalid strategy in configuration")
            }
        } else {
            // Process the data directly (using your original JSON decoding logic)
            do {
                let users = try JSONDecoder().decode([User].self, from: data)
                print(users)
            } catch {
                print("Error decoding JSON: \(error)")
            }
        }
    }
}

// Entry point
processUserData()