# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dashboard.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dashboard.proto',
  package='GmuRoboticsCode',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x64\x61shboard.proto\x12\x0fGmuRoboticsCode\"\xb1\x01\n\nRobotStaus\x12\x13\n\x0brobot_state\x18\x01 \x01(\x08\x1aL\n\x04\x61xes\x12\x0c\n\x04joy1\x18\x01 \x01(\x01\x12\x0c\n\x04joy2\x18\x02 \x01(\x01\x12\x0c\n\x04joy3\x18\x03 \x01(\x01\x12\x0c\n\x04joy4\x18\x04 \x01(\x01\x12\x0c\n\x04joy5\x18\x05 \x01(\x01\x1a@\n\x06\x62utton\x12\x0c\n\x04\x62utA\x18\x01 \x01(\x08\x12\x0c\n\x04\x62utB\x18\x02 \x01(\x08\x12\x0c\n\x04\x62utX\x18\x03 \x01(\x08\x12\x0c\n\x04\x62utY\x18\x04 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ROBOTSTAUS_AXES = _descriptor.Descriptor(
  name='axes',
  full_name='GmuRoboticsCode.RobotStaus.axes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='joy1', full_name='GmuRoboticsCode.RobotStaus.axes.joy1', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joy2', full_name='GmuRoboticsCode.RobotStaus.axes.joy2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joy3', full_name='GmuRoboticsCode.RobotStaus.axes.joy3', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joy4', full_name='GmuRoboticsCode.RobotStaus.axes.joy4', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joy5', full_name='GmuRoboticsCode.RobotStaus.axes.joy5', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=148,
)

_ROBOTSTAUS_BUTTON = _descriptor.Descriptor(
  name='button',
  full_name='GmuRoboticsCode.RobotStaus.button',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='butA', full_name='GmuRoboticsCode.RobotStaus.button.butA', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='butB', full_name='GmuRoboticsCode.RobotStaus.button.butB', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='butX', full_name='GmuRoboticsCode.RobotStaus.button.butX', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='butY', full_name='GmuRoboticsCode.RobotStaus.button.butY', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=214,
)

_ROBOTSTAUS = _descriptor.Descriptor(
  name='RobotStaus',
  full_name='GmuRoboticsCode.RobotStaus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_state', full_name='GmuRoboticsCode.RobotStaus.robot_state', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROBOTSTAUS_AXES, _ROBOTSTAUS_BUTTON, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=214,
)

_ROBOTSTAUS_AXES.containing_type = _ROBOTSTAUS
_ROBOTSTAUS_BUTTON.containing_type = _ROBOTSTAUS
DESCRIPTOR.message_types_by_name['RobotStaus'] = _ROBOTSTAUS

RobotStaus = _reflection.GeneratedProtocolMessageType('RobotStaus', (_message.Message,), dict(

  axes = _reflection.GeneratedProtocolMessageType('axes', (_message.Message,), dict(
    DESCRIPTOR = _ROBOTSTAUS_AXES,
    __module__ = 'dashboard_pb2'
    # @@protoc_insertion_point(class_scope:GmuRoboticsCode.RobotStaus.axes)
    ))
  ,

  button = _reflection.GeneratedProtocolMessageType('button', (_message.Message,), dict(
    DESCRIPTOR = _ROBOTSTAUS_BUTTON,
    __module__ = 'dashboard_pb2'
    # @@protoc_insertion_point(class_scope:GmuRoboticsCode.RobotStaus.button)
    ))
  ,
  DESCRIPTOR = _ROBOTSTAUS,
  __module__ = 'dashboard_pb2'
  # @@protoc_insertion_point(class_scope:GmuRoboticsCode.RobotStaus)
  ))
_sym_db.RegisterMessage(RobotStaus)
_sym_db.RegisterMessage(RobotStaus.axes)
_sym_db.RegisterMessage(RobotStaus.button)


# @@protoc_insertion_point(module_scope)
