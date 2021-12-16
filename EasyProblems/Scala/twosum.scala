object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        var numToIndex = Map.empty[Int, Int]
        
        for ((num, i) <- nums.zipWithIndex) {
            numToIndex.get(target - num) match {
                case Some(x) => return Array(x, i)
                case None => numToIndex += (num -> i)
            }
        }
        
        Array(-1,-1)
    }
}