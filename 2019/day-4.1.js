const RANGE = { start: 165432, end: 707912 }

const numberIncreases = num => {
  const digits = num.toString().split('').map(d => parseInt(d));

  for (let i = 1; i < digits.length; i++) {
    if (digits[i - 1] > digits[i]) return false;
  }

  return true;
}

const isAllUnique = num => {
  const digits    = num.toString().split('').map(d => parseInt(d));
  const digitMap  = {};

  digits.forEach(d => digitMap[d] ? digitMap[d] += 1 : digitMap[d] = 1);

  return digits.length == Object.keys(digitMap).length;
}

const possiblePasswords = range => {
  const possibilities = [];

  for(let i = range.start; i <= range.end; i++) {
    if (numberIncreases(i)) possibilities.push(i);
  }

  return possibilities.filter(p => !isAllUnique(p));
};

console.log(possiblePasswords(RANGE).length)
