# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: administracion.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61\x64ministracion.proto\x12\nvendedores\"\x07\n\x05\x45mpty\"*\n\x06Status\x12\x14\n\x07success\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\n\n\x08_success\"p\n\x08Producto\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x08\x63\x61ntidad\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x18\n\x0b\x64\x65scripcion\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x05\n\x03_idB\x0b\n\t_cantidadB\x0e\n\x0c_descripcion\"\x88\x01\n\x10RegistroVendedor\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06nombre\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04\x65\x64\x61\x64\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x14\n\x07salario\x18\x04 \x01(\x02H\x03\x88\x01\x01\x42\x05\n\x03_idB\t\n\x07_nombreB\x07\n\x05_edadB\n\n\x08_salario\"z\n\x0eRegistroTienda\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scripcion\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\ndelegacion\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x05\n\x03_idB\x0e\n\x0c_descripcionB\r\n\x0b_delegacion\"|\n\x12RegistroAsignacion\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0bid_vendedor\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x16\n\tid_tienda\x18\x03 \x01(\x05H\x02\x88\x01\x01\x42\x05\n\x03_idB\x0e\n\x0c_id_vendedorB\x0c\n\n_id_tienda\"K\n\x13ListadoAsignaciones\x12\x34\n\x0c\x61signaciones\x18\x01 \x03(\x0b\x32\x1e.vendedores.RegistroAsignacion2\xcd\x04\n\x0e\x41\x64ministracion\x12H\n\x12registrar_vendedor\x12\x1c.vendedores.RegistroVendedor\x1a\x12.vendedores.Status\"\x00\x12\x44\n\x10registrar_tienda\x12\x1a.vendedores.RegistroTienda\x1a\x12.vendedores.Status\"\x00\x12H\n\x10\x61signar_a_tienda\x12\x1e.vendedores.RegistroAsignacion\x1a\x12.vendedores.Status\"\x00\x12\x44\n\x0flistado_tiendas\x12\x11.vendedores.Empty\x1a\x1a.vendedores.RegistroTienda\"\x00\x30\x01\x12I\n\x12listado_vendedores\x12\x11.vendedores.Empty\x1a\x1c.vendedores.RegistroVendedor\"\x00\x30\x01\x12L\n\x14listado_asignaciones\x12\x11.vendedores.Empty\x1a\x1f.vendedores.ListadoAsignaciones\"\x00\x12@\n\x10\x61grega_productos\x12\x14.vendedores.Producto\x1a\x12.vendedores.Status\"\x00(\x01\x12@\n\x11listado_productos\x12\x11.vendedores.Empty\x1a\x14.vendedores.Producto\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'administracion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=36
  _EMPTY._serialized_end=43
  _STATUS._serialized_start=45
  _STATUS._serialized_end=87
  _PRODUCTO._serialized_start=89
  _PRODUCTO._serialized_end=201
  _REGISTROVENDEDOR._serialized_start=204
  _REGISTROVENDEDOR._serialized_end=340
  _REGISTROTIENDA._serialized_start=342
  _REGISTROTIENDA._serialized_end=464
  _REGISTROASIGNACION._serialized_start=466
  _REGISTROASIGNACION._serialized_end=590
  _LISTADOASIGNACIONES._serialized_start=592
  _LISTADOASIGNACIONES._serialized_end=667
  _ADMINISTRACION._serialized_start=670
  _ADMINISTRACION._serialized_end=1259
# @@protoc_insertion_point(module_scope)
