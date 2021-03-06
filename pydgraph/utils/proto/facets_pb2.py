# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facets.proto

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
  name='facets.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x66\x61\x63\x65ts.proto\x12\x06protos\"\x9f\x01\n\x05\x46\x61\x63\x65t\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\'\n\x08val_type\x18\x03 \x01(\x0e\x32\x15.protos.Facet.ValType\x12\x0e\n\x06tokens\x18\x04 \x03(\t\"A\n\x07ValType\x12\n\n\x06STRING\x10\x00\x12\x07\n\x03INT\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\x0c\n\x08\x44\x41TETIME\x10\x04\"\'\n\x05Param\x12\x10\n\x08\x61ll_keys\x18\x01 \x01(\x08\x12\x0c\n\x04keys\x18\x02 \x03(\t\"\'\n\x06\x46\x61\x63\x65ts\x12\x1d\n\x06\x66\x61\x63\x65ts\x18\x01 \x03(\x0b\x32\r.protos.Facet\"1\n\nFacetsList\x12#\n\x0b\x66\x61\x63\x65ts_list\x18\x01 \x03(\x0b\x32\x0e.protos.Facets\"3\n\x08\x46unction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\"^\n\nFilterTree\x12\n\n\x02op\x18\x01 \x01(\t\x12$\n\x08\x63hildren\x18\x02 \x03(\x0b\x32\x12.protos.FilterTree\x12\x1e\n\x04\x66unc\x18\x03 \x01(\x0b\x32\x10.protos.Functionb\x06proto3')
)



_FACET_VALTYPE = _descriptor.EnumDescriptor(
  name='ValType',
  full_name='protos.Facet.ValType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=119,
  serialized_end=184,
)
_sym_db.RegisterEnumDescriptor(_FACET_VALTYPE)


_FACET = _descriptor.Descriptor(
  name='Facet',
  full_name='protos.Facet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protos.Facet.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.Facet.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val_type', full_name='protos.Facet.val_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tokens', full_name='protos.Facet.tokens', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FACET_VALTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=184,
)


_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='protos.Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_keys', full_name='protos.Param.all_keys', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='protos.Param.keys', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=186,
  serialized_end=225,
)


_FACETS = _descriptor.Descriptor(
  name='Facets',
  full_name='protos.Facets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='facets', full_name='protos.Facets.facets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=227,
  serialized_end=266,
)


_FACETSLIST = _descriptor.Descriptor(
  name='FacetsList',
  full_name='protos.FacetsList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='facets_list', full_name='protos.FacetsList.facets_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=268,
  serialized_end=317,
)


_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='protos.Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protos.Function.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='protos.Function.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='protos.Function.args', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=319,
  serialized_end=370,
)


_FILTERTREE = _descriptor.Descriptor(
  name='FilterTree',
  full_name='protos.FilterTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='protos.FilterTree.op', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='children', full_name='protos.FilterTree.children', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func', full_name='protos.FilterTree.func', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=372,
  serialized_end=466,
)

_FACET.fields_by_name['val_type'].enum_type = _FACET_VALTYPE
_FACET_VALTYPE.containing_type = _FACET
_FACETS.fields_by_name['facets'].message_type = _FACET
_FACETSLIST.fields_by_name['facets_list'].message_type = _FACETS
_FILTERTREE.fields_by_name['children'].message_type = _FILTERTREE
_FILTERTREE.fields_by_name['func'].message_type = _FUNCTION
DESCRIPTOR.message_types_by_name['Facet'] = _FACET
DESCRIPTOR.message_types_by_name['Param'] = _PARAM
DESCRIPTOR.message_types_by_name['Facets'] = _FACETS
DESCRIPTOR.message_types_by_name['FacetsList'] = _FACETSLIST
DESCRIPTOR.message_types_by_name['Function'] = _FUNCTION
DESCRIPTOR.message_types_by_name['FilterTree'] = _FILTERTREE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Facet = _reflection.GeneratedProtocolMessageType('Facet', (_message.Message,), dict(
  DESCRIPTOR = _FACET,
  __module__ = 'facets_pb2'
  # @@protoc_insertion_point(class_scope:protos.Facet)
  ))
_sym_db.RegisterMessage(Facet)

Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), dict(
  DESCRIPTOR = _PARAM,
  __module__ = 'facets_pb2'
  # @@protoc_insertion_point(class_scope:protos.Param)
  ))
_sym_db.RegisterMessage(Param)

Facets = _reflection.GeneratedProtocolMessageType('Facets', (_message.Message,), dict(
  DESCRIPTOR = _FACETS,
  __module__ = 'facets_pb2'
  # @@protoc_insertion_point(class_scope:protos.Facets)
  ))
_sym_db.RegisterMessage(Facets)

FacetsList = _reflection.GeneratedProtocolMessageType('FacetsList', (_message.Message,), dict(
  DESCRIPTOR = _FACETSLIST,
  __module__ = 'facets_pb2'
  # @@protoc_insertion_point(class_scope:protos.FacetsList)
  ))
_sym_db.RegisterMessage(FacetsList)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTION,
  __module__ = 'facets_pb2'
  # @@protoc_insertion_point(class_scope:protos.Function)
  ))
_sym_db.RegisterMessage(Function)

FilterTree = _reflection.GeneratedProtocolMessageType('FilterTree', (_message.Message,), dict(
  DESCRIPTOR = _FILTERTREE,
  __module__ = 'facets_pb2'
  # @@protoc_insertion_point(class_scope:protos.FilterTree)
  ))
_sym_db.RegisterMessage(FilterTree)


# @@protoc_insertion_point(module_scope)