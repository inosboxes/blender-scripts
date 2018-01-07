const fs = require("fs");
const debug = require("debug")("Tsk-dbg");
module.exports = function Task() {
  function readFile(path) {
    return fs.readFileSync(path, "utf8");
  }
  function writeFile(path, content) {
    return fs.writeFileSync(path, content,"utf8");
  }
  function normalizedKey(key) {
    return key.replace(".", "").replace(' ','-');
  }
  function normilizePlanetData(planet) {
    let keys = Object.keys(planet);
    let normalized = {};
    keys.map((v, k) => {
      let r = {};
      let value = planet[v];
      k = normalizedKey(v);
      if (['rotation','revolution'].includes(k)) {
        // Convert value to hours
        value = value.split(' ')
        let metric = value[1]
        value[0] = parseFloat(value[0])
        switch (metric) {
          case 'd':
            value = value[0] * 24
            break;
          case 'y':
            value = value[0] * 24 * 356
            break;
          default:
            value = value[0];
        }
        value = Number((value).toFixed(6))
        //debug(k,value + ' H', metric)
      } else {
        value = value.replace(',', '').replace('~','');
      }
      normalized[k] = value;
    });
    return normalized;
  }
  function transform(data) {
    let result = {};
    data.map(function(source, index) {
      let planets = source.data;
      planets.map(function(planet, i2) {
        let name = planet.planet;
        let planetInResult = result[name] || {};
        result[name] = Object.assign(
          planetInResult,
          normilizePlanetData(planet)
        );
      });
    });
    return result;
  }
  let data = readFile("./planetaty-characteristics.json");
  let result =  transform(JSON.parse(data));
  writeFile("./planetaty-characteristics-normal.json", JSON.stringify(result));
  return result;
};
