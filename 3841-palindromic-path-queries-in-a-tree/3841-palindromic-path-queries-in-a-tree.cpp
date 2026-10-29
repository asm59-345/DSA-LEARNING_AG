
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> adj;
    int n, timer = 0, LOG;

    vector<int> tin, tout, eulerTour, depth;
    vector<vector<int>> up;
    vector<int> segmentTree;

    void dfs(int node, int parent, string& s) {
        tin[node] = timer;
        eulerTour[timer++] = (1 << (s[node] - 'a'));

        up[node][0] = parent;

        for (int j = 1; j < LOG; j++) {
            up[node][j] = up[up[node][j - 1]][j - 1];
        }

        for (int child : adj[node]) {
            if (child == parent) continue;

            depth[child] = depth[node] + 1;
            dfs(child, node, s);
        }

        tout[node] = timer;
        eulerTour[timer++] = (1 << (s[node] - 'a'));
    }

    int getLCA(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);

        int diff = depth[u] - depth[v];

        for (int j = LOG - 1; j >= 0; j--) {
            if (diff & (1 << j)) {
                u = up[u][j];
            }
        }

        if (u == v) return u;

        for (int j = LOG - 1; j >= 0; j--) {
            if (up[u][j] != up[v][j]) {
                u = up[u][j];
                v = up[v][j];
            }
        }

        return up[u][0];
    }

    void buildSegmentTree(int i, int l, int r,
                          vector<int>& nums) {
        if (l == r) {
            segmentTree[i] = nums[l];
            return;
        }

        int mid = l + (r - l) / 2;

        buildSegmentTree(2 * i + 1, l, mid, nums);
        buildSegmentTree(2 * i + 2, mid + 1, r, nums);

        segmentTree[i] =
            segmentTree[2 * i + 1] ^
            segmentTree[2 * i + 2];
    }

    void updateSegmentTree(int index, int val,
                           int i, int l, int r) {
        if (l == r) {
            segmentTree[i] = val;
            return;
        }

        int mid = l + (r - l) / 2;

        if (index <= mid) {
            updateSegmentTree(index, val,
                             2 * i + 1, l, mid);
        } else {
            updateSegmentTree(index, val,
                             2 * i + 2, mid + 1, r);
        }

        segmentTree[i] =
            segmentTree[2 * i + 1] ^
            segmentTree[2 * i + 2];
    }

    int querySegmentTree(int start, int end,
                         int i, int l, int r) {
        if (l > end || r < start) return 0;

        if (start <= l && r <= end) {
            return segmentTree[i];
        }

        int mid = l + (r - l) / 2;

        return querySegmentTree(start, end,
                                2 * i + 1, l, mid)
             ^ querySegmentTree(start, end,
                                2 * i + 2, mid + 1, r);
    }

    vector<bool> palindromePath(
        int n,
        vector<vector<int>>& edges,
        string s,
        vector<string>& queries
    ) {
        this->n = n;
        timer = 0;

        adj.assign(n, {});
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];

            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        tin.assign(n, 0);
        tout.assign(n, 0);
        depth.assign(n, 0);
        eulerTour.assign(2 * n, 0);

        LOG = 1;
        while ((1LL << LOG) <= n) LOG++;

        up.assign(n, vector<int>(LOG, 0));

        // Root's parent is itself.
        dfs(0, 0, s);

        int N = 2 * n;
        segmentTree.assign(4 * N, 0);
        buildSegmentTree(0, 0, N - 1, eulerTour);

        vector<bool> result;
        result.reserve(queries.size());

        for (const string& q : queries) {
            stringstream ss(q);
            string type;
            ss >> type;

            if (type == "update") {
                int node;
                char c;
                ss >> node >> c;

                int charValue = 1 << (c - 'a');
                s[node] = c;

                updateSegmentTree(
                    tin[node], charValue, 0, 0, N - 1
                );

                updateSegmentTree(
                    tout[node], charValue, 0, 0, N - 1
                );
            } else {
                int u, v;
                ss >> u >> v;

                int lcaNode = getLCA(u, v);
                int charValue = 1 << (s[lcaNode] - 'a');

                int mask =
                    querySegmentTree(
                        0, tin[u], 0, 0, N - 1
                    ) ^
                    querySegmentTree(
                        0, tin[v], 0, 0, N - 1
                    ) ^
                    charValue;

                result.push_back(
                    (mask & (mask - 1)) == 0
                );
            }
        }

        return result;
    }
};
