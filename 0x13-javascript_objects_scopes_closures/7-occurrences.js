#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let nOccurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nOccurences++;
    }
  }
  return nOccurrences;
};
