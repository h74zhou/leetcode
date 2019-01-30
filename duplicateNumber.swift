class Solution {
    func findDuplicate(_ nums: [Int]) -> Int {
        var answer : Int = 0;
        let arraySorted = nums.sorted()
        for i in 0..<nums.count {
            if (arraySorted[i] == arraySorted[i+1]) {
                answer = arraySorted[i]
                break
            }
        }
        return answer
    }
}
