# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qoin/proto/hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='qoin/proto/hello.proto',
  package='qoin',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16qoin/proto/hello.proto\x12\x04qoin\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xaf\x01\n\x07Greeter\x12\x32\n\x08SayHello\x12\x12.qoin.HelloRequest\x1a\x10.qoin.HelloReply\"\x00\x12\x37\n\rSayHelloAgain\x12\x12.qoin.HelloRequest\x1a\x10.qoin.HelloReply\"\x00\x12\x37\n\x0bHelloStream\x12\x12.qoin.HelloRequest\x1a\x10.qoin.HelloReply\"\x00\x30\x01\x62\x06proto3'
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='qoin.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='qoin.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=60,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='qoin.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='qoin.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=62,
  serialized_end=91,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'qoin.proto.hello_pb2'
  # @@protoc_insertion_point(class_scope:qoin.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'qoin.proto.hello_pb2'
  # @@protoc_insertion_point(class_scope:qoin.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='qoin.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=94,
  serialized_end=269,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='qoin.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloAgain',
    full_name='qoin.Greeter.SayHelloAgain',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HelloStream',
    full_name='qoin.Greeter.HelloStream',
    index=2,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
