# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BuildInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBuildInfo(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BuildInfo()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def BuildInfoBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x53\x52\x4F\x4D", size_prefixed=size_prefixed)

    # BuildInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BuildInfo
    def Banner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BuildInfo
    def Style(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BuildInfo
    def Tag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def BuildInfoStart(builder): builder.StartObject(3)
def BuildInfoAddBanner(builder, banner): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(banner), 0)
def BuildInfoAddStyle(builder, style): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(style), 0)
def BuildInfoAddTag(builder, tag): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(tag), 0)
def BuildInfoEnd(builder): return builder.EndObject()