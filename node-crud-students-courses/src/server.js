const express = require("express");
const { sequelize } = require("./models");

const studentsRouter = require("./routes/students");
const coursesRouter = require("./routes/courses");
const enrollmentsRouter = require("./routes/enrollments");

const app = express();
app.use(express.json());

app.get("/", (_req, res) => {
  res.json({ status: "ok", docs: "Use /students /courses /enrollments" });
});

app.use("/students", studentsRouter);
app.use("/courses", coursesRouter);
app.use("/enrollments", enrollmentsRouter);

// Sync database and start server
const PORT = 3000;
sequelize.sync().then(() => {
  console.log("Database synced");
  app.listen(PORT, () =>
    console.log(`Server running at http://localhost:${PORT}`)
  );
});
