/*
  Input: a 2 dimensional array of integers
  Output: A 1 dimensional array of all the same elements preserving original order
*/

// this given array has a length of 3 because it has 3 arrays as items
var twoDimArr1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  var expected1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  
  var twoDimArr2 = [[1], [2], [3]];
  var expected2 = [1, 2, 3];
  
  var twoDimArr3 = [[], [], [10, 20]];
  var expected3 = [10, 20];
  
  /**
   * Flattens a two dimensional array into a new one dimensional array.
   * @param {Array<Array<any>>} twoDimArr An array of arrays of any data type.
   * @returns {Array<any>} The flattened array that should be one dimensional.
   */
  function flatten2dArray(twoDimArr) {
    var newArry=[]
    
    for(const subArr of twoDimArr){
        for(const elem of subArr){
            newArry.push(elem)
        }
    }

    // for(var i=0; i<twoDimArr.length; i++){
    //     for(var x=0; x<twoDimArr[i].length; x++){
    //         newArry.push(twoDimArr[i][x])
    //     }
    // }
    return newArry
    }    
 




  console.log(flatten2dArray(twoDimArr1))
  
  /*****************************************************************************/
  
  /* 
    Array: Second-Largest
  
    Return the second-largest element of an array, or null if there is none.
  
    Bonus: do it with one loop and no nested loops
  */
  
  // 2nd largest is 2nd
  var nums1 = [2, 3, 1, 4];
  var expected1 = 3;
  
  // largest is first
  var nums2 = [4, 1, 3, 2];
  var expected2 = 3;
  
  // largest duplicated first
  var nums3 = [4, 4, 4, 1, 3, 2];
  var expected3 = 3;
  
  // 2nd largest is first
  var nums4 = [3, 1, 4, 2];
  var expected4 = 3;
  
  // largest is 2nd
  var nums5 = [3, 4, 2, 1];
  var expected5 = 3;
  
  var nums6 = [3, 3];
  var expected6 = null;
  
  var nums7 = [2];
  var expected7 = null;
  
  var nums8 = [];
  var expected8 = null;
  
  /**
   * Finds the second largest int from the given array and returns it or null.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<number>} nums
   * @returns {?number} The second largest int from the given array or null.
   *    The ? in front means it's nullable.
   */
  function secondLargest(nums) {
    if(nums.length<2){
        return null
    }
    
    var largest=nums[0]
    for(var i=0; i<nums.length; i++){
        if(nums[i] > largest ){
            largest = nums[i]
        }
    }
    var secLargest=nums[1]
    for(var i=0; i<nums.length; i++){
        if(nums[i]<largest && secLargest == largest){
            secLargest = nums[i]
        }
        if(nums[i] > secLargest && nums[i] < largest ){
            secLargest = nums[i]
        }
    }
    if(largest == secLargest){
        return null
    }

    return secLargest
  }

//   console.log(secondLargest(nums1))
//   console.log(secondLargest(nums2))
//   console.log(secondLargest(nums3))
//   console.log(secondLargest(nums6))
//   console.log(secondLargest(nums7))