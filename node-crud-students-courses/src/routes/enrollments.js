const express = require("express");
const router = express.Router();
const { Student, Course } = require("../models");

// Enroll student in course
router.post("/", async (req, res) => {
  const { studentId, courseId } = req.body;
  try {
    const student = await Student.findByPk(studentId);
    const course = await Course.findByPk(courseId);
    if (!student || !course)
      return res.status(404).json({ error: "Student or Course not found" });

    await student.addCourse(course);
    res.status(201).json({ studentId, courseId });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Unenroll
router.delete("/", async (req, res) => {
  const { studentId, courseId } = req.body;
  const student = await Student.findByPk(studentId);
  const course = await Course.findByPk(courseId);
  if (!student || !course)
    return res.status(404).json({ error: "Student or Course not found" });

  await student.removeCourse(course);
  res.status(204).end();
});

module.exports = router;
