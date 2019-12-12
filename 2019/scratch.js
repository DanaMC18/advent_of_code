const INTCODE = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,46,47,225,2,122,130,224,101,-1998,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,61,51,225,102,32,92,224,101,-800,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,61,64,225,1001,118,25,224,101,-106,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,33,25,225,1102,73,67,224,101,-4891,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,14,81,225,1102,17,74,225,1102,52,67,225,1101,94,27,225,101,71,39,224,101,-132,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,14,38,224,101,-1786,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,65,126,224,1001,224,-128,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,81,40,224,1001,224,-121,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,374,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,539,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,614,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226];

const add       = (int1, int2) => int1 + int2;
const multiply  = (int1, int2) => int1 * int2;
const replace   = (val, pos) => INTCODE[pos] = val;
const print     = val => console.log(val);

const jump = (opCode, params) => {
  if ((opCode === 5 && params[0] > 0) ||
      (opCode === 6 && params[0] === 0)) return params[1];
  return false;
};

const lessOrEqual = (opCode, params) => {
  let val = 0;
  if ((opCode === 7 && params[0] < params[1]) ||
    (opCode === 8 && params[0] === params[1])) val = 1;
  return val;
}

const position  = pos => INTCODE[INTCODE[pos]];
const immediate = pos => INTCODE[pos];

const OPCODES = {
  1: add,
  2: multiply,
  3: replace,
  4: print,
  5: jump, // jumpTrue
  6: jump, // jumpFalse
  7: lessOrEqual, // lessThan
  8: lessOrEqual // equalTo
}

const PARAM_MODES = {
  0: position,
  1: immediate
}

const paramMode = (opStr, index) => {
  const modes   = opStr.split('').map(m => parseInt(m)).reverse();
  const op      = modes[0];
  const params  = [];
  let mode;
  let param;

  for (let i = 2; i < 4; i++) {
    index += 1
    mode = modes[i] || 0;
    param = PARAM_MODES[mode].call(null, index);
    params.push(param);
  }

  params.push(INTCODE[index + 1]);
  return [op, params];
}

const diagnostics = (input, pointer = 0) => {
  let opCode = INTCODE[pointer];
  let params;
  
  if (!opCode || opCode === 99) return;

  if (String(opCode).length > 1) {
    [opCode, params] = paramMode(String(opCode), pointer);
  }

  let func = OPCODES[opCode];

  switch (opCode) {
    case 1:
    case 2:
      if (!params) {
        const coords = INTCODE.slice(pointer + 1, pointer + 3);
        params = coords.map(c => INTCODE[c]);
        params.push(INTCODE[pointer + 2]);
      }
      INTCODE[params[2]] = func.call(null, params[0], params[1]);
      pointer += 4;
      break;
    case 3:
      const position = INTCODE[pointer + 1];
      func.call(null, input, position);
      pointer += 2;
      break;
    case 4:
      if (!params) params = [INTCODE[INTCODE[pointer + 1]]];
      print(params[0]);
      pointer += 2;
      break;
    case 5:
    case 6:
      const newPointer = func.call(null, opCode, params);
      pointer = (newPointer) || (pointer + 3);
      break;
    case 7:
    case 8:
      if (!params) {
        const coords = INTCODE.slice(pointer + 1, pointer + 3);
        params = coords.map(c => INTCODE[c]);
        params.push(INTCODE[pointer + 2]);
      }
      const val = func.call(null, opCode, params);
      INTCODE[params[2]] = val;
      pointer += 4
      break;
  }
  diagnostics(input, pointer);
}

diagnostics(5);
