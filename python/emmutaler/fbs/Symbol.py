# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Symbol(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSymbol(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Symbol()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def SymbolBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x53\x52\x4F\x4D", size_prefixed=size_prefixed)

    # Symbol
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Symbol
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Symbol
    def Start(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Symbol
    def End(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Symbol
    def FileStart(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Symbol
    def FileEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Symbol
    def CDefinition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def SymbolStart(builder): builder.StartObject(7)
def SymbolAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def SymbolAddStart(builder, start): builder.PrependUint64Slot(2, start, 0)
def SymbolAddEnd(builder, end): builder.PrependUint64Slot(3, end, 0)
def SymbolAddFileStart(builder, fileStart): builder.PrependUint64Slot(4, fileStart, 0)
def SymbolAddFileEnd(builder, fileEnd): builder.PrependUint64Slot(5, fileEnd, 0)
def SymbolAddCDefinition(builder, cDefinition): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(cDefinition), 0)
def SymbolEnd(builder): return builder.EndObject()


class SymbolT(object):

    # SymbolT
    def __init__(self):
        self.name = None  # type: str
        self.start = 0  # type: int
        self.end = 0  # type: int
        self.fileStart = 0  # type: int
        self.fileEnd = 0  # type: int
        self.cDefinition = None  # type: str

    @classmethod
    def InitFromBuf(cls, buf, pos):
        symbol = Symbol()
        symbol.Init(buf, pos)
        return cls.InitFromObj(symbol)

    @classmethod
    def InitFromObj(cls, symbol):
        x = SymbolT()
        x._UnPack(symbol)
        return x

    # SymbolT
    def _UnPack(self, symbol):
        if symbol is None:
            return
        self.name = symbol.Name()
        self.start = symbol.Start()
        self.end = symbol.End()
        self.fileStart = symbol.FileStart()
        self.fileEnd = symbol.FileEnd()
        self.cDefinition = symbol.CDefinition()

    # SymbolT
    def Pack(self, builder):
        if self.name is not None:
            name = builder.CreateString(self.name)
        if self.cDefinition is not None:
            cDefinition = builder.CreateString(self.cDefinition)
        SymbolStart(builder)
        if self.name is not None:
            SymbolAddName(builder, name)
        SymbolAddStart(builder, self.start)
        SymbolAddEnd(builder, self.end)
        SymbolAddFileStart(builder, self.fileStart)
        SymbolAddFileEnd(builder, self.fileEnd)
        if self.cDefinition is not None:
            SymbolAddCDefinition(builder, cDefinition)
        symbol = SymbolEnd(builder)
        return symbol