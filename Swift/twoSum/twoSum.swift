class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int:Int]()
        let length = nums.count
        var complement: Int
        var arrayIndex: [Int] = []
        for index in 0..<length {
            complement = target - nums[index]
            if let val = dict[complement] {
                arrayIndex.append(contentsOf: [val, index])
                break
            } else {
                dict[nums[index]] = index
            }
        }
        return arrayIndex
    }
}
