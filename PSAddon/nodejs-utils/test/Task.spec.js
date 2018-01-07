let debug = require('debug')('Task-dbg');
let chai = require('chai');
let expect = chai.expect;

let Task = require('../src/Task')

describe('"Task" module exports', function(){
  it('should an instance of "Function".', function() {
    expect(Task).to.be.instanceOf(Function)
  })
  it('should return instance of Object".', function() {
    let planets = Task();
    //debug(planets)
    expect(Task).to.be.instanceOf(Function)
  })
})
