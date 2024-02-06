/* 
  Given an array of integers
  return the index where the smallest integer is located

  return -1 if there is no smallest integer (array is empty) 
  since -1 is not a valid index, this indicates it couldn't be found

  If the smallest integer occurs more than once, return the index of the first one.
*/

var nums1 = [5, 2, 3];
var expected1 = 1;

var nums2 = [5, 4, 2, 2, 3];
var expected2 = 2;

var nums3 = [];
var expected3 = -1;

var nums4 = [2];
var expected4 = 0;

var nums5 = [2, 2];


/**
 * Returns the index of the smallest number from the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} Index of smallest number or -1 if empty given array.
 */
function indexOfMinVal(nums) {
  if(nums.length === 0){
    return -1
  }
  var smallIdx = 0
  for(var i =1; i< nums.length; i++){
    if(nums[i] < nums[smallIdx]){
        smallIdx = i
    }
  }
  return smallIdx
}

// console.log(indexOfMinVal(nums1))
// console.log(indexOfMinVal(nums2))
// console.log(indexOfMinVal(nums3))
// console.log(indexOfMinVal(nums4))
// console.log(indexOfMinVal(nums5))

/*******************************************************************************/

/* 
  Given an array, reverse it's items in place
  return the array after reversing it

  Do it in place without using any built in methods
*/

var arr1 = [1, 2, 3];
var expected1 = [3, 2, 1];

var arr2 = ['a', 'b'];
var expected2 = ['b', 'a'];

var arr3 = ['a'];
var expected3 = ['a'];

var arr4 = [];
var expected4 = [];

/**
 * Reverses the given arr in place without built in methods
 * BONUS: Do this in place without built ins
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} items
 * @returns {Array<any>} The given arr after being reversed.
 */
function reverseArr(items) {
    // for(var j = 1; j < items.length; j++){

        for(var i = items.length-1; i > 0; i--){
        [items[0], items[i], items[i-1]] = [items[i-1], items[i], items[0]]
        }
    }
    return items
// }

console.log(reverseArr(arr1))


// var a = 0;
// var b = 1;
// [a, b] = [b, a]
// console.log(a)
// console.log(b)