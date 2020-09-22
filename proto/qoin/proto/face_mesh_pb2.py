# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qoin/proto/face_mesh.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework.formats import landmark_pb2 as mediapipe_dot_framework_dot_formats_dot_landmark__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qoin/proto/face_mesh.proto',
  package='qoin',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aqoin/proto/face_mesh.proto\x12\x04qoin\x1a*mediapipe/framework/formats/landmark.proto\"\x15\n\x13\x46\x61\x63\x65MeshPullRequest\"M\n\x11\x46\x61\x63\x65MeshPullReply\x12\x38\n\rlandmark_list\x18\x01 \x03(\x0b\x32!.mediapipe.NormalizedLandmarkList\"O\n\x13\x46\x61\x63\x65MeshPushRequest\x12\x38\n\rlandmark_list\x18\x01 \x03(\x0b\x32!.mediapipe.NormalizedLandmarkList\"\x13\n\x11\x46\x61\x63\x65MeshPushReply2\xa6\x01\n\x08\x46\x61\x63\x65Mesh\x12L\n\x12\x46\x61\x63\x65MeshPullStream\x12\x19.qoin.FaceMeshPullRequest\x1a\x17.qoin.FaceMeshPullReply\"\x00\x30\x01\x12L\n\x12\x46\x61\x63\x65MeshPushStream\x12\x19.qoin.FaceMeshPushRequest\x1a\x17.qoin.FaceMeshPushReply\"\x00(\x01\x62\x06proto3'
  ,
  dependencies=[mediapipe_dot_framework_dot_formats_dot_landmark__pb2.DESCRIPTOR,])




_FACEMESHPULLREQUEST = _descriptor.Descriptor(
  name='FaceMeshPullRequest',
  full_name='qoin.FaceMeshPullRequest',
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
  serialized_start=80,
  serialized_end=101,
)


_FACEMESHPULLREPLY = _descriptor.Descriptor(
  name='FaceMeshPullReply',
  full_name='qoin.FaceMeshPullReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='landmark_list', full_name='qoin.FaceMeshPullReply.landmark_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=103,
  serialized_end=180,
)


_FACEMESHPUSHREQUEST = _descriptor.Descriptor(
  name='FaceMeshPushRequest',
  full_name='qoin.FaceMeshPushRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='landmark_list', full_name='qoin.FaceMeshPushRequest.landmark_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=182,
  serialized_end=261,
)


_FACEMESHPUSHREPLY = _descriptor.Descriptor(
  name='FaceMeshPushReply',
  full_name='qoin.FaceMeshPushReply',
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
  serialized_start=263,
  serialized_end=282,
)

_FACEMESHPULLREPLY.fields_by_name['landmark_list'].message_type = mediapipe_dot_framework_dot_formats_dot_landmark__pb2._NORMALIZEDLANDMARKLIST
_FACEMESHPUSHREQUEST.fields_by_name['landmark_list'].message_type = mediapipe_dot_framework_dot_formats_dot_landmark__pb2._NORMALIZEDLANDMARKLIST
DESCRIPTOR.message_types_by_name['FaceMeshPullRequest'] = _FACEMESHPULLREQUEST
DESCRIPTOR.message_types_by_name['FaceMeshPullReply'] = _FACEMESHPULLREPLY
DESCRIPTOR.message_types_by_name['FaceMeshPushRequest'] = _FACEMESHPUSHREQUEST
DESCRIPTOR.message_types_by_name['FaceMeshPushReply'] = _FACEMESHPUSHREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaceMeshPullRequest = _reflection.GeneratedProtocolMessageType('FaceMeshPullRequest', (_message.Message,), {
  'DESCRIPTOR' : _FACEMESHPULLREQUEST,
  '__module__' : 'qoin.proto.face_mesh_pb2'
  # @@protoc_insertion_point(class_scope:qoin.FaceMeshPullRequest)
  })
_sym_db.RegisterMessage(FaceMeshPullRequest)

FaceMeshPullReply = _reflection.GeneratedProtocolMessageType('FaceMeshPullReply', (_message.Message,), {
  'DESCRIPTOR' : _FACEMESHPULLREPLY,
  '__module__' : 'qoin.proto.face_mesh_pb2'
  # @@protoc_insertion_point(class_scope:qoin.FaceMeshPullReply)
  })
_sym_db.RegisterMessage(FaceMeshPullReply)

FaceMeshPushRequest = _reflection.GeneratedProtocolMessageType('FaceMeshPushRequest', (_message.Message,), {
  'DESCRIPTOR' : _FACEMESHPUSHREQUEST,
  '__module__' : 'qoin.proto.face_mesh_pb2'
  # @@protoc_insertion_point(class_scope:qoin.FaceMeshPushRequest)
  })
_sym_db.RegisterMessage(FaceMeshPushRequest)

FaceMeshPushReply = _reflection.GeneratedProtocolMessageType('FaceMeshPushReply', (_message.Message,), {
  'DESCRIPTOR' : _FACEMESHPUSHREPLY,
  '__module__' : 'qoin.proto.face_mesh_pb2'
  # @@protoc_insertion_point(class_scope:qoin.FaceMeshPushReply)
  })
_sym_db.RegisterMessage(FaceMeshPushReply)



_FACEMESH = _descriptor.ServiceDescriptor(
  name='FaceMesh',
  full_name='qoin.FaceMesh',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=285,
  serialized_end=451,
  methods=[
  _descriptor.MethodDescriptor(
    name='FaceMeshPullStream',
    full_name='qoin.FaceMesh.FaceMeshPullStream',
    index=0,
    containing_service=None,
    input_type=_FACEMESHPULLREQUEST,
    output_type=_FACEMESHPULLREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FaceMeshPushStream',
    full_name='qoin.FaceMesh.FaceMeshPushStream',
    index=1,
    containing_service=None,
    input_type=_FACEMESHPUSHREQUEST,
    output_type=_FACEMESHPUSHREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FACEMESH)

DESCRIPTOR.services_by_name['FaceMesh'] = _FACEMESH

# @@protoc_insertion_point(module_scope)