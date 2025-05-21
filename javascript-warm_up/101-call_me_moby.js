#!/usr/bin/node

function callMeNTimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = callMeNTimes;
