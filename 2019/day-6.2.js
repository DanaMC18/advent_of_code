
class Graph {
  constructor () {
    this.vertMap = {};
  }

  addToVertex(vert, val) { this.vertMap[vert].push(val); }
  createNewVertex(vert) { this.vertMap[vert] = [] }
}

const createGraph = isParentToChild => {
  let g = new Graph();

  ORBITS.forEach(o => {
    const nodes = o.split(')');
    const k = isParentToChild ? nodes[0] : nodes[1];
    const v = isParentToChild ? nodes[1] : nodes[0]

    if (!g.vertMap[k]) g.createNewVertex(k)
    g.addToVertex(k, v);
  })

  return g;
}
