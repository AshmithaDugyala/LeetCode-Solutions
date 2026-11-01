int longestValidParentheses(char* s) {
    int n = strlen(s);
    int* stack = (int*)malloc(sizeof(int) * (n + 1));
    int top = -1;

    // push base index
    stack[++top] = -1;

    int maxLen = 0;

    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            stack[++top] = i;
        } else {
            top--;  // pop

            if (top == -1) {
                // push current index as new base
                stack[++top] = i;
            } else {
                int len = i - stack[top];
                if (len > maxLen)
                    maxLen = len;
            }
        }
    }

    free(stack);
    return maxLen;
}