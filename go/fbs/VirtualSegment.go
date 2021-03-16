// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package fbs

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type VirtualSegmentT struct {
	Start uint64
	Size uint64
}

func (t *VirtualSegmentT) Pack(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	if t == nil { return 0 }
	return CreateVirtualSegment(builder, t.Start, t.Size)
}
func (rcv *VirtualSegment) UnPackTo(t *VirtualSegmentT) {
	t.Start = rcv.Start()
	t.Size = rcv.Size()
}

func (rcv *VirtualSegment) UnPack() *VirtualSegmentT {
	if rcv == nil { return nil }
	t := &VirtualSegmentT{}
	rcv.UnPackTo(t)
	return t
}

type VirtualSegment struct {
	_tab flatbuffers.Struct
}

func (rcv *VirtualSegment) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *VirtualSegment) Table() flatbuffers.Table {
	return rcv._tab.Table
}

func (rcv *VirtualSegment) Start() uint64 {
	return rcv._tab.GetUint64(rcv._tab.Pos + flatbuffers.UOffsetT(0))
}
func (rcv *VirtualSegment) MutateStart(n uint64) bool {
	return rcv._tab.MutateUint64(rcv._tab.Pos+flatbuffers.UOffsetT(0), n)
}

func (rcv *VirtualSegment) Size() uint64 {
	return rcv._tab.GetUint64(rcv._tab.Pos + flatbuffers.UOffsetT(8))
}
func (rcv *VirtualSegment) MutateSize(n uint64) bool {
	return rcv._tab.MutateUint64(rcv._tab.Pos+flatbuffers.UOffsetT(8), n)
}

func CreateVirtualSegment(builder *flatbuffers.Builder, start uint64, size uint64) flatbuffers.UOffsetT {
	builder.Prep(8, 16)
	builder.PrependUint64(size)
	builder.PrependUint64(start)
	return builder.Offset()
}