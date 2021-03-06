// Generated by gencpp from file autonomous_navigation/RoverState.msg
// DO NOT EDIT!


#ifndef AUTONOMOUS_NAVIGATION_MESSAGE_ROVERSTATE_H
#define AUTONOMOUS_NAVIGATION_MESSAGE_ROVERSTATE_H


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
struct RoverState_
{
  typedef RoverState_<ContainerAllocator> Type;

  RoverState_()
    : x(0.0)
    , y(0.0)
    , theta(0.0)  {
    }
  RoverState_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , theta(0.0)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _theta_type;
  _theta_type theta;





  typedef boost::shared_ptr< ::autonomous_navigation::RoverState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonomous_navigation::RoverState_<ContainerAllocator> const> ConstPtr;

}; // struct RoverState_

typedef ::autonomous_navigation::RoverState_<std::allocator<void> > RoverState;

typedef boost::shared_ptr< ::autonomous_navigation::RoverState > RoverStatePtr;
typedef boost::shared_ptr< ::autonomous_navigation::RoverState const> RoverStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::autonomous_navigation::RoverState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::autonomous_navigation::RoverState_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::autonomous_navigation::RoverState_<ContainerAllocator1> & lhs, const ::autonomous_navigation::RoverState_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.theta == rhs.theta;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::autonomous_navigation::RoverState_<ContainerAllocator1> & lhs, const ::autonomous_navigation::RoverState_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace autonomous_navigation

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::autonomous_navigation::RoverState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::autonomous_navigation::RoverState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::autonomous_navigation::RoverState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::autonomous_navigation::RoverState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::autonomous_navigation::RoverState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::autonomous_navigation::RoverState_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::autonomous_navigation::RoverState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a130bc60ee6513855dc62ea83fcc5b20";
  }

  static const char* value(const ::autonomous_navigation::RoverState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa130bc60ee651385ULL;
  static const uint64_t static_value2 = 0x5dc62ea83fcc5b20ULL;
};

template<class ContainerAllocator>
struct DataType< ::autonomous_navigation::RoverState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "autonomous_navigation/RoverState";
  }

  static const char* value(const ::autonomous_navigation::RoverState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::autonomous_navigation::RoverState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
"float32 theta\n"
;
  }

  static const char* value(const ::autonomous_navigation::RoverState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::autonomous_navigation::RoverState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.theta);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RoverState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonomous_navigation::RoverState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::autonomous_navigation::RoverState_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "theta: ";
    Printer<float>::stream(s, indent + "  ", v.theta);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AUTONOMOUS_NAVIGATION_MESSAGE_ROVERSTATE_H
