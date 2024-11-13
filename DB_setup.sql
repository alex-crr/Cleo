Create database Cleo_Brain;
Use Cleo_brain;
CREATE TABLE Persons (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- Inherited table for stakeholders
CREATE TABLE Stakeholders (
    stakeholder_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    role VARCHAR(100), -- Specific to stakeholders
    organization VARCHAR(100), -- Specific to stakeholders
    FOREIGN KEY (person_id) REFERENCES Persons(person_id) ON DELETE CASCADE
);

CREATE TABLE ProjectTypes (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Table: Projects
CREATE TABLE Projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type_id INT,
    scope TEXT,
    start_date DATE,
    end_date DATE,
    status ENUM('Not Started', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Not Started',
    progress_percentage INT DEFAULT 0,
    priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES ProjectTypes(type_id) ON DELETE SET NULL
);

CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT,
    task_name VARCHAR(100) NOT NULL,
    description TEXT,
    assigned_to VARCHAR(100),
    status ENUM('Not Started', 'In Progress', 'Completed', 'Blocked') DEFAULT 'Not Started',
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);