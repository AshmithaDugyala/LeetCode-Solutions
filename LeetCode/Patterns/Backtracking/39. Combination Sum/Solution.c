/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
 void dfs(int* candidates, int n, int target, int start,
         int* path, int pathSize,
         int*** result, int* returnSize, int** returnColumnSizes) {

    if (target == 0) {
        (*result)[*returnSize] = (int*)malloc(sizeof(int) * pathSize);
        for (int i = 0; i < pathSize; i++)
            (*result)[*returnSize][i] = path[i];

        (*returnColumnSizes)[*returnSize] = pathSize;
        (*returnSize)++;
        return;
    }

    for (int i = start; i < n; i++) {

        if (candidates[i] > target)
            continue;

        path[pathSize] = candidates[i];

        dfs(candidates, n, target - candidates[i], i,
            path, pathSize + 1,
            result, returnSize, returnColumnSizes);
    }
}
int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {
    int** result = (int**)malloc(sizeof(int*) * 150);
    *returnSize = 0;
    *returnColumnSizes = (int*)malloc(sizeof(int) * 150);

    int* path = (int*)malloc(sizeof(int) * 50);

    dfs(candidates, candidatesSize, target, 0,
        path, 0, &result, returnSize, returnColumnSizes);

    return result;
}