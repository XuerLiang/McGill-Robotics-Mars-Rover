;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::ControlOutput)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'ControlOutput (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::CONTROLOUTPUT")
  (make-package "BEGINNER_TUTORIALS::CONTROLOUTPUT"))

(in-package "ROS")
;;//! \htmlinclude ControlOutput.msg.html


(defclass beginner_tutorials::ControlOutput
  :super ros::object
  :slots (_velocity _steering_angle_change ))

(defmethod beginner_tutorials::ControlOutput
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

(setf (get beginner_tutorials::ControlOutput :md5sum-) "fcd261e6d1b905da554ca0b775f8bf1e")
(setf (get beginner_tutorials::ControlOutput :datatype-) "beginner_tutorials/ControlOutput")
(setf (get beginner_tutorials::ControlOutput :definition-)
      "float32 velocity
float32 steering_angle_change

")



(provide :beginner_tutorials/ControlOutput "fcd261e6d1b905da554ca0b775f8bf1e")


