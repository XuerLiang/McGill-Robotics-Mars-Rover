;; Auto-generated. Do not edit!


(when (boundp 'autonomous_navigation::ControlOutput)
  (if (not (find-package "AUTONOMOUS_NAVIGATION"))
    (make-package "AUTONOMOUS_NAVIGATION"))
  (shadow 'ControlOutput (find-package "AUTONOMOUS_NAVIGATION")))
(unless (find-package "AUTONOMOUS_NAVIGATION::CONTROLOUTPUT")
  (make-package "AUTONOMOUS_NAVIGATION::CONTROLOUTPUT"))

(in-package "ROS")
;;//! \htmlinclude ControlOutput.msg.html


(defclass autonomous_navigation::ControlOutput
  :super ros::object
  :slots (_velocity _steering_angle_change ))

(defmethod autonomous_navigation::ControlOutput
  (:init
   (&key
    ((:velocity __velocity) 0.0)
    ((:steering_angle_change __steering_angle_change) 0.0)
    )
   (send-super :init)
   (setq _velocity (float __velocity))
   (setq _steering_angle_change (float __steering_angle_change))
   self)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:steering_angle_change
   (&optional __steering_angle_change)
   (if __steering_angle_change (setq _steering_angle_change __steering_angle_change)) _steering_angle_change)
  (:serialization-length
   ()
   (+
    ;; float32 _velocity
    4
    ;; float32 _steering_angle_change
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _steering_angle_change
       (sys::poke _steering_angle_change (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _velocity
     (setq _velocity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _steering_angle_change
     (setq _steering_angle_change (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get autonomous_navigation::ControlOutput :md5sum-) "fcd261e6d1b905da554ca0b775f8bf1e")
(setf (get autonomous_navigation::ControlOutput :datatype-) "autonomous_navigation/ControlOutput")
(setf (get autonomous_navigation::ControlOutput :definition-)
      "float32 velocity
float32 steering_angle_change

")



(provide :autonomous_navigation/ControlOutput "fcd261e6d1b905da554ca0b775f8bf1e")


