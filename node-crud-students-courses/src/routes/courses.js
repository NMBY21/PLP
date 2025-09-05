const express = require("express");
const router = express.Router();
const { Course } = require("../models");

// Create
router.post("/", async (req, res) => {
  try {
    const course = await Course.create(req.body);
    res.status(201).json(course);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// List
router.get("/", async (_req, res) => {
  const courses = await Course.findAll();
  res.json(courses);
});

// Get one
router.get("/:id", async (req, res) => {
  const course = await Course.findByPk(req.params.id);
  if (!course) return res.status(404).json({ error: "Not found" });
  res.json(course);
});

// Update
router.patch("/:id", async (req, res) => {
  const course = await Course.findByPk(req.params.id);
  if (!course) return res.status(404).json({ error: "Not found" });
  await course.update(req.body);
  res.json(course);
});

// Delete
router.delete("/:id", async (req, res) => {
  const course = await Course.findByPk(req.params.id);
  if (!course) return res.status(404).json({ error: "Not found" });
  await course.destroy();
  res.status(204).end();
});

module.exports = router;
