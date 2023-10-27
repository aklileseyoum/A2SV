class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int length = img1.size();
        int ans = 0;

        for (int dx = -length + 1; dx < length; dx++) {
            for (int dy = -length + 1; dy < length; dy++) {
                int count = 0;
                for (int x = 0; x < length; x++) {
                    int nx = x + dx;
                    if (0 <= nx && nx < length) {
                        for (int y = 0; y < length; y++) {
                            int ny = y + dy;
                            if (0 <= ny && ny < length) {
                                if (img1[nx][ny] == 1 && img2[x][y] == 1) {
                                    count++;
                                }
                            }
                        }
                    }
                }

                ans = max(count, ans);
            }
        }

        return ans;
    }
};