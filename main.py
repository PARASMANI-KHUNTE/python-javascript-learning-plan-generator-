import os

# Define the folder structure based on the provided timeline and topics
folder_structure = {
    "Month 1-Foundations": {
        "Week 1-2-Refresh Python Basics": ["Review basic Python syntax, data types, control structures, and functions.", "Complete small coding exercises and quizzes to reinforce concepts."],
        "Week 3-4-JavaScript Fundamentals": ["Review basic JavaScript syntax, data types, functions, and control structures.", "Practice DOM manipulation and event handling.", "Complete coding challenges on platforms like LeetCode or HackerRank."]
    },
    "Month 2-Intermediate Concepts": {
        "Week 1-2-Object-Oriented Programming (OOP)": ["Dive deeper into OOP concepts in Python and JavaScript.", "Learn about classes, objects, inheritance, polymorphism, etc.", "Implement OOP principles in small projects."],
        "Week 3-4-Asynchronous Programming and Frameworks": ["Explore asynchronous programming concepts in JavaScript (callbacks, promises, async/await).", "Start learning about popular JavaScript frameworks/libraries (React, Angular, Vue.js).", "Build a simple web application using one of the frameworks."]
    },
    "Month 3-Advanced Topics": {
        "Week 1-2-Advanced Python Concepts": ["Study advanced Python topics like generators, decorators, context managers, etc.", "Implement these concepts in practical projects or coding exercises."],
        "Week 3-4-Advanced JavaScript Concepts": ["Dive deeper into advanced JavaScript topics like closures, prototypes, ES6 features, etc.", "Practice functional programming concepts (higher-order functions, map/filter/reduce).", "Work on more complex projects using JavaScript."]
    },
    "Month 4-Specializations and Projects": {
        "Week 1-2-Data Science and Machine Learning (Python)": ["Learn about data science libraries like Pandas, NumPy, Matplotlib.", "Explore machine learning concepts using scikit-learn or TensorFlow.", "Work on a small data science project or Kaggle competition."],
        "Week 3-4-Full-Stack Development (JavaScript)": ["Dive deeper into your chosen JavaScript framework (React, Angular, Vue.js).", "Build a full-stack web application using Node.js for the backend and your chosen frontend framework.", "Focus on integrating backend/frontend components and handling HTTP requests."]
    },
    "Month 5-6-Special Projects and Refinement": {
        "Week 1-2-Advanced Web Development (JavaScript)": ["Learn about browser APIs, web sockets, and modern web development tools.", "Refactor and optimize your previous full-stack project.", "Explore additional JavaScript libraries or tools (e.g., Express.js for backend)."],
        "Week 3-4-Final Projects and Portfolio Building": ["Work on one or two larger projects that showcase your skills in both Python and JavaScript.", "Polish your projects, add documentation, and deploy them to showcase your work.", "Create a portfolio website to showcase your projects and skills."]
    }
}

# Function to create folder structure
def create_folder_structure(root, structure):
    for main_topic, subtopics in structure.items():
        main_topic_path = os.path.join(root, main_topic)
        os.makedirs(main_topic_path, exist_ok=True)
        for subtopic, details in subtopics.items():
            subtopic_path = os.path.join(main_topic_path, subtopic)
            os.makedirs(subtopic_path, exist_ok=True)
            for i, detail in enumerate(details, start=1):
                with open(os.path.join(subtopic_path, f"Detail_{i}.txt"), "w") as f:
                    f.write(detail)

# Create folder structure
root_folder = "Learning_Plan"
create_folder_structure(root_folder, folder_structure)
print("Folder structure created successfully!")
