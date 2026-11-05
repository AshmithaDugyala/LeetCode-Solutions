bool canJump(int* nums, int numsSize) {
    int maxReach = 0;

    for (int i = 0; i < numsSize; i++) {

        // if current index is unreachable
        if (i > maxReach)
            return false;

        // update max reach
        if (i + nums[i] > maxReach)
            maxReach = i + nums[i];
    }

    return true;
}