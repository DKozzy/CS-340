# CS-340
Welcome to the CS-340 repository! This repository contains projects I developed as part of the CS-340 Client/Server Development course at Southern New Hampshire University. This course focused on building database-driven applications using Python and MongoDB, emphasizing secure data access, modular architecture, and interactive dashboard development. The work in this repository demonstrates the integration of backend database systems with frontend client interfaces through a structured, reusable CRUD design.

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

In Project One, I developed a reusable Python class (AnimalShelter) that handles CRUD operations for the Austin Animal Center (AAC) Outcomes dataset stored in MongoDB. This module isolates database access logic, making it reusable, maintainable, and adaptable.
The module:

- Authenticates securely using MongoDB credentials
- Connects to the aac database and animals collection
- Implements create(), read(), update(), and delete() methods
- Returns clean results usable by other applications

**Project Two- Grazioso Salvare Dashboard**
- ProjectTwoDashboard.ipynb
- CS 340 README Project 2.docx

Project Two builds a Dash-based interactive dashboard that connects to MongoDB only through the CRUD module developed in Project One. All database communication is routed through the Python CRUD module, reinforcing modular architecture and separation of concerns.

The dashboard includes:
- Authentication through the CRUD module
- Interactive rescue-type filters (Water, Mountain/Wilderness, Disaster/Individual Tracking)
- Dynamic data table updates
- Geolocation mapping using Plotly
- Analytical chart visualization
- Reset functionality

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

Separation of responsibility is necessary in order to write maintainable and adaptable programs. Project one has a special CRUD module that separates the operations of the database with the other components of the application. Rather than integrating MongoDB logic into the dashboard code, I put all the database interactions in a reusable class. This helped make Project Two much easier to construct. The dashboard just invokes functions such as read without giving thought to connection strings, authentication sources or update logic. In case the database credentials are modified, or some validation is required in the future, the changes are merely required to occur within the CRUD module. The great benefit of this design is the reusability. This CRUD module may be applicable in a web application of the future, a mobile interface, a REST API, or any other system based on Python and requires access to the same dataset. It gives a base on which it can grow even beyond this assignment.

**How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?**

As I went about the Grazioso Salvare requirements, I started by trying to learn the data structure and the client objectives. This client required filtered types of rescue, visualization and interactive response. That is to say that the database queries were to accommodate efficient filtering and dynamic updating. This project had a different approach to other programming tasks that were limited by either algorithms or object-oriented concepts: this project was necessary to think about the architecture of the system. I needed to be aware of database authentication, connection management, modular structure, and frontend-backend logic interaction.

When creating databases in response to client requests in the future, I would:

- Standardize data where it is necessary
- Expect filtering and aggregation requirements
- Performance design indexes
- Seperate database logic and presentation logic
- Plan for scalability prior to implementation

To me, this project supported the significance of architecture first before writing code.

**What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?**

Computer scientists come up with systems that are effective and dependable in solving real-life problems. The system in this project enables Grazioso Salvare to filter and analyse animal rescue data fast to make operational decisions. The dashboard offers a better alternative to scanning spreadsheets or raw data files manually, in the sense that it offers:

- Instant filtering
- Real-time visualization
- Location mapping
- Organized data representation

This enhances quickness when making decisions and minimizes human error. In the context of an organization that organizes efforts to rescue, it is a direct influence on the resource distribution and response time. Such projects are important as they are used to convert raw data into useful information.

## Future Applications

There are several possible improvements and extensions to this project:

- Multi-breed normalization to resolve inconsistent breed labeling
- Additional aggregation pipelines for advanced reporting
- Pagination and sorting controls for large datasets
- Deployment as a standalone web application
- REST API layer built on top of the CRUD module
- Role-based authentication and access control

The CRUD architecture already supports these enhancements without requiring structural redesign.
