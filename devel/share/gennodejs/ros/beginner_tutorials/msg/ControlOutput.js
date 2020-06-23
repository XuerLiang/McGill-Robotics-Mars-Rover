// Auto-generated. Do not edit!

// (in-package beginner_tutorials.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ControlOutput {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.velocity = null;
      this.steering_angle_change = null;
    }
    else {
      if (initObj.hasOwnProperty('velocity')) {
        this.velocity = initObj.velocity
      }
      else {
        this.velocity = 0.0;
      }
      if (initObj.hasOwnProperty('steering_angle_change')) {
        this.steering_angle_change = initObj.steering_angle_change
      }
      else {
        this.steering_angle_change = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ControlOutput
    // Serialize message field [velocity]
    bufferOffset = _serializer.float32(obj.velocity, buffer, bufferOffset);
    // Serialize message field [steering_angle_change]
    bufferOffset = _serializer.float32(obj.steering_angle_change, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ControlOutput
    let len;
    let data = new ControlOutput(null);
    // Deserialize message field [velocity]
    data.velocity = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [steering_angle_change]
    data.steering_angle_change = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'beginner_tutorials/ControlOutput';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fcd261e6d1b905da554ca0b775f8bf1e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 velocity
    float32 steering_angle_change
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ControlOutput(null);
    if (msg.velocity !== undefined) {
      resolved.velocity = msg.velocity;
    }
    else {
      resolved.velocity = 0.0
    }

    if (msg.steering_angle_change !== undefined) {
      resolved.steering_angle_change = msg.steering_angle_change;
    }
    else {
      resolved.steering_angle_change = 0.0
    }

    return resolved;
    }
};

module.exports = ControlOutput;
