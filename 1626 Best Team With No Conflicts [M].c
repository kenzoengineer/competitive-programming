#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max(a, b) \
    ({ __typeof__ (a) _a = (a); \
    __typeof__ (b) _b = (b); \
   _a > _b ? _a : _b; })

int compare(const void *e1, const void *e2)
{
    const int *a = *(const int **)e1;
    const int *b = *(const int **)e2;
    if (a[0] == b[0])
        return a[1] - b[1];
    else
        return a[0] - b[0];
}

int bestTeamScore(int *scores, int scoresSize, int *ages, int agesSize)
{
    int **pairs;
    pairs = malloc(scoresSize * sizeof(int *));
    for (int i = 0; i < scoresSize; i++)
    {
        pairs[i] = malloc(sizeof(int) * 2);
        pairs[i][0] = ages[i];
        pairs[i][1] = scores[i];
    }

    qsort(pairs, scoresSize, sizeof(pairs[0]), compare);

    int *dp = malloc(scoresSize * sizeof(int));
    int result = 0;
    for (int i = 0; i < scoresSize; i++)
    {
        dp[i] = pairs[i][1];
        result = max(result, dp[i]);
    }

    for (int i = 0; i < scoresSize; i++) {
        for (int j = i - 1; j >= 0; j--) {
            if (pairs[j][1] <= pairs[i][1]) {
                dp[i] = max(dp[i], pairs[i][1] + dp[j]);
            }
        }
        result = max(dp[i], result);
    }

    free(dp);
    for (int i = 0; i < scoresSize; i++) {
        free(pairs[i]);
    }
    free(pairs);

    return result;
}

int main()
{
    int t1[4] = {1, 2, 3, 5};
    int t2 = 4;
    int t3[4] = {8, 9, 10, 1};
    int t4 = 4;
    printf("RESULT: %d\n", bestTeamScore(t1, t2, t3, t4));
    return 0;
}