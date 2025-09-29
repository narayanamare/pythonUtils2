import matplotlib.pyplot as plt
import numpy as np
import itertools

def curved_line(x0, y0, x1, y1, curvature=0.2, points=100, offset=0):
    """
    Draw a smooth curve between (x0, y0) and (x1, y1) using a quadratic Bézier curve.
    curvature > 0 → arch upwards, curvature < 0 → downwards
    offset → shifts the curve vertically to prevent overlaps
    """
    # Control point at midpoint, shifted up/down by curvature
    xm, ym = (x0 + x1) / 2, (y0 + y1) / 2
    ym += curvature * abs(x1 - x0) + offset

    t = np.linspace(0, 1, points)
    x = (1 - t)**2 * x0 + 2*(1 - t)*t * xm + t**2 * x1
    y = (1 - t)**2 * y0 + 2*(1 - t)*t * ym + t**2 * y1
    return x, y

def plot_storyline(characters, interactions, title="Storyline Visualization"):
    """
    characters: list of character names
    interactions: list of tuples (start_time, end_time, char1, char2)
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Assign fixed y-positions to each character
    y_positions = {name: i+1 for i, name in enumerate(characters)}

    # Draw character timelines
    for name, y in y_positions.items():
        ax.hlines(y, 0, max(i[1] for i in interactions)+1,
                  color="gray", linestyle="--", alpha=0.6)
        ax.text(-0.5, y, name, ha="right", va="center", fontsize=10, fontweight="bold")

    # Group interactions by (start, end) to avoid overlapping curves
    grouped = {}
    for start, end, a, b in interactions:
        grouped.setdefault((start, end), []).append((a, b))

    # Draw curved interactions
    for (start, end), pairs in grouped.items():
        # Offset curves slightly to separate multiple arcs between same times
        for idx, (a, b) in enumerate(pairs):
            y0, y1 = y_positions[a], y_positions[b]
            curvature = 0.3 if y0 < y1 else -0.3
            offset = (idx - len(pairs)/2) * 0.15  # small vertical separation
            x, y = curved_line(start, y0, end, y1, curvature=curvature, offset=offset)
            ax.plot(x, y, linewidth=2, alpha=0.8)

    # Style
    ax.set_xlim(0, max(i[1] for i in interactions)+1)
    ax.set_ylim(0, len(characters)+1)
    ax.set_xlabel("Time", fontsize=12)
    ax.set_ylabel("Characters", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_yticks([])  # Hide numeric Y ticks
    plt.tight_layout()
    plt.show()

# -------------------------
# Example usage
characters = ["Alice", "Bob", "Charlie", "Diana"]

interactions = [
    (1, 3, "Alice", "Bob"),
    (2, 5, "Bob", "Charlie"),
    (4, 6, "Alice", "Charlie"),
    (5, 7, "Charlie", "Diana"),
    (3, 7, "Alice", "Diana"),   # Overlaps with above → offset curve
]

plot_storyline(characters, interactions, title="Character Interactions Storyline")
