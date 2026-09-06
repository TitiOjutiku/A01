from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing


def main() -> None:
    housing = fetch_california_housing(as_frame=True)
    output_path = Path(__file__).resolve().parent.parent / "figs" / "boxplot.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    housing.frame["MedInc"].plot(kind="box", figsize=(8, 6))
    plt.title("Boxplot of Median Income in California Housing")
    plt.ylabel("Median Income")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    main()