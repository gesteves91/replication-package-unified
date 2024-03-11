from scipy.stats import mannwhitneyu

model_rankings_dict = {"documentation": 1, "size": 2, "complexity": 3, "coupling": 4}
developer_rankings_dict = {"documentation": 4, "size": 2, "complexity": 1, "coupling": 3}

statistic, p_value = mannwhitneyu(list(model_rankings_dict.values()), list(developer_rankings_dict.values()), alternative='two-sided')

print(f'Mann-Whitney U statistic: {statistic}')
print(f'P-value: {p_value}')

alpha = 0.05

if p_value < alpha:
    print('Reject the null hypothesis: There is a significant difference between the two rankings provided by the model and the developers.')
else:
    print('Fail to reject the null hypothesis: There is no significant difference between the two rankings provided by the model and the developers.')
