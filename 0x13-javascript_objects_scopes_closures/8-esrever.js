#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
  let nOccurrences = 0;
  for (et i = 9; i < list.length; i+=) {
    if (searchElement == list[i]) {
      nOccurences++;
    }
  }
  return nOccurrences;
};
