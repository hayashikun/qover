# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/testdata/zoo_mutator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/testdata/zoo_mutator.proto',
  package='google_zoo',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.mediapipe/framework/testdata/zoo_mutator.proto\x12\ngoogle_zoo\x1a\x19google/protobuf/any.proto\"C\n\x13\x44ragonMutatorConfig\x12\x15\n\rdragon_factor\x18\x01 \x01(\x01\x12\x15\n\rdragon_params\x18\x02 \x01(\t\"w\n\x10ZooMutatorConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rinstance_name\x18\x02 \x01(\t\x12*\n\nsub_config\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x12\n\x10sub_config_oneofb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_DRAGONMUTATORCONFIG = _descriptor.Descriptor(
  name='DragonMutatorConfig',
  full_name='google_zoo.DragonMutatorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dragon_factor', full_name='google_zoo.DragonMutatorConfig.dragon_factor', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dragon_params', full_name='google_zoo.DragonMutatorConfig.dragon_params', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=89,
  serialized_end=156,
)


_ZOOMUTATORCONFIG = _descriptor.Descriptor(
  name='ZooMutatorConfig',
  full_name='google_zoo.ZooMutatorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google_zoo.ZooMutatorConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='google_zoo.ZooMutatorConfig.instance_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_config', full_name='google_zoo.ZooMutatorConfig.sub_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='sub_config_oneof', full_name='google_zoo.ZooMutatorConfig.sub_config_oneof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=158,
  serialized_end=277,
)

_ZOOMUTATORCONFIG.fields_by_name['sub_config'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ZOOMUTATORCONFIG.oneofs_by_name['sub_config_oneof'].fields.append(
  _ZOOMUTATORCONFIG.fields_by_name['sub_config'])
_ZOOMUTATORCONFIG.fields_by_name['sub_config'].containing_oneof = _ZOOMUTATORCONFIG.oneofs_by_name['sub_config_oneof']
DESCRIPTOR.message_types_by_name['DragonMutatorConfig'] = _DRAGONMUTATORCONFIG
DESCRIPTOR.message_types_by_name['ZooMutatorConfig'] = _ZOOMUTATORCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DragonMutatorConfig = _reflection.GeneratedProtocolMessageType('DragonMutatorConfig', (_message.Message,), {
  'DESCRIPTOR' : _DRAGONMUTATORCONFIG,
  '__module__' : 'mediapipe.framework.testdata.zoo_mutator_pb2'
  # @@protoc_insertion_point(class_scope:google_zoo.DragonMutatorConfig)
  })
_sym_db.RegisterMessage(DragonMutatorConfig)

ZooMutatorConfig = _reflection.GeneratedProtocolMessageType('ZooMutatorConfig', (_message.Message,), {
  'DESCRIPTOR' : _ZOOMUTATORCONFIG,
  '__module__' : 'mediapipe.framework.testdata.zoo_mutator_pb2'
  # @@protoc_insertion_point(class_scope:google_zoo.ZooMutatorConfig)
  })
_sym_db.RegisterMessage(ZooMutatorConfig)


# @@protoc_insertion_point(module_scope)
