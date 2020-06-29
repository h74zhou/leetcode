class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        
        var hash: [Int : Int] = [:]
        var res : [Int] = [];
        
        for (i, n) in nums.enumerated() {
            if let index = hash[target - n]{
                res.append(index)
                res.append(i)
            }
            hash[n] = i 
        }
        return res;
    }
}

