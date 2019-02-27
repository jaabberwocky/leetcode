function elevator(left, right, call){
  let lift;
  let leftDist = Math.abs(left - call);
  let rightDist = Math.abs(right - call);
  
  if (leftDist > rightDist) {
    lift = 'right'
  } else if (leftDist < rightDist) {
    lift = 'left'
  } else {
    lift = 'right'
  }
  
  return lift
}