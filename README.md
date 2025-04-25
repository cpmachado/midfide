# midfide

A simple tool using the latest fide ratings using
[gelo](https://github.com/cpmachado/gelo) to check how mid you are.

```shell
python main.py 1961039
```

```text
shape: (1, 5)
┌─────────┬───────────────────────────┬────────┬──────────────┬──────────────┐
│ id      ┆ name                      ┆ rating ┆ rapid_rating ┆ blitz_rating │
│ ---     ┆ ---                       ┆ ---    ┆ ---          ┆ ---          │
│ i64     ┆ str                       ┆ i64    ┆ i64          ┆ i64          │
╞═════════╪═══════════════════════════╪════════╪══════════════╪══════════════╡
│ 1961039 ┆ Machado, Carlos Augusto G ┆ 1627   ┆ 1585         ┆ 1672         │
└─────────┴───────────────────────────┴────────┴──────────────┴──────────────┘
shape: (1, 3)
┌────────────────────┬──────────────────────────┬──────────────────────────┐
│ percentile(rating) ┆ percentile(rapid_rating) ┆ percentile(blitz_rating) │
│ ---                ┆ ---                      ┆ ---                      │
│ f64                ┆ f64                      ┆ f64                      │
╞════════════════════╪══════════════════════════╪══════════════════════════╡
│ 33.336279          ┆ 35.895522                ┆ 42.024542                │
└────────────────────┴──────────────────────────┴──────────────────────────┘
```

## LICENSE

See [LICENSE](LICENSE) for details.
