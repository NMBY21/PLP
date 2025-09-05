# Students & Courses CRUD (Node.js + Express + Sequelize)

This project implements a clean CRUD app with:
- **Students** (Create, Read, Update, Delete)
- **Courses**
- **Enrollments** (many-to-many relationship)

## Quick Start

```bash
git clone https://github.com/NMBY21/PLP/node-crud-students-courses.git
cd node-crud-students-courses
npm install
npm run dev   # runs with nodemon

API available at: http://localhost:3000

## Endpoints
    Students

        POST /students — create student

        GET /students — list students

        GET /students/:id — get one

        PATCH /students/:id — update

        DELETE /students/:id — delete

    Courses

        POST /courses

        GET /courses

        GET /courses/:id

        PATCH /courses/:id

        DELETE /courses/:id

    Enrollments

        POST /enrollments — enroll { studentId, courseId }

        DELETE /enrollments — unenroll { studentId, courseId }

## Tech

    Node.js, Express

    Sequelize ORM

    SQLite (default, swap with MySQL easily)