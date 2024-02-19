import Foundation

struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

// ... (functions for generating random data: generateRandomName, generateRandomDate, generateLargeJSONFile)

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