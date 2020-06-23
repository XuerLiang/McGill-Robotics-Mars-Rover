
(cl:in-package :asdf)

(defsystem "beginner_tutorials-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ControlOutput" :depends-on ("_package_ControlOutput"))
    (:file "_package_ControlOutput" :depends-on ("_package"))
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
    (:file "RoverState" :depends-on ("_package_RoverState"))
    (:file "_package_RoverState" :depends-on ("_package"))
  ))