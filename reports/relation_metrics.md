# Relation extraction - held-out test metrics

20 job descriptions | 95 gold relations | gold entities given to both systems

Both systems tuned on dev only: baseline distance cutoffs {'DEGREE_IN': 40, 'EXPERIENCE_IN': 20}, model threshold 0.5.

|               |   precision |   recall |    f1 |   tp |   predicted |   gold |
|:--------------|------------:|---------:|------:|-----:|------------:|-------:|
| rule baseline |       0.73  |    0.968 | 0.833 |   92 |         126 |     95 |
| trained model |       0.591 |    0.547 | 0.568 |   52 |          88 |     95 |

## Per label

|                                                      |   precision |   recall |    f1 |   tp |   predicted |   gold |
|:-----------------------------------------------------|------------:|---------:|------:|-----:|------------:|-------:|
| ('rule baseline (type + distance)', 'DEGREE_IN')     |       0.955 |    1     | 0.977 |   21 |          22 |     21 |
| ('rule baseline (type + distance)', 'EXPERIENCE_IN') |       0.683 |    0.959 | 0.798 |   71 |         104 |     74 |
| ('rule baseline (type + distance)', '** MICRO **')   |       0.73  |    0.968 | 0.833 |   92 |         126 |     95 |
| ('trained rel_component', 'DEGREE_IN')               |       0.75  |    1     | 0.857 |   21 |          28 |     21 |
| ('trained rel_component', 'EXPERIENCE_IN')           |       0.517 |    0.419 | 0.463 |   31 |          60 |     74 |
| ('trained rel_component', '** MICRO **')             |       0.591 |    0.547 | 0.568 |   52 |          88 |     95 |
