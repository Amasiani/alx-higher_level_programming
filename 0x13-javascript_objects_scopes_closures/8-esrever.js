#!/usr/bin/node
exports.eserver = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len = i) > 0) {
    const temp = list[len];
    list[len] = list[i];
    list[i] = temp;
    i++;
    len--;
  }
  return list;
};
