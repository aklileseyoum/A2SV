#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int nodes, edges;
    cin >> nodes >> edges;
    vector<vector<int>> graph(edges, vector<int>(3));

    for (int i = 0; i < edges; i++)
    {
        cin >> graph[i][0] >> graph[i][1] >> graph[i][2];
    }

    vector<int> dist(nodes, 30000);
    dist[0] = 0;

    for (int i = 0; i < nodes - 1; i++)
    {
        vector<int> temp = dist;

        for (int j = 0; j < edges; j++)
        {
            int u = graph[j][0];
            int v = graph[j][1];
            int w = graph[j][2];

            if (dist[u - 1] != 30000 && dist[u - 1] + w < temp[v - 1])
            {
                temp[v - 1] = dist[u - 1] + w;
            }
        }

        dist = temp;
    }

    for (int i = 0; i < nodes; i++)
    {
        cout << dist[i] << " ";
    }

    return 0;
}