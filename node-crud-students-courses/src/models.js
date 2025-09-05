const { DataTypes } = require("sequelize");
const sequelize = require("./db");

// Student model
const Student = sequelize.define("Student", {
  fullName: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  email: {
    type: DataTypes.STRING,
    unique: true,
    allowNull: false,
  },
});

// Course model
const Course = sequelize.define("Course", {
  code: {
    type: DataTypes.STRING,
    unique: true,
    allowNull: false,
  },
  title: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  description: DataTypes.STRING,
});

// Many-to-Many relationship
const Enrollment = sequelize.define("Enrollment", {}, { timestamps: true });

Student.belongsToMany(Course, { through: Enrollment });
Course.belongsToMany(Student, { through: Enrollment });

module.exports = { sequelize, Student, Course, Enrollment };
