import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import seaborn as sns

#   Load and clean data
df = pd.read_csv("books_data.csv")
df["Price"] = df["Price"].astype(str).str.replace(r"[^\d.]", "", regex=True).astype(float)
sns.set(style="whitegrid")

#   Create initial figure and axis (will be reused)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

#   Mutable index tracker
current_index = [0]

#   Plotting functions with custom figure sizes
def show_rating_distribution():
    fig.set_size_inches(7, 4)  # Width x Height
    ax.clear()
    sns.countplot(x="Rating", data=df, palette="viridis", ax=ax)
    ax.set_title("⭐ Rating Distribution")
    ax.set_xlabel("Rating (1–5 Stars)")
    ax.set_ylabel("Number of Books")
    fig.suptitle("1/4", fontsize=10)
    update_buttons()
    fig.canvas.draw_idle()

def show_price_distribution():
    fig.set_size_inches(8, 5)
    ax.clear()
    sns.histplot(df["Price"], bins=25, kde=True, color="skyblue", ax=ax)
    ax.set_title("💰 Book Price Distribution")
    ax.set_xlabel("Price (£)")
    ax.set_ylabel("Number of Books")
    fig.suptitle("2/4", fontsize=10)
    update_buttons()
    fig.canvas.draw_idle()

def show_top_expensive_books():
    fig.set_size_inches(10, 6)
    ax.clear()
    top_books = df.sort_values(by="Price", ascending=False).head(10)
    sns.barplot(y="Title", x="Price", data=top_books, palette="rocket", ax=ax)
    ax.set_title("🏆 Top 10 Most Expensive Books")
    ax.set_xlabel("Price (£)")
    ax.set_ylabel("Book Title")
    fig.suptitle("3/4", fontsize=10)
    fig.tight_layout(rect=[0, 0.15, 1, 0.95])
    update_buttons()
    fig.canvas.draw_idle()

def show_avg_price_by_rating():
    fig.set_size_inches(7, 4.5)
    ax.clear()
    avg_price_rating = df.groupby("Rating")["Price"].mean().reset_index()
    sns.barplot(x="Rating", y="Price", data=avg_price_rating, palette="mako", ax=ax)
    ax.set_title(" Average Price by Rating")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Average Price (£)")
    fig.suptitle("4/4", fontsize=10)
    update_buttons()
    fig.canvas.draw_idle()

#   List of plots
plots = [
    show_rating_distribution,
    show_price_distribution,
    show_top_expensive_books,
    show_avg_price_by_rating
]

#   Button click handlers
def next_plot(event):
    if current_index[0] < len(plots) - 1:
        current_index[0] += 1
        plots[current_index[0]]()

def prev_plot(event):
    if current_index[0] > 0:
        current_index[0] -= 1
        plots[current_index[0]]()

#   Show/hide buttons based on current graph
def update_buttons():
    # Show/hide "Back"
    btn_back.ax.set_visible(current_index[0] > 0)
    # Show/hide "Next"
    btn_next.ax.set_visible(current_index[0] < len(plots) - 1)
    fig.canvas.draw_idle()

#   Create navigation buttons
ax_back = plt.axes([0.7, 0.05, 0.1, 0.05])
btn_back = Button(ax_back, "⬅️ Back")
btn_back.on_clicked(prev_plot)

ax_next = plt.axes([0.81, 0.05, 0.1, 0.05])
btn_next = Button(ax_next, "Next ➡️")
btn_next.on_clicked(next_plot)

#   Show first graph
plots[0]()

plt.show()
