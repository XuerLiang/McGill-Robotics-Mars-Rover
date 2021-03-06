// Generated by gencpp from file autonomous_navigation/ControlOutput.msg
// DO NOT EDIT!


#ifndef AUTONOMOUS_NAVIGATION_MESSAGE_CONTROLOUTPUT_H
#define AUTONOMOUS_NAVIGATION_MESSAGE_CONTROLOUTPUT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace autonomous_navigation
{
template <class ContainerAllocator>
struct ControlOutput_
{
  typedef ControlOutput_<ContainerAllocator> Type;

  ControlOutput_()
    : velocity(0.0)
    , steering_angle_change(0.0)  {
    }
  ControlOutput_(const ContainerAllocator& _alloc)
    : velocity(0.0)
    , steering_angle_change(0.0)  {
  (void)_alloc;
    }



   typedef float _velocity_type;
  _velocity_type velocity;

   typedef float _steering_angle_change_type;
  _steering_angle_change_type steering_angle_change;





  typedef boost::shared_ptr< ::autonomous_navigation::ControlOutput_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonomous_navigation::ControlOutput_<ContainerAllocator> const> ConstPtr;

}; // struct ControlOutput_

typedef ::autonomous_navigation::ControlOutput_<std::allocator<void> > ControlOutput;

typedef boost::shared_ptr< ::autonomous_navigation::ControlOutput > ControlOutputPtr;
typedef boost::shared_ptr< ::autonomous_navigation::ControlOutput const> ControlOutputConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::autonomous_navigation::ControlOutput_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::autonomous_navigation::ControlOutput_<ContainerAllocator1> & lhs, const ::autonomous_navigation::ControlOutput_<ContainerAllocator2> & rhs)
{
  return lhs.velocity == rhs.velocity &&
    lhs.steering_angle_change == rhs.steering_angle_change;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::autonomous_navigation::ControlOutput_<ContainerAllocator1> & lhs, const ::autonomous_navigation::ControlOutput_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace autonomous_navigation

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::autonomous_navigation::ControlOutput_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::autonomous_navigation::ControlOutput_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::autonomous_navigation::ControlOutput_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fcd261e6d1b905da554ca0b775f8bf1e";
  }

  static const char* value(const ::autonomous_navigation::ControlOutput_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfcd261e6d1b905daULL;
  static const uint64_t static_value2 = 0x554ca0b775f8bf1eULL;
};

template<class ContainerAllocator>
struct DataType< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >
{
  static const char* value()
  {
    return "autonomous_navigation/ControlOutput";
  }

  static const char* value(const ::autonomous_navigation::ControlOutput_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 velocity\n"
"float32 steering_angle_change\n"
;
  }

  static const char* value(const ::autonomous_navigation::ControlOutput_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.velocity);
      stream.next(m.steering_angle_change);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ControlOutput_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonomous_navigation::ControlOutput_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::autonomous_navigation::ControlOutput_<ContainerAllocator>& v)
  {
    s << indent << "velocity: ";
    Printer<float>::stream(s, indent + "  ", v.velocity);
    s << indent << "steering_angle_change: ";
    Printer<float>::stream(s, indent + "  ", v.steering_angle_change);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AUTONOMOUS_NAVIGATION_MESSAGE_CONTROLOUTPUT_H
