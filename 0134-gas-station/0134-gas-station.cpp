class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total_tank = 0;
        int curr_tank = 0;
        int st_index =0;

        for (int i =0; i < gas.size(); ++i){
            int net_fuel = gas[i] - cost[i];

            total_tank += net_fuel;
            curr_tank += net_fuel;

            if ( curr_tank < 0){
                st_index = i + 1;
                curr_tank = 0;

            }

        }
        return (total_tank < 0) ? -1 : st_index;
    }
};