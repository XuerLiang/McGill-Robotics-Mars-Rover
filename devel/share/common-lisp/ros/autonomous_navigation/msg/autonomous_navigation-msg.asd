
(cl:in-package :asdf)

(defsystem "autonomous_navigation-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ControlOutput" :depends-on ("_package_ControlOutput"))
    (:file "_package_ControlOutput" :depends-on ("_package"))
    (:file "RoverState" :depends-on ("_package_RoverState"))
    (:file "_package_RoverState" :depends-on ("_package"))
  ))