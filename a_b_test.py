import argparse
import pandas as pd
import scipy.stats as stats


def chi_square(df, col1, col2, alpha):
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    if p <= alpha:
        print(
            f'Reject null hypothesis. There is a significant association between {col1} and {col2} (p={p})')
    else:
        print(
            f'Fail to reject null hypothesis. There is no significant association between {col1} and {col2} (p={p})')


def one_sample_t_test(df, col1, mean, alpha):
    t, p = stats.ttest_1samp(df[col1], mean)
    if p <= alpha:
        print(
            f'Reject null hypothesis. The sample mean differs from the population mean (p={p})')
    else:
        print(
            f'Fail to reject null hypothesis. The sample mean is not significantly different from the population mean (p={p})')


def two_sample_t_test(df, col1, col2, alpha):
    t, p = stats.ttest_ind(df[col1], df[col2])
    if p <= alpha:
        print(
            f'Reject null hypothesis. There is a significant difference between the means of {col1} and {col2} (p={p})')
    else:
        print(
            f'Fail to reject null hypothesis. There is no significant difference between the means of {col1} and {col2} (p={p})')


def main():
    parser = argparse.ArgumentParser(description='A/B Testing CLI Tool')
    parser.add_argument('-f', '--file', type=str,
                        required=True, help='File path of the dataset')
    parser.add_argument('-t', '--test', type=str, required=True, choices=[
                        'chi2', '1s', '2s'], help='Type of test to perform (chi2: chi-square, 1s: 1 sample t-test, 2s: 2 sample t-test)')
    parser.add_argument('-c1', '--col1', type=str,
                        required=True, help='Name of column 1')
    parser.add_argument('-c2', '--col2', type=str,
                        help='Name of column 2 (optional for 1 sample test)')
    parser.add_argument('-m', '--mean', type=float,
                        help='Mean value (optional for 1 sample test)')
    parser.add_argument('-a', '--alpha', type=float, default=0.05,
                        help='Significance level (default: 0.05)')

    args = parser.parse_args()
    df = pd.read_csv(args.file)

    if args.test == 'chi2':
        chi_square(df, args.col1, args.col2, args.alpha)
    elif args.test == '1s':
        one_sample_t_test(df, args.col1, args.mean, args.alpha)
    elif args.test == '2s':
        two_sample_t_test(df, args.col1, args.col2, args.alpha)


if __name__ == '__main__':
    main()
