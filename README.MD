# A/B testing CLI tool

---

### To run

```bash
python a_b_test.py -f <file.csv> -t 2s -c1 <column1> -c2 <column1> -a <alpha>
```

### Flags

```
'-f',  '--file'  -> File path of the dataset (required)
'-t',  '--test'  -> Type of test to perform (required): chi2, 1s, 2s
'-c1', '--col1'  -> Name of column 1 (required)
'-c2', '--col2'  -> Name of column 2 (optional for 1 sample test)
'-m',  '--mean'  -> Mean value (optional for 1 sample test)
'-a',  '--alpha' -> Significance level (default: 0.05)
```

### Example:

```bash
python a_b_test.py -f <file.csv> -t 1s -c1 <column1> -a <alpha> -m <mean>
```
