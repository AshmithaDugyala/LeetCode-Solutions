/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generateMatrix(int n, int* returnSize, int** returnColumnSizes) {
    int** matrix = (int**)malloc(sizeof(int*) * n);
    *returnColumnSizes = (int*)malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++) {
        matrix[i] = (int*)malloc(sizeof(int) * n);
        (*returnColumnSizes)[i] = n;
    }

    *returnSize = n;

    int top = 0, bottom = n - 1;
    int left = 0, right = n - 1;

    int num = 1;

    while (top <= bottom && left <= right) {

        // left → right
        for (int j = left; j <= right; j++)
            matrix[top][j] = num++;
        top++;

        // top → bottom
        for (int i = top; i <= bottom; i++)
            matrix[i][right] = num++;
        right--;

        // right → left
        if (top <= bottom) {
            for (int j = right; j >= left; j--)
                matrix[bottom][j] = num++;
            bottom--;
        }

        // bottom → top
        if (left <= right) {
            for (int i = bottom; i >= top; i--)
                matrix[i][left] = num++;
            left++;
        }
    }

    return matrix;
}