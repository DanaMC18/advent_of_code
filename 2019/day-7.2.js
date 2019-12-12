// const STATIC_INTCODE = [3,8,1001,8,10,8,105,1,0,0,21,46,63,76,97,118,199,280,361,442,99999,3,9,102,4,9,9,101,2,9,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,1002,9,5,9,1001,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

const STATIC_INTCODE = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5];
let INTCODE;

let RESULT;

const add       = (int1, int2) => int1 + int2;
const multiply  = (int1, int2) => int1 * int2;
const replace   = (val, pos) => INTCODE[pos] = val;
const print     = val => RESULT = val;

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

const gravityAssist = coords => {
  const func        = OPCODES[coords[0]];
  const param1      = INTCODE[coords[1]];
  const param2      = INTCODE[coords[2]];
  const posToUpdate = coords[3];

  INTCODE[posToUpdate] = func.call(null, param1, param2);
}

const paramMode = (opCode, index) => {
  const opStr   = String(opCode);
  const indStr  = String(index);
  const modes   = opStr.split('').map(m => parseInt(m)).reverse();
  const op      = modes[0];
  const func    = OPCODES[op];
  const params  = [];
  let mode;
  let param;

  for (let i = 2; i < 4; i++) {
    index += 1;
    mode  = modes[i] || 0;
    param = PARAM_MODES[mode].call(null, index);
    params.push(param);
  }

  params.push(INTCODE[index + 1]);

  if ([1,2].includes(op)) {
    INTCODE[params[2]] = func.call(null, params[0], params[1]);
    return 4;
  } else if (op === 4) {
    print(params[0]);
    return 2;
  } else if ([5,6].includes(op)) {
    const newPointer = func.call(null, op, params);
    return newPointer ? (newPointer - parseInt(indStr)) : 3;
  } else if ([7,8].includes(op)) {
    const val = func.call(null, op, params);
    INTCODE[params[2]] = val;
    return 4;
  }
}

// update to take in one input, own intcode, own pointer
const diagnostics = (inputs, pointer = 0) => {
  const opCode = INTCODE[pointer];
  if (opCode === 99 || !opCode) return RESULT;

  if ([1,2].includes(opCode)) {
    const coords = INTCODE.slice(pointer, pointer + 4);
    gravityAssist(coords);
    pointer += 4;
  } else if (opCode === 3) {
    const position = INTCODE[pointer + 1];
    const input = inputs[0];
    inputs = [inputs[1]];
    replace(input, position);
    pointer += 2;
  } else if (opCode === 4) {
    print(INTCODE[INTCODE[pointer + 1]]);
    pointer += 2;
  } else if ([7, 8].includes(opCode)) {
    const coords = INTCODE.slice(pointer + 1, pointer + 3);
    const params = coords.map(c => INTCODE[c]);
    const val = lessOrEqual(opCode, params);
    INTCODE[INTCODE[pointer + 3]] = val;
    pointer += 4
  } else {
    const addToPointer = paramMode(opCode, pointer);
    pointer += addToPointer
  }

  return diagnostics(inputs, pointer);
}

//* DAY 7 CODE STARTS HERE (tiny modifications above) *//

const permutations = (phases, perms=[], used=[]) => {
  for (let i = 0; i < phases.length; i++) {
    let phase = phases.splice(i, 1)[0];
    used.push(phase);
    if (phases.length === 0) perms.push(used.slice());
    permutations(phases, perms, used);
    phases.splice(i, 0, phase);
    used.pop();
  }
  return perms
};

const arrayMax = arr => Math.max.apply(Math, arr);

const maxThrusters = phases => {
  const maxThrusters  = [];
  const sequences     = permutations([[9,8,7,6,5]]);
  let thrusters       = [];
  let memory          = {};
  let output;
  let result;

  for (phaseSequence of sequences) {
    for (phase of phaseSequence) {
      if (!memory[phase]) {
        memory[phase] = STATIC_INTCODE.slice(0);
        output        = phase;
      };

      intcode = memory[phase];
      output  = output || thrusters[thrusters.length - 1];
      result  = diagnostics(output, intcode);
      thrusters.push(result);
    }
    maxThrusters.push(arrayMax(thrusters))
    thrusters = [0]
  }
  return arrayMax(maxThrusters);
}

console.log(maxThrusters([9,8,7,6,5]));
