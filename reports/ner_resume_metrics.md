# Resume NER - held-out test metrics

distilroberta-base | 30 test resumes | 494 gold spans

|                     |   precision |   recall |    f1 |   support |
|:--------------------|------------:|---------:|------:|----------:|
| Name                |       0.935 |    0.967 | 0.951 |        30 |
| Email Address       |       0.561 |    0.793 | 0.657 |        29 |
| Degree              |       0.618 |    0.583 | 0.6   |        36 |
| Location            |       0.667 |    0.522 | 0.585 |        69 |
| Designation         |       0.567 |    0.594 | 0.58  |        64 |
| College Name        |       0.564 |    0.524 | 0.543 |        42 |
| Graduation Year     |       0.467 |    0.226 | 0.304 |        31 |
| Companies worked at |       0.223 |    0.189 | 0.205 |       111 |
| Skills              |       0.344 |    0.141 | 0.2   |        78 |
| Years of Experience |       0     |    0     | 0     |         4 |
| ** OVERALL **       |       0.509 |    0.421 | 0.461 |       494 |
