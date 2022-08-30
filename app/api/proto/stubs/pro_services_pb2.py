# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pro_services.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pro_services.proto',
  package='tracardi_pro',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12pro_services.proto\x12\x0ctracardi_pro\x1a\x1cgoogle/protobuf/struct.proto\"\r\n\x0b\x45mptyParams\"\x8f\x01\n\x0fServiceMetadata\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07traffic\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x0e\n\x06submit\x18\x07 \x03(\t\x12\x0e\n\x06prefix\x18\x08 \x01(\t\"\x91\x01\n\x08Services\x12\x36\n\x08services\x18\x01 \x03(\x0b\x32$.tracardi_pro.Services.ServicesEntry\x1aM\n\rServicesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.tracardi_pro.ServiceEnvelop:\x02\x38\x01\" \n\x0ePluginMetaData\x12\x0e\n\x06module\x18\x01 \x01(\t\"V\n\x06Plugin\x12%\n\x04init\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04\x66orm\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x16\n\x05Hosts\x12\r\n\x05hosts\x18\x01 \x03(\t\"\xe6\x01\n\x0eServiceEnvelop\x12/\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.tracardi_pro.ServiceMetadata\x12%\n\x04\x66orm\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04init\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0b\x64\x65stination\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06plugin\x18\x05 \x03(\x0b\x32\x17.google.protobuf.Struct\"1\n\x0b\x43redentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"C\n\x0fHostCredentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\"\x16\n\x05Token\x12\r\n\x05token\x18\x01 \x01(\t\"\'\n\x08UserData\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t2\xdb\x02\n\x07Service\x12M\n\x16get_available_services\x12\x19.tracardi_pro.EmptyParams\x1a\x16.tracardi_pro.Services\"\x00\x12\x42\n\nget_plugin\x12\x1c.tracardi_pro.PluginMetaData\x1a\x14.tracardi_pro.Plugin\"\x00\x12?\n\x07sign_up\x12\x1d.tracardi_pro.HostCredentials\x1a\x13.tracardi_pro.Token\"\x00\x12>\n\x07sign_in\x12\x19.tracardi_pro.Credentials\x1a\x16.tracardi_pro.UserData\"\x00\x12<\n\x08validate\x12\x19.tracardi_pro.EmptyParams\x1a\x13.tracardi_pro.Token\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_EMPTYPARAMS = _descriptor.Descriptor(
  name='EmptyParams',
  full_name='tracardi_pro.EmptyParams',
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
  serialized_start=66,
  serialized_end=79,
)


_SERVICEMETADATA = _descriptor.Descriptor(
  name='ServiceMetadata',
  full_name='tracardi_pro.ServiceMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='tracardi_pro.ServiceMetadata.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='tracardi_pro.ServiceMetadata.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='tracardi_pro.ServiceMetadata.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traffic', full_name='tracardi_pro.ServiceMetadata.traffic', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icon', full_name='tracardi_pro.ServiceMetadata.icon', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='tracardi_pro.ServiceMetadata.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submit', full_name='tracardi_pro.ServiceMetadata.submit', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='tracardi_pro.ServiceMetadata.prefix', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=82,
  serialized_end=225,
)


_SERVICES_SERVICESENTRY = _descriptor.Descriptor(
  name='ServicesEntry',
  full_name='tracardi_pro.Services.ServicesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tracardi_pro.Services.ServicesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='tracardi_pro.Services.ServicesEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=373,
)

_SERVICES = _descriptor.Descriptor(
  name='Services',
  full_name='tracardi_pro.Services',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='tracardi_pro.Services.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SERVICES_SERVICESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=373,
)


_PLUGINMETADATA = _descriptor.Descriptor(
  name='PluginMetaData',
  full_name='tracardi_pro.PluginMetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='module', full_name='tracardi_pro.PluginMetaData.module', index=0,
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
  serialized_start=375,
  serialized_end=407,
)


_PLUGIN = _descriptor.Descriptor(
  name='Plugin',
  full_name='tracardi_pro.Plugin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='init', full_name='tracardi_pro.Plugin.init', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='form', full_name='tracardi_pro.Plugin.form', index=1,
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
  serialized_start=409,
  serialized_end=495,
)


_HOSTS = _descriptor.Descriptor(
  name='Hosts',
  full_name='tracardi_pro.Hosts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='tracardi_pro.Hosts.hosts', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=497,
  serialized_end=519,
)


_SERVICEENVELOP = _descriptor.Descriptor(
  name='ServiceEnvelop',
  full_name='tracardi_pro.ServiceEnvelop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tracardi_pro.ServiceEnvelop.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='form', full_name='tracardi_pro.ServiceEnvelop.form', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init', full_name='tracardi_pro.ServiceEnvelop.init', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination', full_name='tracardi_pro.ServiceEnvelop.destination', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plugin', full_name='tracardi_pro.ServiceEnvelop.plugin', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=522,
  serialized_end=752,
)


_CREDENTIALS = _descriptor.Descriptor(
  name='Credentials',
  full_name='tracardi_pro.Credentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='tracardi_pro.Credentials.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='tracardi_pro.Credentials.password', index=1,
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
  serialized_start=754,
  serialized_end=803,
)


_HOSTCREDENTIALS = _descriptor.Descriptor(
  name='HostCredentials',
  full_name='tracardi_pro.HostCredentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='tracardi_pro.HostCredentials.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='tracardi_pro.HostCredentials.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='tracardi_pro.HostCredentials.host', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=805,
  serialized_end=872,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='tracardi_pro.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='tracardi_pro.Token.token', index=0,
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
  serialized_start=874,
  serialized_end=896,
)


