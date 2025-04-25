import polars as pl
import argparse


def main():
    parser = argparse.ArgumentParser(
        usage="A simple program to see how mid you are in FIDE"
    )
    parser.add_argument("id", type=int, help="FIDE id")
    parser.add_argument(
        "--filename",
        type=str,
        default="data/players.csv",
        help="Path to the input CSV file (default: data/players.csv)",
    )

    args = parser.parse_args()

    df = pl.read_csv(args.filename, has_header=True, infer_schema_length=1000)
    cols = ["rating", "rapid_rating", "blitz_rating"]
    player = df.filter(pl.col("id") == args.id).select(
        pl.col("id"), pl.col("name"), *map(pl.col, cols)
    )
    print(player)

    p = [(col, pl.col(col), player.select(col).item()) for col in cols]

    print(
        pl.DataFrame(
            dict(
                (
                    f"percentile({name})",
                    df.filter(x > 0).select(x <= v).cast(pl.Int8).mean().item() * 100,
                )
                for name, x, v in p
            )
        )
    )


if __name__ == "__main__":
    main()
