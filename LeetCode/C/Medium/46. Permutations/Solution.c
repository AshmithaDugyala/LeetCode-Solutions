/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
 void dfs(int* nums, int n,
         int* used,
         int* path,
         int pathSize,
         int*** result,
         int* returnSize,
         int** returnColumnSizes) {

    if (pathSize == n) {
        (*result)[*returnSize] = (int*)malloc(sizeof(int) * n);
        for (int i = 0; i < n; i++)
            (*result)[*returnSize][i] = path[i];

        (*returnColumnSizes)[*returnSize] = n;
        (*returnSize)++;
        return;
    }

    for (int i = 0; i < n; i++) {

        if (used[i])
            continue;

        used[i] = 1;
        path[pathSize] = nums[i];

        dfs(nums, n, used, path, pathSize + 1,
            result, returnSize, returnColumnSizes);

        used[i] = 0; // backtrack
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int max = 720; // 6! max constraint
    int** result = (int**)malloc(sizeof(int*) * max);
    *returnSize = 0;

    *returnColumnSizes = (int*)malloc(sizeof(int) * max);

    int* used = (int*)calloc(numsSize, sizeof(int));
    int* path = (int*)malloc(sizeof(int) * numsSize);

    dfs(nums, numsSize, used, path, 0,
        &result, returnSize, returnColumnSizes);

    return result;
}