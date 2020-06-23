; Auto-generated. Do not edit!


(cl:in-package autonomous_navigation-msg)


;//! \htmlinclude ControlOutput.msg.html

(cl:defclass <ControlOutput> (roslisp-msg-protocol:ros-message)
  ((velocity
    :reader velocity
    :initarg :velocity
    :type cl:float
    :initform 0.0)
   (steering_angle_change
    :reader steering_angle_change
    :initarg :steering_angle_change
    :type cl:float
    :initform 0.0))
)

(cl:defclass ControlOutput (<ControlOutput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControlOutput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControlOutput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name autonomous_navigation-msg:<ControlOutput> is deprecated: use autonomous_navigation-msg:ControlOutput instead.")))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <ControlOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_navigation-msg:velocity-val is deprecated.  Use autonomous_navigation-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'steering_angle_change-val :lambda-list '(m))
(cl:defmethod steering_angle_change-val ((m <ControlOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_navigation-msg:steering_angle_change-val is deprecated.  Use autonomous_navigation-msg:steering_angle_change instead.")
  (steering_angle_change m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControlOutput>) ostream)
  "Serializes a message object of type '<ControlOutput>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'steering_angle_change))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControlOutput>) istream)
  "Deserializes a message object of type '<ControlOutput>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'steering_angle_change) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControlOutput>)))
  "Returns string type for a message object of type '<ControlOutput>"
  "autonomous_navigation/ControlOutput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlOutput)))
  "Returns string type for a message object of type 'ControlOutput"
  "autonomous_navigation/ControlOutput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControlOutput>)))
  "Returns md5sum for a message object of type '<ControlOutput>"
  "fcd261e6d1b905da554ca0b775f8bf1e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControlOutput)))
  "Returns md5sum for a message object of type 'ControlOutput"
  "fcd261e6d1b905da554ca0b775f8bf1e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControlOutput>)))
  "Returns full string definition for message of type '<ControlOutput>"
  (cl:format cl:nil "float32 velocity~%float32 steering_angle_change~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControlOutput)))
  "Returns full string definition for message of type 'ControlOutput"
  (cl:format cl:nil "float32 velocity~%float32 steering_angle_change~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControlOutput>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControlOutput>))
  "Converts a ROS message object to a list"
  (cl:list 'ControlOutput
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':steering_angle_change (steering_angle_change msg))
))
