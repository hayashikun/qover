# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qoin/proto/hand_tracking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework.formats import landmark_pb2 as mediapipe_dot_framework_dot_formats_dot_landmark__pb2
from mediapipe.framework.formats import detection_pb2 as mediapipe_dot_framework_dot_formats_dot_detection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qoin/proto/hand_tracking.proto',
  package='qoin',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eqoin/proto/hand_tracking.proto\x12\x04qoin\x1a*mediapipe/framework/formats/landmark.proto\x1a+mediapipe/framework/formats/detection.proto\"\x19\n\x17HandTrackingPullRequest\"z\n\x15HandTrackingPullReply\x12\'\n\tdetection\x18\x01 \x03(\x0b\x32\x14.mediapipe.Detection\x12\x38\n\rlandmark_list\x18\x02 \x01(\x0b\x32!.mediapipe.NormalizedLandmarkList\"|\n\x17HandTrackingPushRequest\x12\'\n\tdetection\x18\x01 \x03(\x0b\x32\x14.mediapipe.Detection\x12\x38\n\rlandmark_list\x18\x02 \x01(\x0b\x32!.mediapipe.NormalizedLandmarkList\"\x17\n\x15HandTrackingPushReply2\xc2\x01\n\x0cHandTracking\x12X\n\x16HandTrackingPullStream\x12\x1d.qoin.HandTrackingPullRequest\x1a\x1b.qoin.HandTrackingPullReply\"\x00\x30\x01\x12X\n\x16HandTrackingPushStream\x12\x1d.qoin.HandTrackingPushRequest\x1a\x1b.qoin.HandTrackingPushReply\"\x00(\x01\x62\x06proto3'
  ,
  dependencies=[mediapipe_dot_framework_dot_formats_dot_landmark__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_formats_dot_detection__pb2.DESCRIPTOR,])




_HANDTRACKINGPULLREQUEST = _descriptor.Descriptor(
  name='HandTrackingPullRequest',
  full_name='qoin.HandTrackingPullRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=154,
)


_HANDTRACKINGPULLREPLY = _descriptor.Descriptor(
  name='HandTrackingPullReply',
  full_name='qoin.HandTrackingPullReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='detection', full_name='qoin.HandTrackingPullReply.detection', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='landmark_list', full_name='qoin.HandTrackingPullReply.landmark_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=278,
)


_HANDTRACKINGPUSHREQUEST = _descriptor.Descriptor(
  name='HandTrackingPushRequest',
  full_name='qoin.HandTrackingPushRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='detection', full_name='qoin.HandTrackingPushRequest.detection', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='landmark_list', full_name='qoin.HandTrackingPushRequest.landmark_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=404,
)


_HANDTRACKINGPUSHREPLY = _descriptor.Descriptor(
  name='HandTrackingPushReply',
  full_name='qoin.HandTrackingPushReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=429,
)

_HANDTRACKINGPULLREPLY.fields_by_name['detection'].message_type = mediapipe_dot_framework_dot_formats_dot_detection__pb2._DETECTION
_HANDTRACKINGPULLREPLY.fields_by_name['landmark_list'].message_type = mediapipe_dot_framework_dot_formats_dot_landmark__pb2._NORMALIZEDLANDMARKLIST
_HANDTRACKINGPUSHREQUEST.fields_by_name['detection'].message_type = mediapipe_dot_framework_dot_formats_dot_detection__pb2._DETECTION
_HANDTRACKINGPUSHREQUEST.fields_by_name['landmark_list'].message_type = mediapipe_dot_framework_dot_formats_dot_landmark__pb2._NORMALIZEDLANDMARKLIST
DESCRIPTOR.message_types_by_name['HandTrackingPullRequest'] = _HANDTRACKINGPULLREQUEST
DESCRIPTOR.message_types_by_name['HandTrackingPullReply'] = _HANDTRACKINGPULLREPLY
DESCRIPTOR.message_types_by_name['HandTrackingPushRequest'] = _HANDTRACKINGPUSHREQUEST
DESCRIPTOR.message_types_by_name['HandTrackingPushReply'] = _HANDTRACKINGPUSHREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HandTrackingPullRequest = _reflection.GeneratedProtocolMessageType('HandTrackingPullRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDTRACKINGPULLREQUEST,
  '__module__' : 'qoin.proto.hand_tracking_pb2'
  # @@protoc_insertion_point(class_scope:qoin.HandTrackingPullRequest)
  })
_sym_db.RegisterMessage(HandTrackingPullRequest)

HandTrackingPullReply = _reflection.GeneratedProtocolMessageType('HandTrackingPullReply', (_message.Message,), {
  'DESCRIPTOR' : _HANDTRACKINGPULLREPLY,
  '__module__' : 'qoin.proto.hand_tracking_pb2'
  # @@protoc_insertion_point(class_scope:qoin.HandTrackingPullReply)
  })
_sym_db.RegisterMessage(HandTrackingPullReply)

HandTrackingPushRequest = _reflection.GeneratedProtocolMessageType('HandTrackingPushRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDTRACKINGPUSHREQUEST,
  '__module__' : 'qoin.proto.hand_tracking_pb2'
  # @@protoc_insertion_point(class_scope:qoin.HandTrackingPushRequest)
  })
_sym_db.RegisterMessage(HandTrackingPushRequest)

HandTrackingPushReply = _reflection.GeneratedProtocolMessageType('HandTrackingPushReply', (_message.Message,), {
  'DESCRIPTOR' : _HANDTRACKINGPUSHREPLY,
  '__module__' : 'qoin.proto.hand_tracking_pb2'
  # @@protoc_insertion_point(class_scope:qoin.HandTrackingPushReply)
  })
_sym_db.RegisterMessage(HandTrackingPushReply)



_HANDTRACKING = _descriptor.ServiceDescriptor(
  name='HandTracking',
  full_name='qoin.HandTracking',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=432,
  serialized_end=626,
  methods=[
  _descriptor.MethodDescriptor(
    name='HandTrackingPullStream',
    full_name='qoin.HandTracking.HandTrackingPullStream',
    index=0,
    containing_service=None,
    input_type=_HANDTRACKINGPULLREQUEST,
    output_type=_HANDTRACKINGPULLREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandTrackingPushStream',
    full_name='qoin.HandTracking.HandTrackingPushStream',
    index=1,
    containing_service=None,
    input_type=_HANDTRACKINGPUSHREQUEST,
    output_type=_HANDTRACKINGPUSHREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HANDTRACKING)

DESCRIPTOR.services_by_name['HandTracking'] = _HANDTRACKING

# @@protoc_insertion_point(module_scope)
