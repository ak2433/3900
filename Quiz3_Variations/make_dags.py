"""Draws the Q3 DAG for each quiz variation into images/."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

OUT = Path(__file__).resolve().parent / "images"
OUT.mkdir(exist_ok=True)
GREY, RED, BLUE, GOLD = "#7f7f7f", "#d95f4e", "#4393c3", "#d4a017"
R = 0.32


def draw(name, c1, c2, a, y, mediator=None):
    nodes = {"c1": (0, 2, *c1, "above", GREY), "c2": (3, 2, *c2, "above", GREY),
             "a": (0, 0, *a, "below", RED), "y": (3, 0, *y, "below", BLUE)}
    edges = [("c1", "a"), ("c1", "y"), ("c2", "a"), ("c2", "y"), ("a", "y")]
    if mediator:
        nodes["a"] = (0, 0, *a, "left", RED)
        nodes["y"] = (3, 0, *y, "right", BLUE)
        nodes["m"] = (1.5, -1.2, *mediator, "below", GOLD)
        edges += [("a", "m"), ("m", "y")]
    fig, ax = plt.subplots(figsize=(6, 4.6 if mediator else 4))
    for s, t in edges:
        (x1, y1), (x2, y2) = nodes[s][:2], nodes[t][:2]
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=22, lw=2.5,
                                     color="black", shrinkA=26, shrinkB=28))
    for x, yy, letter, cap, pos, col in nodes.values():
        ax.add_patch(Circle((x, yy), R, facecolor=col, edgecolor="black", lw=2, zorder=3))
        ax.text(x, yy, letter, ha="center", va="center", color="white", fontsize=16, weight="bold", zorder=4)
        if pos in ("left", "right"):
            dx = -0.45 if pos == "left" else 0.45
            ax.text(x + dx, yy, cap, ha="right" if pos == "left" else "left", va="center", fontsize=14)
        else:
            ax.text(x, yy + (0.55 if pos == "above" else -0.6), cap, ha="center", va="center", fontsize=14)
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1.9 if mediator else -1, 2.8)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(OUT / name, dpi=110, bbox_inches="tight", facecolor="white")
    plt.close(fig)


draw("v1_dag.png", ("G", "Prior GPA"), ("P", "Parental income"), ("A", "Tutoring"), ("Y", "Exam score"))
draw("v2_dag.png", ("G", "Age"), ("B", "BMI"), ("A", "Exercise program"), ("Y", "Blood pressure"))
draw("v3_dag.png", ("N", "Neighborhood"), ("P", "Parent education"), ("A", "After-school program"),
     ("Y", "Test score"), mediator=("H", "Homework hours"))
draw("v4_dag.png", ("D", "Distance to hospital"), ("S", "Insurance status"), ("A", "New surgery"),
     ("Y", "Recovery time"))
