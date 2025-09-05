const express = require("express");
const router = express.Router();
const { Student } = require("../models");

// Create student
router.post("/", async (req, res) => {
  try {
    const student = await Student.create(req.body);
    res.status(201).json(student);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// List all
router.get("/", async (_req, res) => {
  const students = await Student.findAll();
  res.json(students);
});

// Get by id
router.get("/:id", async (req, res) => {
  const student = await Student.findByPk(req.params.id);
  if (!student) return res.status(404).json({ error: "Not found" });
  res.json(student);
});

// Update
router.patch("/:id", async (req, res) => {
  const student = await Student.findByPk(req.params.id);
  if (!student) return res.status(404).json({ error: "Not found" });
  await student.update(req.body);
  res.json(student);
});

// Delete
router.delete("/:id", async (req, res) => {
  const student = await Student.findByPk(req.params.id);
  if (!student) return res.status(404).json({ error: "Not found" });
  await student.destroy();
  res.status(204).end();
});

module.exports = router;
