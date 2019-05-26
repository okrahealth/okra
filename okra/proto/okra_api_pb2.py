# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/okra_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/okra_api.proto',
  package='okra.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14proto/okra_api.proto\x12\x07okra.v1\"m\n\x12IsoDateAggregation\x12\x0e\n\x06yearmo\x18\x01 \x01(\t\x12\x13\n\x0b\x63ommit_hash\x18\x02 \x01(\t\x12\x10\n\x08iso_week\x18\x03 \x01(\x05\x12\x10\n\x08iso_year\x18\x04 \x01(\x05\x12\x0e\n\x06status\x18\x05 \x01(\t\"\xa8\x02\n\x17RepositoryHistoryMetric\x12\x0f\n\x07repo_id\x18\x01 \x01(\t\x12\x14\n\x0cstart_yearmo\x18\x02 \x01(\t\x12\x16\n\x0e\x63urrent_yearmo\x18\x03 \x01(\t\x12-\n\x08isodates\x18\x04 \x03(\x0b\x32\x1b.okra.v1.IsoDateAggregation\x12\x1a\n\x12last_commit_yearmo\x18\x05 \x01(\t\x12\x18\n\x10last_commit_hash\x18\x06 \x01(\t\x12\x19\n\x11total_lines_added\x18\x07 \x01(\x05\x12\x1e\n\x16total_lines_subtracted\x18\x08 \x01(\x05\x12\x1a\n\x12total_truck_factor\x18\t \x01(\x05\x12\x12\n\ntotal_days\x18\n \x01(\x02\"\xe8\x01\n\x10RepositoryMetric\x12\x0f\n\x07repo_id\x18\x01 \x01(\t\x12\x0e\n\x06yearmo\x18\x02 \x01(\t\x12-\n\x08isodates\x18\x03 \x03(\x0b\x32\x1b.okra.v1.IsoDateAggregation\x12\x14\n\x0c\x61uthor_count\x18\x04 \x01(\x05\x12\x15\n\rcontrib_count\x18\x05 \x01(\x05\x12\x12\n\nfile_count\x18\x06 \x01(\x05\x12\x13\n\x0blines_added\x18\x07 \x01(\x05\x12\x18\n\x10lines_subtracted\x18\x08 \x01(\x05\x12\x14\n\x0ctruck_factor\x18\t \x01(\x05\"`\n\x0eRepositoryInfo\x12\x0f\n\x07repo_id\x18\x01 \x01(\t\x12\x0e\n\x06yearmo\x18\x02 \x01(\t\x12-\n\x08isodates\x18\x03 \x03(\x0b\x32\x1b.okra.v1.IsoDateAggregationb\x06proto3')
)




_ISODATEAGGREGATION = _descriptor.Descriptor(
  name='IsoDateAggregation',
  full_name='okra.v1.IsoDateAggregation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='yearmo', full_name='okra.v1.IsoDateAggregation.yearmo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_hash', full_name='okra.v1.IsoDateAggregation.commit_hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iso_week', full_name='okra.v1.IsoDateAggregation.iso_week', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iso_year', full_name='okra.v1.IsoDateAggregation.iso_year', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='okra.v1.IsoDateAggregation.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=33,
  serialized_end=142,
)


_REPOSITORYHISTORYMETRIC = _descriptor.Descriptor(
  name='RepositoryHistoryMetric',
  full_name='okra.v1.RepositoryHistoryMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_id', full_name='okra.v1.RepositoryHistoryMetric.repo_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_yearmo', full_name='okra.v1.RepositoryHistoryMetric.start_yearmo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_yearmo', full_name='okra.v1.RepositoryHistoryMetric.current_yearmo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isodates', full_name='okra.v1.RepositoryHistoryMetric.isodates', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_commit_yearmo', full_name='okra.v1.RepositoryHistoryMetric.last_commit_yearmo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_commit_hash', full_name='okra.v1.RepositoryHistoryMetric.last_commit_hash', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_lines_added', full_name='okra.v1.RepositoryHistoryMetric.total_lines_added', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_lines_subtracted', full_name='okra.v1.RepositoryHistoryMetric.total_lines_subtracted', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_truck_factor', full_name='okra.v1.RepositoryHistoryMetric.total_truck_factor', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_days', full_name='okra.v1.RepositoryHistoryMetric.total_days', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=145,
  serialized_end=441,
)