_USERDATA = _descriptor.Descriptor(
  name='UserData',
  full_name='tracardi_pro.UserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='tracardi_pro.UserData.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='tracardi_pro.UserData.host', index=1,
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
  serialized_start=898,
  serialized_end=937,
)

_SERVICES_SERVICESENTRY.fields_by_name['value'].message_type = _SERVICEENVELOP
_SERVICES_SERVICESENTRY.containing_type = _SERVICES
_SERVICES.fields_by_name['services'].message_type = _SERVICES_SERVICESENTRY
_PLUGIN.fields_by_name['init'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_PLUGIN.fields_by_name['form'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICEENVELOP.fields_by_name['metadata'].message_type = _SERVICEMETADATA
_SERVICEENVELOP.fields_by_name['form'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICEENVELOP.fields_by_name['init'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICEENVELOP.fields_by_name['destination'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICEENVELOP.fields_by_name['plugin'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['EmptyParams'] = _EMPTYPARAMS
DESCRIPTOR.message_types_by_name['ServiceMetadata'] = _SERVICEMETADATA
DESCRIPTOR.message_types_by_name['Services'] = _SERVICES
DESCRIPTOR.message_types_by_name['PluginMetaData'] = _PLUGINMETADATA
DESCRIPTOR.message_types_by_name['Plugin'] = _PLUGIN
DESCRIPTOR.message_types_by_name['Hosts'] = _HOSTS
DESCRIPTOR.message_types_by_name['ServiceEnvelop'] = _SERVICEENVELOP
DESCRIPTOR.message_types_by_name['Credentials'] = _CREDENTIALS
DESCRIPTOR.message_types_by_name['HostCredentials'] = _HOSTCREDENTIALS
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['UserData'] = _USERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyParams = _reflection.GeneratedProtocolMessageType('EmptyParams', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYPARAMS,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.EmptyParams)
  })
_sym_db.RegisterMessage(EmptyParams)

ServiceMetadata = _reflection.GeneratedProtocolMessageType('ServiceMetadata', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEMETADATA,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.ServiceMetadata)
  })
_sym_db.RegisterMessage(ServiceMetadata)

Services = _reflection.GeneratedProtocolMessageType('Services', (_message.Message,), {

  'ServicesEntry' : _reflection.GeneratedProtocolMessageType('ServicesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVICES_SERVICESENTRY,
    '__module__' : 'pro_services_pb2'
    # @@protoc_insertion_point(class_scope:tracardi_pro.Services.ServicesEntry)
    })
  ,
  'DESCRIPTOR' : _SERVICES,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.Services)
  })
_sym_db.RegisterMessage(Services)
_sym_db.RegisterMessage(Services.ServicesEntry)

PluginMetaData = _reflection.GeneratedProtocolMessageType('PluginMetaData', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINMETADATA,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.PluginMetaData)
  })
_sym_db.RegisterMessage(PluginMetaData)

Plugin = _reflection.GeneratedProtocolMessageType('Plugin', (_message.Message,), {
  'DESCRIPTOR' : _PLUGIN,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.Plugin)
  })
_sym_db.RegisterMessage(Plugin)

Hosts = _reflection.GeneratedProtocolMessageType('Hosts', (_message.Message,), {
  'DESCRIPTOR' : _HOSTS,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.Hosts)
  })
_sym_db.RegisterMessage(Hosts)

ServiceEnvelop = _reflection.GeneratedProtocolMessageType('ServiceEnvelop', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEENVELOP,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.ServiceEnvelop)
  })
_sym_db.RegisterMessage(ServiceEnvelop)

Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIALS,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.Credentials)
  })
_sym_db.RegisterMessage(Credentials)

HostCredentials = _reflection.GeneratedProtocolMessageType('HostCredentials', (_message.Message,), {
  'DESCRIPTOR' : _HOSTCREDENTIALS,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.HostCredentials)
  })
_sym_db.RegisterMessage(HostCredentials)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.Token)
  })
_sym_db.RegisterMessage(Token)

UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), {
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'pro_services_pb2'
  # @@protoc_insertion_point(class_scope:tracardi_pro.UserData)
  })
_sym_db.RegisterMessage(UserData)


_SERVICES_SERVICESENTRY._options = None

_SERVICE = _descriptor.ServiceDescriptor(
  name='Service',
  full_name='tracardi_pro.Service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=940,
  serialized_end=1287,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_available_services',
    full_name='tracardi_pro.Service.get_available_services',
    index=0,
    containing_service=None,
    input_type=_EMPTYPARAMS,
    output_type=_SERVICES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_plugin',
    full_name='tracardi_pro.Service.get_plugin',
    index=1,
    containing_service=None,
    input_type=_PLUGINMETADATA,
    output_type=_PLUGIN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sign_up',
    full_name='tracardi_pro.Service.sign_up',
    index=2,
    containing_service=None,
    input_type=_HOSTCREDENTIALS,
    output_type=_TOKEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sign_in',
    full_name='tracardi_pro.Service.sign_in',
    index=3,
    containing_service=None,
    input_type=_CREDENTIALS,
    output_type=_USERDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='validate',
    full_name='tracardi_pro.Service.validate',
    index=4,
    containing_service=None,
    input_type=_EMPTYPARAMS,
    output_type=_TOKEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name['Service'] = _SERVICE

# @@protoc_insertion_point(module_scope)
