最近看陈儒的《Python源码剖析》一书，其中讲解pyc文件结构时，提到解析工具pycparser，网上没找到源码，所以自己动手写一个。

**! 目前仅针对python版本区间[2.5, 2.7.12]内的pyc格式**

files:
- demo.py是示例脚本。
- pyc_generator.py是生成pyc文件的脚本
- pyc_parser.py是解析pyc，输出xml文件的脚本

usage:
```
$ python pyc_generator.py demo  # 注意demo后面没有.py后缀
$ python pyc_parser.py demo.pyc
```
即可生成r.xml结果文件。

目前demo.pyc解析后的xml内容如下（xml格式大致模仿书中的实例，略有改动）：
```
<PycFile magic="0x0a0df2b3" time="Thu Oct 18 13:10:37 2018">
  <codeObject>
    <argCount value="0"/>
    <nLocals value="0"/>
    <stackSize value="3"/>
    <flags value="64"/>
    <code>
      <raw length="48" value="\x64\x00\x00\x64\x04\x00\x64\x01\x00\x84\x00\x00\x83\x00\x00\x59\x5a\x00\x00\x64\x02\x00\x84\x00\x00\x5a\x01\x00\x65\x00\x00\x83\x00\x00\x5a\x02\x00\x65\x01\x00\x83\x00\x00\x01\x64\x03\x00\x53"/>
      <insList>
        <ins value="  0 LOAD_CONST 0"/>
        <ins value="  3 LOAD_CONST 4"/>
        <ins value="  6 LOAD_CONST 1"/>
        <ins value="  9 MAKE_FUNCTION 0"/>
        <ins value=" 12 CALL_FUNCTION 0"/>
        <ins value=" 15 BUILD_CLASS"/>
        <ins value=" 16 STORE_NAME 0"/>
        <ins value=" 19 LOAD_CONST 2"/>
        <ins value=" 22 MAKE_FUNCTION 0"/>
        <ins value=" 25 STORE_NAME 1"/>
        <ins value=" 28 LOAD_NAME 0"/>
        <ins value=" 31 CALL_FUNCTION 0"/>
        <ins value=" 34 STORE_NAME 2"/>
        <ins value=" 37 LOAD_NAME 1"/>
        <ins value=" 40 CALL_FUNCTION 0"/>
        <ins value=" 43 POP_TOP"/>
        <ins value=" 44 LOAD_CONST 3"/>
        <ins value=" 47 RETURN_VALUE"/>
      </insList>
    </code>
    <consts>
      <internStr index="0" length="1" value="A"/>
      <codeObject>
        <argCount value="0"/>
        <nLocals value="0"/>
        <stackSize value="1"/>
        <flags value="66"/>
        <code>
          <raw length="8" value="\x65\x00\x00\x5a\x01\x00\x52\x53"/>
          <insList>
            <ins value="  0 LOAD_NAME 0"/>
            <ins value="  3 STORE_NAME 1"/>
            <ins value="  6 LOAD_LOCALS"/>
            <ins value="  7 RETURN_VALUE"/>
          </insList>
        </code>
        <consts/>
        <names>
          <internStr index="1" length="8" value="__name__"/>
          <internStr index="2" length="10" value="__module__"/>
        </names>
        <varNames/>
        <freeVars/>
        <cellVars/>
        <fileName>
          <str length="25" value="/data/python/code/demo.py"/>
        </fileName>
        <name>
          <refStr ref="0"/>
        </name>
        <firstLineNo value="1"/>
        <lnotab>
          <str length="2" value="\x06\x01"/>
        </lnotab>
      </codeObject>
      <codeObject>
        <argCount value="0"/>
        <nLocals value="0"/>
        <stackSize value="1"/>
        <flags value="67"/>
        <code>
          <raw length="4" value="\x64\x00\x00\x53"/>
          <insList>
            <ins value="  0 LOAD_CONST 0"/>
            <ins value="  3 RETURN_VALUE"/>
          </insList>
        </code>
        <consts>
          <NoneObject/>
        </consts>
        <names/>
        <varNames/>
        <freeVars/>
        <cellVars/>
        <fileName>
          <str length="25" value="/data/python/code/demo.py"/>
        </fileName>
        <name>
          <internStr index="3" length="4" value="Func"/>
        </name>
        <firstLineNo value="4"/>
        <lnotab>
          <str length="2" value="\x00\x01"/>
        </lnotab>
      </codeObject>
      <NoneObject/>
      <tuple/>
    </consts>
    <names>
      <refStr ref="0"/>
      <refStr ref="3"/>
      <internStr index="4" length="1" value="a"/>
    </names>
    <varNames/>
    <freeVars/>
    <cellVars/>
    <fileName>
      <str length="25" value="/data/python/code/demo.py"/>
    </fileName>
    <name>
      <str length="8" value="&lt;module&gt;"/>
    </name>
    <firstLineNo value="1"/>
    <lnotab>
      <str length="6" value="\x13\x03\x09\x03\x09\x01"/>
    </lnotab>
  </codeObject>
</PycFile>
```
