/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
 int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

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

        // 🔥 skip duplicates
        if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])
            continue;

        used[i] = 1;
        path[pathSize] = nums[i];

        dfs(nums, n, used, path, pathSize + 1,
            result, returnSize, returnColumnSizes);

        used[i] = 0;
    }
}

int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
     qsort(nums, numsSize, sizeof(int), cmp);

    int max = 40320; // 8!
    int** result = (int**)malloc(sizeof(int*) * max);
    *returnSize = 0;

    *returnColumnSizes = (int*)malloc(sizeof(int) * max);

    int* used = (int*)calloc(numsSize, sizeof(int));
    int* path = (int*)malloc(sizeof(int) * numsSize);

    dfs(nums, numsSize, used, path, 0,
        &result, returnSize, returnColumnSizes);

    return result;
}