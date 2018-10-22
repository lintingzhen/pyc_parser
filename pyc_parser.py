#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Create Date: 2018-10-19 10:40
# Author: Airlam

import sys
import time
from lxml import etree
import opcode


def r_long(f):
    data = bytearray(f.read(4))
    m = data[0]
    m |= data[1] << 8
    m |= data[2] << 16
    m |= data[3] << 24
    return m


def r_long64(f):
    data = bytearray(f.read(8))
    m = data[0]
    m |= data[1] << 8
    m |= data[2] << 16
    m |= data[3] << 24
    m |= data[4] << 32
    m |= data[5] << 40
    m |= data[6] << 48
    m |= data[7] << 56
    return m


def r_str_raw_object(f, b=False):
    s = etree.Element("str")

    length = r_long(f)
    s.set("length", str(length))
    if not b:
        s.set("value", f.read(length))
    else:
        s.set("value", "".join(["\\x{:02x}".format(ord(c)) for c in f.read(length)]))

    return s


intern_string_index = 0


def r_str_interned_object(f):
    s = etree.Element("internStr")

    global intern_string_index
    s.set("index", str(intern_string_index))
    intern_string_index += 1

    length = r_long(f)
    s.set("length", str(length))
    s.set("value", f.read(length))
    return s


def r_str_ref_object(f):
    r = etree.Element("refStr")
    ref = r_long(f)
    r.set("ref", str(ref))
    return r


def r_tuple_object(f, tag="tuple"):
    t = etree.Element(tag)
    size = r_long(f)
    while size > 0:
        t.append(sr_object(f))
        size -= 1
    return t


def r_list_object(f, tag="list"):
    t = etree.Element(tag)
    size = r_long(f)
    while size > 0:
        t.append(sr_object(f))
        size -= 1
    return t


def r_dict_object(f, tag="dict"):
    t = etree.Element(tag)
    while 1:
        key = sr_object(f)
        if key is None:
            break
        ke = etree.Element("key")
        ke.append(key)
        t.append(ke)

        ve = etree.Element("value")
        ve.append(sr_object(f))
        t.append(ve)
    return t


def r_none_object(_):
    return etree.Element("NoneObject")


def r_null_object(_):
    return None


def r_int_object(f):
    return etree.Element("int", value=str(r_long(f)))


def r_int64_object(f):
    return etree.Element("int64", value=str(r_long64(f)))


def r_long_object(f):
    return etree.Element("long", value=str(r_long(f)))


def r_code_list(data, parent):
    size = len(data)
    i = 0
    while i < size:
        instruction = data[i]
        p = i
        op = opcode.opname[instruction]
        if instruction >= opcode.HAVE_ARGUMENT:
            arg = data[i + 1] + (data[i + 2] << 8)
            ins_p = "{:>3d} {} {}".format(p, op, arg)
            i += 3
        else:
            ins_p = "{:>3d} {}".format(p, op)
            i += 1
        parent.append(etree.Element("ins", value=ins_p))


def r_code_object(f):
    def r_long_element(f, tag):
        v = r_long(f)
        return etree.Element(tag, value="{}".format(v))

    def r_code_code_object(f):
        e = etree.Element("code")
        length = r_long(f)
        data = bytearray(f.read(length))
        e.append(etree.Element("raw", value="".join(["\\x{:02x}".format(c) for c in data])))
        r_code_list(data, e)
        return e

    def sr_str_object(f, tag=None, binary=False):
        t = f.read(1)
        assert t in ("s", "t", "R")
        if t == "s":
            s = r_str_raw_object(f, binary)
        else:
            s = object_unmarshal_method_map[t](f)

        if tag:
            wrap = etree.Element(tag)
            wrap.append(s)
            return wrap
        else:
            return s

    code = etree.Element("codeObject")
    code.append(r_long_element(f, "argCount"))
    code.append(r_long_element(f, "nLocals"))
    code.append(r_long_element(f, "stackSize"))
    code.append(r_long_element(f, "flags"))

    assert f.read(1) == 's'
    code.append(r_code_code_object(f))

    assert f.read(1) == '('
    code.append(r_tuple_object(f, "consts"))

    assert f.read(1) == '('
    code.append(r_tuple_object(f, "names"))

    assert f.read(1) == '('
    code.append(r_tuple_object(f, "varNames"))

    assert f.read(1) == '('
    code.append(r_tuple_object(f, "freeVars"))

    assert f.read(1) == '('
    code.append(r_tuple_object(f, "cellVars"))

    code.append(sr_str_object(f, "fileName"))
    code.append(sr_str_object(f, "name"))

    code.append(r_long_element(f, "firstLineNo"))

    code.append(sr_str_object(f, "lnotab", True))

    return code


object_unmarshal_method_map = {
    "N": r_none_object,
    "c": r_code_object,
    "(": r_tuple_object,
    "s": r_str_raw_object,
    "t": r_str_interned_object,
    "R": r_str_ref_object,
    "l": r_long_object,
    "i": r_int_object,
    "I": r_int64_object,
    "[": r_list_object,
    "{": r_dict_object,
    "0": r_null_object,
}


def sr_object(f):
    t = f.read(1)
    if t in object_unmarshal_method_map:
        return object_unmarshal_method_map[t](f)
    else:
        print "unknown object type: {}".format(t)
        assert 0


def r_magic(f):
    return "0x{:08x}".format(r_long(f))


def r_time(f):
    return time.ctime(r_long(f))


def main(argv):
    if argv:
        pyc_file = argv[0]
    else:
        pyc_file = "demo.pyc"

    xml_file = "{}.xml".format(pyc_file[:pyc_file.rfind('.')])

    root = etree.Element("PycFile")
    with open(pyc_file, "rb") as f:
        root.set("magic", r_magic(f))
        root.set("time", r_time(f))
        f.read(1)
        root.append(r_code_object(f))

    with open(xml_file, "w+") as of:
        of.write(etree.tostring(root, pretty_print=True))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

