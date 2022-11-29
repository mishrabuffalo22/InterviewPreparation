class RandomizedSet {
public:
    vector<int> v;
    unordered_map<int,int> mp;
    int i;
    RandomizedSet() {
        i=-1;
    }
    bool insert(int val) {
        if(mp.find(val)==mp.end()){
            v.push_back(val);
            i++;
            mp[val]=i;
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
        if(i>=0 && mp.find(val)!=mp.end()){
            int index=mp[val];
            swap(v[index],v[i]);
            mp[v[index]]=index;
            mp.erase(val);
            v.pop_back();
            i--;
            return true;
        }
        return false;
    }
    int getRandom() {
        return v[rand()%v.size()];
    }
};