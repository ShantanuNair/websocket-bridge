# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/jarvis_proto/audio.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/jarvis_proto/audio.proto',
  package='nvidia.jarvis',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n\x1csrc/jarvis_proto/audio.proto\x12\rnvidia.jarvis*,\n\rAudioEncoding\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nLINEAR_PCM\x10\x01\x42\x03\xf8\x01\x01\x62\x06proto3')
)

_AUDIOENCODING = _descriptor.EnumDescriptor(
  name='AudioEncoding',
  full_name='nvidia.jarvis.AudioEncoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINEAR_PCM', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=47,
  serialized_end=91,
)
_sym_db.RegisterEnumDescriptor(_AUDIOENCODING)

AudioEncoding = enum_type_wrapper.EnumTypeWrapper(_AUDIOENCODING)
UNKNOWN = 0
LINEAR_PCM = 1


DESCRIPTOR.enum_types_by_name['AudioEncoding'] = _AUDIOENCODING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
