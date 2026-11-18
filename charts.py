from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Load employee data from the script's folder.
folder = Path(__file__).resolve().parent
employees = pd.read_csv(folder / "employees.csv")
employees.columns = employees.columns.str.strip().str.lower()

employees["department"] = employees["department"].str.strip()
employees["id"] = pd.to_numeric(employees["id"], errors="raise")
employees["salary"] = pd.to_numeric(employees["salary"], errors="raise")

required = ["id", "department", "salary"]
if employees.empty or employees[required].isna().any().any():
    raise ValueError("Employee data must contain rows with id, department and salary.")

# Save all charts in a charts folder.
output = folder / "charts"
output.mkdir(exist_ok=True)


def save_chart(fig, filename):
    fig.tight_layout()
    fig.savefig(output / filename, dpi=300, bbox_inches="tight")
    plt.close(fig)


# 1. Bar chart: average salary per department
average_salary = employees.groupby("department")["salary"].mean()

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(
    average_salary.index,
    average_salary.values,
    color="steelblue",
)
ax.bar_label(bars, labels=[f"{v:,.2f}" for v in average_salary], padding=4)
ax.set_title("Average Salary per Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")
ax.tick_params(axis="x", labelrotation=20)
ax.margins(y=0.15)
save_chart(fig, "average_salary_by_department.png")


# 2. Histogram: salary distribution with exactly 5 bins
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(employees["salary"], bins=5, color="teal", edgecolor="black")
ax.set_title("Salary Distribution")
ax.set_xlabel("Salary")
ax.set_ylabel("Number of Employees")
ax.yaxis.get_major_locator().set_params(integer=True)
save_chart(fig, "salary_histogram.png")


# 3. Scatter plot: employee ID vs salary, coloured by department
departments = sorted(employees["department"].unique())
colours = plt.get_cmap("tab20", max(len(departments), 1))

fig, ax = plt.subplots(figsize=(9, 5))
for index, department in enumerate(departments):
    group = employees[employees["department"] == department]
    ax.scatter(
        group["id"],
        group["salary"],
        color=colours(index),
        label=department,
        s=65,
        edgecolors="black",
        linewidths=0.5,
    )

ax.set_title("Employee Salary by Department")
ax.set_xlabel("Employee ID")
ax.set_ylabel("Salary")
ax.legend(title="Department", bbox_to_anchor=(1.02, 1), loc="upper left")
save_chart(fig, "id_vs_salary.png")


# 4. Line chart: monthly sales with markers
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(months, sales, marker="o", linewidth=2, color="darkorange")
ax.set_title("Monthly Sales: January–June")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.grid(axis="y", alpha=0.3)
save_chart(fig, "monthly_sales.png")

print(f"Saved all four PNG charts to: {output}")