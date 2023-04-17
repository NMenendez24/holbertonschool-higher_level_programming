#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  for (let j = 0; j < list.length; j++) {
    if (searchElement === list[j]) {
      ocurrences += 1;
    }
  }
  return ocurrences;
};
