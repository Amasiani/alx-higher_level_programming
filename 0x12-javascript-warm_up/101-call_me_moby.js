#!/usr/bin/node
exports.callMeMody = function (x, theFunction) {
  for (let i = 0; i < x; ++i) theFunction();
};
