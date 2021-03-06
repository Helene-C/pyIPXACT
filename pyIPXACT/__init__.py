# EMACS settings: -*- tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python package:     A DOM based IP-XACT implementation for Python
#
# Description:
# ------------------------------------
#   TODO:
#
# License:
# ==============================================================================
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#
from textwrap import dedent

from pathlib import Path


class IpxactSchemaStruct:
	def __init__(self, version, namespacePrefix, schemaUri, schemaUrl, localPath):
		self.Version =         version
		self.NamespacePrefix = namespacePrefix
		self.SchemaUri =       schemaUri
		self.SchemaUrl =       schemaUrl
		self.LocalPath =       localPath


_SCHEMA_PATH =  Path("lib/schema")  #version, xmlns, URI                                                            URL,                                                              Local Path
_IPXACT_10 =    IpxactSchemaStruct("1.0", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",         "",                                                               _SCHEMA_PATH / "1.0")
_IPXACT_11 =    IpxactSchemaStruct("1.1", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",         "",                                                               _SCHEMA_PATH / "1.1")
_IPXACT_14 =    IpxactSchemaStruct("1.4", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",         "",                                                               _SCHEMA_PATH / "1.4")
_IPXACT_15 =    IpxactSchemaStruct("1.5", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",         "",                                                               _SCHEMA_PATH / "1.5")
_IPXACT_2009 =  IpxactSchemaStruct("2009", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",  "",                                                               _SCHEMA_PATH / "2009")
_IPXACT_2014 =  IpxactSchemaStruct("2014", "ipxact", "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",         "http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd",  _SCHEMA_PATH / "2014")

__VERSION_TABLE__ = {
	'1.0':   _IPXACT_10,
	'1.1':   _IPXACT_11,
	'1.4':   _IPXACT_14,
	'1.5':   _IPXACT_15,
	'2009':  _IPXACT_2009,
	'2014':  _IPXACT_2014
}
__URI_MAP__ = {value.SchemaUri: value for key, value in __VERSION_TABLE__.items()}


__DEFAULT_VERSION__ = "2014"
__DEFAULT_SCHEMA__ =  __VERSION_TABLE__[__DEFAULT_VERSION__]


class RootElement:
	def __init__(self, vlnv):
		self._vlnv =    vlnv

	@classmethod
	def FromFile(cls, file):
		pass


class Vlnv:
	def __init__(self, vendor, library, name, version):
		self.Vendor =   vendor
		self.Library =  library
		self.Name =     name
		self.Version =  version
	
	def ToXml(self, indent=1, isVersionedIdentifier=False):
		if isVersionedIdentifier:
			buffer = dedent("""\
				{indent}<{xmlns}:vendor>{vendor}</{xmlns}:vendor>
				{indent}<{xmlns}:library>{library}</{xmlns}:library>
				{indent}<{xmlns}:name>{name}</{xmlns}:name>
				{indent}<{xmlns}:version>{version}</{xmlns}:version>\
			""")
		else:
			buffer = """{indent}<{xmlns}:vlnv vendor="{vendor}" library="{library}" name="{name}" version="{version}"/>"""
		
		return buffer.format(indent= "\t" *indent, xmlns=__DEFAULT_SCHEMA__.NamespacePrefix, vendor=self.Vendor, library=self.Library, name=self.Name, version=self.Version)

class PyIpxactException(Exception):
	pass
