# CS-340
Welcome to the CS-340 repository!

## About the Course 
CS-340 focuses on client/server development using Python and MongoDB. The course emphasizes building database-driven applications, implementing secure data access layers, and developing interactive dashboards that rely on backend services. This course bridges backend database logic with frontend user interaction, simulating real-world full-stack development workflows.

Key topics in this course:
- MongoDB database design and document storage
- CRUD (Create, Read, Update, Delete) operations
- PyMongo integration
- Authentication and secure database access
- Seperation of concerns and modular design
- Interactive dashboards using Dash and Plotly
- Data filtering, aggregation, and visualization

## What You Will Find Here

This repository contains two major projects:
**Project One- Python CRUD Module**
- CRUD_Python_Module.py
- ProjectOneTestScript.ipynb
- CS 340 README Project 1.docx

In Project One, I developed a reusable Python class (AnimalShelter) that handles CRUD operations for the Austin Animal Center (AAC) Outcomes dataset stored in MongoDB.
The module:

- Authenticates securely using MongoDB credentials
- Connects to the aac database and animals collection
- Implements create(), read(), update(), and delete() methods
- Returns clean results usable by other applications

This module isolates database access logic, making it reusable, maintainable, and adaptable.

**Project Two- Grazioso Salvare Dashboard**
- ProjectTwoDashboard.ipynb
- CS 340 README Project 2.docx

Project Two builds a Dash-based interactive dashboard that connects to MongoDB only through the CRUD module developed in Project One.

The dashboard includes:
- Authentication through the CRUD module
- Interactive rescue-type filters (Water, Mountain/Wilderness, Disaster/Individual Tracking)
- Dynamic data table updates
- Geolocation mapping using Plotly
- Analytical chart visualization
- Reset functionality

All database communication is routed through the Python CRUD module, reinforcing modular architecture and separation of concerns.

## Why these Projects Matter

These projects simulate a real client scenario (Grazioso Salvare) and demonstrate how backend database services and frontend interfaces should interact in professional systems.

Instead of embedding raw database queries directly into the dashboard, I created a reusable access layer. This approach:
- Improves maintainability
- Increases security
- Simplifies debugging
- Allows scalability
- Reduces duplication of database logic

In industry environments, clean architecture and modular design are critical. This project reflects that structure.

## Reflection

**How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?**

(to be filled)

**How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?**

(to be filled)

**What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?**

(to be filled)

## Future Applications
(to be filled)