_REPOSITORYMETRIC = _descriptor.Descriptor(
  name='RepositoryMetric',
  full_name='okra.v1.RepositoryMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_id', full_name='okra.v1.RepositoryMetric.repo_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yearmo', full_name='okra.v1.RepositoryMetric.yearmo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isodates', full_name='okra.v1.RepositoryMetric.isodates', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_count', full_name='okra.v1.RepositoryMetric.author_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contrib_count', full_name='okra.v1.RepositoryMetric.contrib_count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_count', full_name='okra.v1.RepositoryMetric.file_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lines_added', full_name='okra.v1.RepositoryMetric.lines_added', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lines_subtracted', full_name='okra.v1.RepositoryMetric.lines_subtracted', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truck_factor', full_name='okra.v1.RepositoryMetric.truck_factor', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=444,
  serialized_end=676,
)


_REPOSITORYINFO = _descriptor.Descriptor(
  name='RepositoryInfo',
  full_name='okra.v1.RepositoryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_id', full_name='okra.v1.RepositoryInfo.repo_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yearmo', full_name='okra.v1.RepositoryInfo.yearmo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isodates', full_name='okra.v1.RepositoryInfo.isodates', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=678,
  serialized_end=774,
)

_REPOSITORYHISTORYMETRIC.fields_by_name['isodates'].message_type = _ISODATEAGGREGATION
_REPOSITORYMETRIC.fields_by_name['isodates'].message_type = _ISODATEAGGREGATION
_REPOSITORYINFO.fields_by_name['isodates'].message_type = _ISODATEAGGREGATION
DESCRIPTOR.message_types_by_name['IsoDateAggregation'] = _ISODATEAGGREGATION
DESCRIPTOR.message_types_by_name['RepositoryHistoryMetric'] = _REPOSITORYHISTORYMETRIC
DESCRIPTOR.message_types_by_name['RepositoryMetric'] = _REPOSITORYMETRIC
DESCRIPTOR.message_types_by_name['RepositoryInfo'] = _REPOSITORYINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IsoDateAggregation = _reflection.GeneratedProtocolMessageType('IsoDateAggregation', (_message.Message,), dict(
  DESCRIPTOR = _ISODATEAGGREGATION,
  __module__ = 'proto.okra_api_pb2'
  # @@protoc_insertion_point(class_scope:okra.v1.IsoDateAggregation)
  ))
_sym_db.RegisterMessage(IsoDateAggregation)

RepositoryHistoryMetric = _reflection.GeneratedProtocolMessageType('RepositoryHistoryMetric', (_message.Message,), dict(
  DESCRIPTOR = _REPOSITORYHISTORYMETRIC,
  __module__ = 'proto.okra_api_pb2'
  # @@protoc_insertion_point(class_scope:okra.v1.RepositoryHistoryMetric)
  ))
_sym_db.RegisterMessage(RepositoryHistoryMetric)

RepositoryMetric = _reflection.GeneratedProtocolMessageType('RepositoryMetric', (_message.Message,), dict(
  DESCRIPTOR = _REPOSITORYMETRIC,
  __module__ = 'proto.okra_api_pb2'
  # @@protoc_insertion_point(class_scope:okra.v1.RepositoryMetric)
  ))
_sym_db.RegisterMessage(RepositoryMetric)

RepositoryInfo = _reflection.GeneratedProtocolMessageType('RepositoryInfo', (_message.Message,), dict(
  DESCRIPTOR = _REPOSITORYINFO,
  __module__ = 'proto.okra_api_pb2'
  # @@protoc_insertion_point(class_scope:okra.v1.RepositoryInfo)
  ))
_sym_db.RegisterMessage(RepositoryInfo)


# @@protoc_insertion_point(module_scope)